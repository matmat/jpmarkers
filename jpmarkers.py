#!/usr/bin/env python3

import argparse
import struct

jpeg_markers = {
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
    0xFFF0: "JPG0",  0xFFF1: "JPG1",  0xFFF2: "JPG2",   0xFFF3: "JPG3",
    0xFFF4: "JPG4",  0xFFF5: "JPG5",  0xFFF6: "JPG6",   0xFFF7: "SOF48",
    0xFFF8: "LSE",   0xFFF9: "JPG9",  0xFFFA: "JPG10",  0xFFFB: "JPG11",
    0xFFFC: "JPG12", 0xFFFD: "JPG13", 0xFFFE: "COM",
}

paramterless_jpeg_markers = [
    0xFF01, 0xFF0A,                 # TEM, JXL

    0xFF30, 0xFF31, 0xFF32, 0xFF33, # RES (Reserved), guaranteed parameter less
    0xFF34, 0xFF35, 0xFF36, 0xFF37,
    0xFF38, 0xFF39, 0xFF3A, 0xFF3B,
    0xFF3C, 0xFF3D, 0xFF3E, 0xFF3F,

    0xFFD0, 0xFFD1, 0xFFD2, 0xFFD3, # RST0, RST1, RST2, RST3
    0xFFD4, 0xFFD5, 0xFFD6, 0xFFD7, # RST4, RST5, RST6, RST7
    0xFFD8, 0xFFD9,                 # SOI, EOI/EOC
]


def read_jpeg_markers(file_path):
    try:
        with open(file_path, "rb") as f:
            while True:
                # Read the byte
                marker_byte = f.read(1)
                if not marker_byte:
                    break  # End of file

                marker_byte = struct.unpack("B", marker_byte)[0]

                # Check for valid marker (start with 0xFF)
                if marker_byte != 0xFF:
                    continue

                # Get the marker code (second byte)
                marker_code = f.read(1)
                if not marker_code:
                    break  # End of file

                marker_code = struct.unpack("B", marker_code)[0]

                # Encoded 0xFF
                if marker_code == 0x00:
                    continue

                # Determine the marker name based on the code
                marker_hexstring = f"0xFF{marker_code:02X}"

                # Only read segment length for marker that has it
                if marker_code < 0xD0 or marker_code > 0xD9:
                    # Read the marker segment length (two bytes)
                    segment_length_bytes = f.read(2)
                    segment_length = struct.unpack(">H", segment_length_bytes)[0]

                    # Read the marker segment data
                    data_segment = f.read(
                        segment_length - 2
                    )  # Subtract 2 for the length bytes

                # Convert marker bytes to an integer using struct.unpack
                marker_int = marker_code | 0xFF00

                marker_name = jpeg_markers.get(marker_int, "UNKNOWN")

                # Print marker name and hex bytes
                print(f"{marker_hexstring} ({marker_name})")
    #                print(f"{marker_hexstring}")
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
