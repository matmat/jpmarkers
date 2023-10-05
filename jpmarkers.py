#!/usr/bin/env python3

import argparse
import struct
import os
import hashlib
from pprint import pprint
import sigs_jpegsnoop
import sigs_exiftool
import sigs_gdal
import numpy as np


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
    0xFFD8: "SOI",   0xFFD9: "EOI",   0xFFDA: "SOS",   0xFFDB: "DQT",
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

def read_image_data(file, bitstream_marker_code):
    CHUNK_SIZE = 4096
    data = bytearray()
    orig_fpos = file.tell()
    search_offset = 0
    index = 0
    stream_markers = {}

    while True:
        chunk = file.read(CHUNK_SIZE)
        if not chunk:
            break  # End of file

        data += chunk

        # spin through allowed markers in image data
        while True:
            if search_offset >= len(data):
                break  # read more data

            index = data.find(b"\xFF", search_offset)

            if index == -1:
                break   # Not found

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
                    #if 0xFFD0 <= marker_code <= 0xFFD7:
                    #    stream_markers[index] = jpeg_markers[marker_code]
                    search_offset = index + 2
                    continue
                else:  # SOS segment can contain any marker
                    data = data[:index]
                    # seek back to the first marker after bitstream data
                    file.seek(orig_fpos + index)
                    return (bytes(data), stream_markers) 
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
                    file.seek(orig_fpos + index)
                    return (bytes(data), stream_markers) 
                else:
                    search_offset = index + 2
                    continue

    return (bytes(data), stream_markers)  # End of file


# In:  dict of qtables (8x8 int matrix) indexed by target table id (int)
# Out: dict of md5 hexstrings indexed by target table id (int)
def hash_matrices(matrix_dict):

    hashed_dict = {}
    for key, matrix in matrix_dict.items():
        # Flatten the matrix and convert it to bytes
        flattened = bytes([item for sublist in matrix for item in sublist])
        # Compute the MD5 hash
        md5_hash = hashlib.md5(flattened)
        # Convert the hash to a hexadecimal string
        hex_digest = md5_hash.hexdigest()
        # Add the hashed matrix to the new dictionary
        hashed_dict[key] = hex_digest
    return hashed_dict


def concat_hash_qtables(qtables):
    concatenated_arrays = []
    for arrays in qtables.values():
        for array in arrays:
            concatenated_arrays.extend(array)

    #print(concatenated_arrays)
    concatenated_bytes = bytes(concatenated_arrays)
    hash_object = hashlib.md5(concatenated_bytes)
    return hash_object.hexdigest()



def segment_string(offset, marker_code, data):

    if marker_code:
        segment_len = len(data) - 2
        marker_name = jpeg_markers.get(marker_code, "RES")
        marker_name = f"{marker_name:5} (0x{marker_code:04X})  "
    else:
        segment_len = len(data)
        marker_code = ""
        marker_name = "[bitstream data]"
        marker_name = f"{marker_name:14}"

    if len(data[2:]) > 0:
        segment_hash = hashlib.md5(data[2:]).hexdigest()
    else:
        segment_hash = ""

    return f"{offset:06X}: {marker_name} {segment_len:>8}  {segment_hash}"

def qdict_zigzag_to_linear(qtables):
    return {k: zigzag_to_linear_table(v) for k, v in qtables.items()}


def zigzag_to_linear_table(matrix):
    # Create a zigzag pattern for 8x8 matrix
    zigzag_pattern = [
        [ 0, 1, 5, 6, 14, 15, 27, 28],
        [ 2,  4,  7, 13, 16, 26, 29, 42],
        [ 3,  8, 12, 17, 25, 30, 41, 43],
        [ 9, 11, 18, 24, 31, 40, 44, 53],
        [10, 19, 23, 32, 39, 45, 52, 54],
        [20, 22, 33, 38, 46, 51, 55, 60],
        [21, 34, 37, 47, 50, 56, 59, 61],
        [35, 36, 48, 49, 57, 58, 62, 63]
    ]

    # Flatten the input matrix
    flat_matrix = [item for sublist in matrix for item in sublist]

    # Flatten the zigzag pattern
    flat_zigzag = [item for sublist in zigzag_pattern for item in sublist]

    # Get the linear order of the matrix in zigzag pattern
    linear_order = [flat_matrix[i] for i in flat_zigzag]

    # Reshape the linear order back to 8x8 matrix
    matrix_order = [linear_order[i:i+8] for i in range(0, len(linear_order), 8)]

    return matrix_order

def linear_to_zigzag_table(matrix):
    # Create a zigzag pattern for 8x8 matrix
    zigzag_pattern = [
        [ 0, 1, 5, 6, 14, 15, 27, 28],
        [ 2, 4, 7, 13, 16, 26, 29, 42],
        [ 3, 8, 12, 17, 25, 30, 41, 43],
        [ 9, 11, 18, 24, 31, 40, 44, 53],
        [10, 19, 23, 32, 39, 45, 52, 54],
        [20, 22, 33, 38, 46, 51, 55, 60],
        [21, 34, 37, 47, 50, 56, 59, 61],
        [35, 36, 48, 49, 57, 58, 62, 63]
    ]

    # Flatten the input matrix
    flat_matrix = [item for sublist in matrix for item in sublist]

    # Flatten the zigzag pattern
    flat_zigzag = [item for sublist in zigzag_pattern for item in sublist]

    # Create an empty list of the same size as flat_matrix
    zigzag_order = [0]*len(flat_matrix)

    # Fill the zigzag_order list with elements from flat_matrix in the order of flat_zigzag
    for i, item in enumerate(flat_zigzag):
        zigzag_order[item] = flat_matrix[i]

    # Reshape the zigzag order back to 8x8 matrix
    matrix_order = [zigzag_order[i:i+8] for i in range(0, len(zigzag_order), 8)]

    return matrix_order


def transpose_matrix(matrix):
    return list(map(list, zip(*matrix)))

def transpose_qtables(qtables):
    transposed = {}
    for t in qtables.keys():
        #transposed[t] = list(map(list, zip(*qtables[t])))
        transposed[t] = transpose_matrix(qtables[t])
    return transposed



def gimp_hash_string(qtables):
    hashval = 11
    for t in sorted(qtables.keys()):
        for row in qtables[t]:
            for val in row:
                # Simulate overflow of 32 bit unsigned integer
                hashval = (hashval * 4177 + val) & 0xFFFFFFFF

    return format(hashval, '08x')


# GDAL hashes all DQT segments, including length bytes
def gdal_hash_string(qtable_data_segments):
    # Concatenate all byte objects
    qtable_bytestring = b''.join(qtable_data_segments)

    # Compute md5 hash
    md5_hash = hashlib.md5(qtable_bytestring)

    # Convert md5 hash to hexadecimal string
    hexdigest = md5_hash.hexdigest()

    return hexdigest


# Exiftool hashes the segments concatenated (excluding length bytes) and separated by \x00
def exiftool_hash_string(qtable_datasegments):
    # Discard the first two bytes of every element
    qtable_datasegments = [element[2:] for element in qtable_datasegments]

    # Extract the second nibble of each segment, "Quantization table destination identifier"
    # If there are more than one table with the same id, keep only the last one defined
    table_dict = {(element[0] & 0x0F): element for element in qtable_datasegments}

    # Sort the remaining elements by target table id and process at maximum four elements
    sorted_elements = sorted([value for key, value in table_dict.items() if key < 4])

    # Flatten the array and separate the original elements with a null byte
    null_separated = b'\x00'.join(sorted_elements)

    not_null_separated = b''.join(sorted_elements)
    md5_notnull = hashlib.md5(not_null_separated).hexdigest()

    #print("md5 not-null-separated: ", md5_notnull )

    # Take an md5 of this
    md5 = hashlib.md5(null_separated)

    # Return the md5 hex digest as a string
    return md5.hexdigest()

# Contruct the JPEGsnoop hash string as defined in
# CjfifDecode::PrepareSignatureSingle() in source/JfifDecode.cpp
def qtable_integer_string(qtable):
    return ','.join([f'{num:03}' for sublist in qtable for num in sublist]) + ','

def jpegsnoop_hash_string(qtables):
    hash_string = ''.join(f"*DQT{k},{qtable_integer_string(v)}" for k, v in qtables.items())
    hash_string = "JPEGsnoop" + hash_string + "*END"
    hash_string = hashlib.md5(hash_string.encode()).hexdigest()
    hash_string = "01" + hash_string[2:]
    return hash_string

# Format qtable dict in a kind of numpy-like way
def qtables_string(qtables):
    result = []
    for tbl_id, tbl in sorted(qtables.items()):
        tbl_id_str = str(tbl_id)
        tbl_str = []
        for row in tbl:
            row_str = ' '.join('{:2}'.format(int(num)) for num in row)
            tbl_str.append(row_str)
        result.append(tbl_id_str + '\n' + '\n'.join(tbl_str))
    return '\n'.join(result)


# Read qtables from *one* DQT segment and store them in the supplied
# qtables dict. Returns the numer of tables in the marker segment
def read_htables(data_segment):
    # discard length bytes
    #print("data_segment: ")
    #print("len(data_segment):", len(data_segment))
    #print(data_segment.hex())


    data = data_segment[2:]
    table_ids = [] # table ids
    while data:
        # Extract precision (upper 4 bits) and table id (lower 4 bits)
        #print("data: ")
        #print("len(data):", len(data))
        #print(data.hex())
        tbltype_and_id = data[0]
        tbltype = tbltype_and_id >> 4
        table_id = tbltype_and_id & 0x0F

        #print(f"tbltype: {tbltype}")
        #print(f"table_id: {table_id}")


        table_ids.append(str(table_id) + ":" + ["AC","DC"][tbltype])

        size_table          = data[1:17]
        #print(f"data[1:17]: {size_table.hex()}")
        #print(f"len(size_table): {len(size_table)}")


        symbol_table_length = sum(size_table)
        table_length        = 16 + symbol_table_length
        #print(f"symbol_table_length: {symbol_table_length}")
        #print(f"table_length: {table_length}")

        #print(f"len(data): {len(data)}")



        # Check if there's enough data for the next table
        # Take into account both segment length and Tc/Th
        if len(data) < 2 + table_length:
            break

        # Move on to the next table
        data = data[1+table_length:]
    return table_ids



# Read qtables from *one* DQT segment and store them in the supplied
# qtables dict. Returns the numer of tables in the marker segment
def read_qtables(data_segment, qtables):
    # discard length bytes
    data = data_segment[2:]
    Tq = [] # table ids
    while data:
        # Extract precision (upper 4 bits) and table id (lower 4 bits)
        precision_and_id = data[0]
        precision = precision_and_id >> 4
        table_id = precision_and_id & 0x0F

        Tq.append(table_id)

        # Determine the length of the table
        table_length = 64 * (2 if precision else 1)

        # Extract the table data
        table_data = data[1:1+table_length]

        # Convert the table data to a list of integers
        if precision:
            # 16-bit precision
            table = [int.from_bytes(table_data[i:i+2], 'big') for i in range(0, table_length, 2)]
        else:
            # 8-bit precision
            table = list(table_data)

        # Convert the linear table to a 8x8 matrix
        matrix = [table[i:i+8] for i in range(0, len(table), 8)]

        # Store the matrix in the qtables dict
        qtables[table_id] = matrix

        # Check if there's enough data for the next table
        if len(data) < 1 + table_length:
            break

        # Move on to the next table
        data = data[1+table_length:]
    return Tq


def transpose_matrix(matrix):
    return list(map(list, zip(*matrix)))

def transpose_data_segments(data_segments):
    return list(map(transpose_data_segment, data_segments))
    #print(len(r))
    #print("Returned, transposed data")
    #print(r)
    #return r


def transpose_data_segment(data_segment):
    #discard length bytes
    data = data_segment[2:]
    new_data_segment = bytearray()
    while data:
        # Extract precision (upper 4 bits) and table id (lower 4 bits)
        precision_and_id = data[0]
        precision = precision_and_id >> 4
        table_id = precision_and_id & 0x0F

        # Determine the length of the table
        table_length = 64 * (2 if precision else 1)

        # Extract the table data
        table_data = data[1:1+table_length]

        #print("table data")
        #print(table_data.hex())

        # Convert the table data to a list of integers
        if precision:
            # 16-bit precision
            table = [int.from_bytes(table_data[i:i+2], 'big') for i in range(0, table_length, 2)]
        else:
            # 8-bit precision
            table = list(table_data)

        # Convert the linear table to a 8x8 matrix
        matrix = [table[i:i+8] for i in range(0, len(table), 8)]

        # zigzag (stored order) to linear
        matrix = zigzag_to_linear_table(matrix)

        #print("matrix")
        #pprint(matrix)

        # Transpose the matrix
        transposed_matrix = transpose_matrix(matrix)

        #print("transposed matrix")
        #pprint(transposed_matrix)

        # Convert to zigzag order (for storage)
        transposed_matrix = linear_to_zigzag_table(transposed_matrix)

        # Flatten the transposed matrix
        flat_matrix = [item for sublist in transposed_matrix for item in sublist]

        # Convert the flat matrix back to bytes and append to new_data_segment
        new_data_segment.append(precision_and_id)
        if precision:
            for i in flat_matrix:
                new_data_segment.extend(i.to_bytes(2, 'big'))
        else:
            new_data_segment.extend(flat_matrix)

        # Check if there's enough data for the next table
        if len(data) < 1 + table_length:
            break

        # Move on to the next table
        data = data[1+table_length:]

    # prepend length bytes
    #print ("old      data: ", (data_segment.hex())) 
    #print ("returned data: ", (data_segment[:2] + new_data_segment).hex())
    return data_segment[:2] + new_data_segment


def merge_dicts_add_val_to_keys(dict1, dict2, add_value):
    #print("merge_dicts:", hex(add_value))

    new_dict2 = {k+add_value: v for k, v in dict2.items()}
    #print("new_dict2:")
    #pprint(new_dict2)
    dict1.update(new_dict2)
    return dict1



def read_bytes(file, num_bytes):
    bytes = file.read(num_bytes)
    if not bytes:
        raise EOFError("End of file reached")
    return bytes


# Define constants
JPEG_MARKER_BYTE = 0xFF
JPEG_ZERO = 0x00

def read_jpeg_markers(file_path):
    markers = {}
    qtables = {}
    qtable_data_segments = []
    htable_data_segments = []

    try:
        with open(file_path, "rb") as file:
            offset = 0
            print("{:7} {:16} {:>8}  {}".format("Offset", "Marker", "Length", "Hash"))

            while True:
                try:

                    data = read_bytes(file, 2)
                    marker_code = struct.unpack(">H", data)[0]

                    # Skip if marker is not valid
                    if marker_code == (JPEG_MARKER_BYTE << 8 | JPEG_ZERO) or marker_code == (JPEG_MARKER_BYTE << 8 | JPEG_MARKER_BYTE):
                        continue

                    markers[offset] = jpeg_markers[marker_code]

                    if marker_code not in paramterless_jpeg_markers:

                        data += read_bytes(file, 2)
                        segment_length = struct.unpack(">H", data[-2:])[0]

                        data += read_bytes(file, segment_length - 2)
                        # discard marker bytes
                        data_segment = data[2:]

                        if marker_code == 0xFFDB:   #DTQ
                            table_ids = read_qtables(data_segment, qtables)
                            markers[offset] += "(" + ",".join(map(str, table_ids)) + ")"
                            qtable_data_segments.append(data_segment)
                        elif marker_code == 0xFFC4:     # DHT
                            table_ids = read_htables(data_segment)
                            markers[offset] += "(" + ".".join(table_ids) + ")"
                            htable_data_segments.append(data_segment)

                    else:
                        data_segment = b''
                        segment_length = 0
                        hash_string = ''

                    print(segment_string(offset, marker_code, data))
                    offset += len(data)

                    if marker_code in start_of_bitsream_markers:
                        (data, stream_markers) = read_image_data(file, marker_code)
                        #pprint(stream_markers)
                        #print("OFFSET: ", hex(offset))
                        #pprint(stream_markers)
                        markers = merge_dicts_add_val_to_keys(markers, stream_markers, offset)
                        #markers.update(stream_markers)
                        #print(segment_string(offset, None, data))
                        offset += len(data)

                except EOFError:
                    break


            #pprint(markers)
            print(np.array([markers[key] for key in sorted(markers)]))
            #pprint(qtables)
            qtables_linear = qdict_zigzag_to_linear(qtables)
            qtables_trans  = transpose_qtables(qtables_linear)

            #print("qtable data segments")
            #print(qtable_data_segments)

            trans_data_segs  = transpose_data_segments(qtable_data_segments)

            trans2_data_segs = transpose_data_segments(trans_data_segs)

            #print("prev     data:",  (qtable_data_segments[0].hex())) 
            #print("trans/new dat:",  (trans2_data_segs[0].hex()))
            #print("new      data:",  (trans_data_segs[0]).hex())

            #print("prev     data: ", (qtable_data_segments[1].hex())) 
            #print("trans/new dat:",  (trans2_data_segs[1].hex()))
            #print("new      data:",  (trans_data_segs[1]).hex())



            print("\n")

            print(f"independantly hashed qtables:\n{hash_matrices(qtables)}")

            #print("\n")
            print(f"\nAll qtables concatenated, then hashed:\n{concat_hash_qtables(qtables)}")


            et_hash_string = exiftool_hash_string(qtable_data_segments)
            print(f"\nexiftool_hash_string:\n{et_hash_string}")

            et_hash_string_r = exiftool_hash_string(trans_data_segs)
            print(f"\nexiftool_hash_string (rotated):\n{et_hash_string_r}")


            gp_hash_string = gimp_hash_string(qtables_linear)
            print(f"\ngimp_hash_string:\n{gp_hash_string}")

            gp_hash_string_r = gimp_hash_string(qtables_trans)
            print(f"\ngimp_hash_string (rotated):\n{gp_hash_string_r}")



            gd_hash_string = gdal_hash_string(qtable_data_segments)
            print(f"\ngdal_hash_string:\n{gd_hash_string}")

            gd_hash_string_r = gdal_hash_string(trans_data_segs)
            print(f"\ngdal_hash_string (rotated):\n{gd_hash_string_r}")



            js_hash_string = jpegsnoop_hash_string(qtables_linear)
            print(f"\njpegsnoop_hash_string:\n{js_hash_string}")

            js_hash_string_r = jpegsnoop_hash_string(qtables_trans)
            print(f"\njpegsnoop_hash_string (rotated):\n{js_hash_string_r}")



            #if gd_hash_string in gdal_sigs.sigs:
            #    print("matching gdal_sig:")
            #    pprint(gdal_sigs.sigs[gdal_hash_string])


            print("\nqtables_zigzag:\n")
            pprint(qtables)

            print("\nqtables_linear:\n")
            pprint(qtables_linear)

            print("\nqtables_transposed")
            pprint(transpose_qtables(qtables_linear))

            if et_hash_string in sigs_exiftool.sigs:
                print("\nmatching sigs_exiftool:")
                pprint(sigs_exiftool.sigs[et_hash_string])

            if js_hash_string in sigs_jpegsnoop.sigs:
                print("\nmatching sigs_jpegsnoop:")
                pprint(sigs_jpegsnoop.sigs[js_hash_string])

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
