#!/usr/bin/env python3

import argparse
import struct
import os
import hashlib

# fmt: off
jpeg_markers = {
    # 00, 01, FE, C0, DF
    # Rec. ITU-T T.81 | ISO/IEC 10918-1

    # F0-F6
    # Rec. ITU-T T.84 | ISO/IEC 10918-3

    # F7-F8
    # Rec. ITU-T T.87 | ISO/IEC 14495-1

    # 4F-6F, 90-93
    # Rec. ITU-T T.800 | ISO/IEC 15444-1

    # 30-3F
    # Reserverd for definition as markers only (no marker segments)


    # 01-0F
                     0xFF01: "TEM",
                                      0xFF0A: "JXL",

    # 10-1F

    # 20-2F

    # 30-3F

    # 40-4F
                                                       0xFF4F: "SOC",

    # 50-5F
    0xFF50: "CAP",   0xFF51: "SIZ",   0xFF52: "COD",   0xFF53: "COC",
    0xFF54: "NSI",   0xFF55: "TLM",   0xFF56: "PRF",   0xFF57: "PLM",
    0xFF58: "PLT",   0xFF59: "CPF",   0xFF5A: "QPD",   0xFF5B: "QPC",
    0xFF5C: "QCD",   0xFF5D: "QCC",   0xFF5E: "RGN",   0xFF5F: "POC",

    # 60-6F
    # ILL is taken from the CREW patent, table 3
    # https://patents.google.com/patent/US20060233257A1
    0xFF60: "PPM",   0xFF61: "PPT",   0xFF62: "ILL",   0xFF63: "CRG",
    0xFF64: "COM",   0xFF65: "SEC",   0xFF66: "EPB",   0xFF67: "ESD",
    0xFF68: "EPC",   0xFF69: "RED",

    # 70-7F
    0xFF70: "DCO",   0xFF71: "VMS",   0xFF72: "DFS",   0xFF73: "ADS",
    0xFF74: "MCT",   0xFF75: "MCC",   0xFF76: "NLT",   0xFF77: "MCO",
    0xFF78: "CBD",   0xFF79: "ATK",

    # 90-9F
    0xFF90: "SOT",   0xFF91: "SOP",   0xFF92: "EPH",   0xFF93: "SOD",
    0xFF94: "INSEC",

    # C0-CF
    0xFFC0: "SOF0",  0xFFC1: "SOF1",  0xFFC2: "SOF2",  0xFFC3: "SOF3",
    0xFFC4: "DHT",   0xFFC5: "SOF5",  0xFFC6: "SOF6",  0xFFC7: "SOF7",
    0xFFC8: "JPG",   0xFFC9: "SOF9",  0xFFCA: "SOF10", 0xFFCB: "SOF11",
    0xFFCC: "DAC",   0xFFCD: "SOF13", 0xFFCE: "SOF14", 0xFFCF: "SOF15",

    # D0-DF
    0xFFD0: "RST0",  0xFFD1: "RST1",  0xFFD2: "RST2",  0xFFD3: "RST3",
    0xFFD4: "RST4",  0xFFD5: "RST5",  0xFFD6: "RST6",  0xFFD7: "RST7",
    0xFFD8: "SOI",   0xFFD9: "EOI/C", 0xFFDA: "SOS",   0xFFDB: "DQT",
    0xFFDC: "DNL",   0xFFDD: "DRI",   0xFFDE: "DHP",   0xFFDF: "EXP",

    # E0-EF
    0xFFE0: "APP0",  0xFFE1: "APP1",  0xFFE2: "APP2",   0xFFE3: "APP3",
    0xFFE4: "APP4",  0xFFE5: "APP5",  0xFFE6: "APP6",   0xFFE7: "APP7",
    0xFFE8: "APP8",  0xFFE9: "APP9",  0xFFEA: "APP10",  0xFFEB: "APP11",
    0xFFEC: "APP12", 0xFFED: "APP13", 0xFFEE: "APP14",  0xFFEF: "APP15",

    # F0-FE
    0xFFF0: "VER",   0xFFF1: "DTI",   0xFFF2: "DTT",    0xFFF3: "SRF",
    0xFFF4: "SRS",   0xFFF5: "DCR",   0xFFF6: "DQS",    0xFFF7: "SOF55",
    0xFFF8: "LSE",   0xFFF9: "JPG9",  0xFFFA: "JPG10",  0xFFFB: "JPG11",
    0xFFFC: "JPG12", 0xFFFD: "JPG13", 0xFFFE: "COM",
}

paramterless_jpeg_markers = [
    0xFF01, 0xFF0A,                 # TEM, JXL

                            0xFF4F, # SOC

    0xFF30, 0xFF31, 0xFF32, 0xFF33, # RES (Reserved), guaranteed parameter less
    0xFF34, 0xFF35, 0xFF36, 0xFF37,
    0xFF38, 0xFF39, 0xFF3A, 0xFF3B,
    0xFF3C, 0xFF3D, 0xFF3E, 0xFF3F,

                    0xFF92, 0xFF93, # EPH, SOD

    0xFFD0, 0xFFD1, 0xFFD2, 0xFFD3, # RST0, RST1, RST2, RST3
    0xFFD4, 0xFFD5, 0xFFD6, 0xFFD7, # RST4, RST5, RST6, RST7
    0xFFD8, 0xFFD9,                 # SOI, EOI/EOC
]

valid_bitstream_markers = [
    0xFF00,
    0xFF90,                         # SOT
    0xFFD0, 0xFFD1, 0xFFD2, 0xFFD3, # RST0, RST1, RST2, RST3
    0xFFD4, 0xFFD5, 0xFFD6, 0xFFD7, # RST4, RST5, RST6, RST7
    0xFFD8, 0xFFD9,                 # SOI, EOI/EOC
]

start_of_bitsream_markers = [
    0xFFD0, 0xFFD1, 0xFFD2, 0xFFD3, # RST0, RST1, RST2, RST3
    0xFFD4, 0xFFD5, 0xFFD6, 0xFFD7, # RST4, RST5, RST6, RST7

    0xFF93, 0xFFDA,                 # SOD, SOS
]

end_of_bitstream_markers = [
    0xFFD9, 0xFF90                  # EOI/EOC, SOT
]
# fmt: on


def read_image_data(f, bitstream_marker_code):
    CHUNK_SIZE = 4096
    data = b""
    orig_fpos = f.tell()
    search_offset = 0
    index = 0

    while True:
        chunk = f.read(CHUNK_SIZE)
        if not chunk:
            break  # End of file

        data += chunk

        # spin through allowed markers in image data
        while True:
            if search_offset >= len(data):
                break  # read more data

            index = data.find(b"\xFF", search_offset)

            if index == -1:
                break

            try:
                marker_code = data[index + 1] | 0xFF00
            except IndexError:
                break

            if bitstream_marker_code != 0xFF93:  # not SOD, i.e. "plain" JPEG
                # padding or stuffing, and RST markers
                if (
                    marker_code == 0xFFFF
                    or marker_code == 0xFF00
                    or 0xFFD0 <= marker_code <= 0xFFD7
                ):
                    search_offset = index + 2
                    continue
                else:  # SOS segment can contain any marker
                    data = data[:index]
                    # seek back to the first marker after bitstream data
                    f.seek(orig_fpos + index)
                    pos = f.tell()
                    return data
            else:  # SOD, JPEG 2000
                if marker_code == 0xFF91 or marker_code == 0xFF92:  # SOP or EPH
                    try:
                        segment_length_bytes = data[(index + 2) : (index + 4)]
                    except IndexError:
                        break  # read more data

                    segment_length = struct.unpack(">H", segment_length_bytes)[0]
                    search_offset = index + 2 + segment_length
                    continue
                elif marker_code in end_of_bitstream_markers:
                    data = data[:index]
                    f.seek(orig_fpos + index)
                    return data
                else:
                    search_offset = index + 2
                    continue

    return data  # End of file


def segment_string(offset, marker_code, data=None):
    if marker_code:
        marker_name = jpeg_markers.get(marker_code, "RES")
        marker_name = f"{marker_name:5} (0x{marker_code:04X})  "
    else:
        marker_code = ""
        marker_name = "[bitstream data]"
        marker_name = f"{marker_name:14}"

    segment_len = len(data)
    if segment_len > 0:
        segment_hash = hashlib.sha256(data).hexdigest()
    else:
        segment_hash = ""

    return f"{offset:06X}: {marker_name} {segment_len:>8}  {segment_hash}"


def read_jpeg_markers(file_path):
    try:
        with open(file_path, "rb") as f:
            offset = 0  # Initialize the offset to 0
            marker_code = 0
            print("{:7} {:16} {:>8}  {}".format("Offset", "Marker", "Length", "Hash"))

            while True:
                # Read the byte
                marker_byte = f.read(1)
                if not marker_byte:
                    break  # End of file

                # convert to int
                marker_byte = ord(marker_byte)

                # Check for valid marker (start with 0xFF)
                if marker_byte != 0xFF:
                    offset += 1
                    continue

                # Get the marker code (second byte)
                marker_code = f.read(1)
                if not marker_code:
                    break  # End of file

                # convert to int
                marker_code = ord(marker_code) | 0xFF00

                # 0xFF is used for padding
                if marker_code == 0xFF00:
                    offset += 1
                    continue

                # Only read segment length for markers with parameters
                if marker_code not in paramterless_jpeg_markers:
                    # Read the marker segment length (two bytes)
                    segment_length_bytes = f.read(2)
                    segment_length = struct.unpack(">H", segment_length_bytes)[0]

                    # Read the marker segment data
                    data_segment = f.read(segment_length - 2)
                    if not data_segment:
                        break  # End of file

                    data_segment = segment_length_bytes + data_segment
                    hash = hashlib.sha256(data_segment)
                    hash_string = hash.hexdigest()

                    offset += len(data_segment)
                else:
                    data_segment = b""
                    segment_length = 0
                    hash_string = ""

                print(segment_string(offset, marker_code, data_segment))

                # increase offset for marker bytes
                offset += 2

                if marker_code in start_of_bitsream_markers:
                    data = read_image_data(f, marker_code)
                    hash = hashlib.sha256(data)
                    hash_string = hash.hexdigest()
                    print(segment_string(offset, None, data))
                    offset += len(data)

    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    parser = argparse.ArgumentParser(description="Read JPEG marker segments.")
    parser.add_argument("file_name", type=str, help="Path to the JPEG file")

    args = parser.parse_args()
    read_jpeg_markers(args.file_name)


if __name__ == "__main__":
    main()
