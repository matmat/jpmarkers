#!/usr/bin/env python3

import argparse
import struct

jpeg_markers = {
    0xFFD8: 'SOI',
    0xFFE0: 'APP0',
    0xFFE1: 'APP1',
    0xFFE2: 'APP2',
    0xFFE3: 'APP3',
    0xFFE4: 'APP4',
    0xFFE5: 'APP5',
    0xFFE6: 'APP6',
    0xFFE7: 'APP7',
    0xFFE8: 'APP8',
    0xFFE9: 'APP9',
    0xFFEA: 'APP10',
    0xFFEB: 'APP11',
    0xFFEC: 'APP12',
    0xFFED: 'APP13',
    0xFFEE: 'APP14',
    0xFFEF: 'APP15',
    0xFFFE: 'COM',
    0xFFDB: 'DQT',
    0xFFC0: 'SOF0',
    0xFFC1: 'SOF1',
    0xFFC2: 'SOF2',
    0xFFC3: 'SOF3',
    0xFFC4: 'DHT',
    0xFFC5: 'SOF5',
    0xFFC6: 'SOF6',
    0xFFC7: 'SOF7',
    0xFFC8: 'JPG',
    0xFFC9: 'SOF9',
    0xFFCA: 'SOF10',
    0xFFCB: 'SOF11',
    0xFFCC: 'DAC',
    0xFFCD: 'SOF13',
    0xFFCE: 'SOF14',
    0xFFCF: 'SOF15',
    0xFFD0: 'RST0',
    0xFFD1: 'RST1',
    0xFFD2: 'RST2',
    0xFFD3: 'RST3',
    0xFFD4: 'RST4',
    0xFFD5: 'RST5',
    0xFFD6: 'RST6',
    0xFFD7: 'RST7',
    0xFFD9: 'EOI',
    0xFFDA: 'SOS',
    0xFFDD: 'DRI',
    0xFFDE: 'DHP',
    0xFFDF: 'EXP'
}




def read_jpeg_markers(file_path):
    try:
        with open(file_path, "rb") as f:
            while True:
                # Read the marker (two bytes)
                marker_bytes = f.read(2)
                if not marker_bytes:
                    break  # End of file

                # Check for valid marker (start with 0xFF)
                if marker_bytes[0] != 0xFF:
                    continue

                # Get the marker code (second byte)
                marker_code = marker_bytes[1]

                # Determine the marker name based on the code
                marker_hexstring = f"0xFF{marker_code:02X}"

                # If the marker is 0xFFD8 (SOI) or 0xFFD9 (EOI), it has no data segment
                if marker_code == 0xD8 or marker_code == 0xD9:
                    data_segment = b""
                else:
                    # Read the marker segment length (two bytes)
                    segment_length_bytes = f.read(2)
                    segment_length = struct.unpack(">H", segment_length_bytes)[0]

                    # Read the marker segment data
                    data_segment = f.read(
                        segment_length - 2
                    )  # Subtract 2 for the length bytes


                # Convert marker bytes to an integer using struct.unpack
                marker_int = struct.unpack(">H", marker_bytes)[0]

                marker_name = jpeg_markers.get(marker_int, 'UNKNOWN')

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
