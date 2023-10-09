#!/usr/bin/env python3

import argparse
import struct
import hashlib
from prettytable import PrettyTable
from pprint import pprint
import sigs_jpegsnoop
import sigs_exiftool
import sigs_gdal
import sigs_gimp


# fmt: off

# JPEG marker constants
M_STUF  = 0x00 # Stuffing, technically not a marker
M_PAD   = 0xFF # Padding, technically not a marker
M_TEM   = 0x01

# JPEG 2000
M_SOP   = 0x91; M_EPH   = 0x92; M_SOD   = 0x93

M_SOF0  = 0xc0; M_SOF1  = 0xc1; M_SOF2  = 0xc2; M_SOF3  = 0xc3
M_DHT   = 0xc4; M_SOF5  = 0xc5; M_SOF6  = 0xc6; M_SOF7  = 0xc7
M_JPG   = 0xc8; M_SOF9  = 0xc9; M_SOF10 = 0xca; M_SOF11 = 0xcb
M_DAC   = 0xcc; M_SOF13 = 0xcd; M_SOF14 = 0xce; M_SOF15 = 0xcf

M_RST0  = 0xd0; M_RST1  = 0xd1; M_RST2  = 0xd2; M_RST3  = 0xd3
M_RST4  = 0xd4; M_RST5  = 0xd5; M_RST6  = 0xd6; M_RST7  = 0xd7
M_SOI   = 0xd8; M_EOI   = 0xd9; M_SOS   = 0xda; M_DQT   = 0xdb
M_DNL   = 0xdc; M_DRI   = 0xdd; M_DHP   = 0xde; M_EXP   = 0xdf

M_APP0  = 0xe0; M_APP1  = 0xe1; M_APP2  = 0xe2; M_APP3  = 0xe3
M_APP4  = 0xe4; M_APP5  = 0xe5; M_APP6  = 0xe6; M_APP7  = 0xe7
M_APP8  = 0xe8; M_APP9  = 0xe9; M_APP10 = 0xea; M_APP11 = 0xeb
M_APP12 = 0xec; M_APP13 = 0xed; M_APP14 = 0xee; M_APP15 = 0xef

M_JPG0  = 0xf0
M_JPG13 = 0xfd; M_COM   = 0xfe

jpeg_markers = {
    # 01-0F
                      M_TEM:   "TEM",
                                        0x0A: "JXL",

    # 40-4F
                                                            0x4F: "SOC",

    # 50-5F
    0x50:    "CAP",   0x51:    "SIZ",   0x52:    "COD",     0x53:  "COC",
    0x54:    "NSI",   0x55:    "TLM",   0x56:    "PRF",     0x57:  "PLM",
    0x58:    "PLT",   0x59:    "CPF",   0x5A:    "QPD",     0x5B:  "QPC",
    0x5C:    "QCD",   0x5D:    "QCC",   0x5E:    "RGN",     0x5F:  "POC",

    # 60-6F
    # ILL is taken from the CREW patent, table 3
    # https://patents.google.com/patent/US20060233257A1
    0x60:    "PPM",   0x61:    "PPT",   0x62:    "ILL",     0x63:  "CRG",
    0x64:    "COM",   0x65:    "SEC",   0x66:    "EPB",     0x67:  "ESD",
    0x68:    "EPC",   0x69:    "RED",

    # 70-7F
    0x70:    "DCO",   0x71:    "VMS",   0x72:    "DFS",     0x73:  "ADS",
    0x74:    "MCT",   0x75:    "MCC",   0x76:    "NLT",     0x77:  "MCO",
    0x78:    "CBD",   0x79:    "ATK",

    # 90-9F
    0x90:    "SOT",   M_SOP:   "SOP",   M_EPH:   "EPH",   M_SOD:   "SOD",
    0x94:    "INSEC",

    # C0-CF
    M_SOF0:  "SOF0",  M_SOF1:  "SOF1",  M_SOF2:  "SOF2",  M_SOF3:  "SOF3",
    M_DHT:   "DHT",   M_SOF5:  "SOF5",  M_SOF6:  "SOF6",  M_SOF7:  "SOF7",
    M_JPG:   "JPG",   M_SOF9:  "SOF9",  M_SOF10: "SOF10", M_SOF11: "SOF11",
    M_DAC:   "DAC",   M_SOF13: "SOF13", M_SOF14: "SOF14", M_SOF15: "SOF15",

    # D0-DF
    M_RST0:  "RST0",  M_RST1:  "RST1",  M_RST2:  "RST2",  M_RST3:  "RST3",
    M_RST4:  "RST4",  M_RST5:  "RST5",  M_RST6:  "RST6",  M_RST7:  "RST7",
    M_SOI:   "SOI",   M_EOI:   "EOI",   M_SOS:   "SOS",   M_DQT:   "DQT",
    M_DNL:   "DNL",   M_DRI:   "DRI",   M_DHP:   "DHP",   M_EXP:   "EXP",

    # E0-EF
    M_APP0:  "APP0",  M_APP1:  "APP1",  M_APP2:  "APP2",  M_APP3:  "APP3",
    M_APP4:  "APP4",  M_APP5:  "APP5",  M_APP6:  "APP6",  M_APP7:  "APP7",
    M_APP8:  "APP8",  M_APP9:  "APP9",  M_APP10: "APP10", M_APP11: "APP11",
    M_APP12: "APP12", M_APP13: "APP13", M_APP14: "APP14", M_APP15: "APP15",

    # F0-FE
    M_JPG0:  "JPG0",  0xF1:    "DTI",   0xF2:    "DTT",   0xF3:    "SRF",
    0xF4:    "SRS",   0xF5:    "DCR",   0xF6:    "DQS",   0xF7:    "SOF55",
    0xF8:    "LSE",   0xF9:    "JPG9",  0xFA:    "JPG10", 0xFB:    "JPG11",
    0xFC:    "JPG12", 0xFD:    "JPG13", M_COM:   "COM",
}

paramterless_jpeg_markers = [
    M_TEM,   0x0A,                   # TEM, JXL

                               0x4F, # SOC

    0x30,    0x31,    0x32,    0x33, # RES (Reserved), guaranteed parameter less
    0x34,    0x35,    0x36,    0x37,
    0x38,    0x39,    0x3A,    0x3B,
    0x3C,    0x3D,    0x3E,    0x3F,

                      0x92,    M_SOD, # EPH, SOD

    M_RST0,  M_RST1,  M_RST2,  M_RST3,
    M_RST4,  M_RST5,  M_RST6,  M_RST7,
    M_SOI,   M_EOI,                  # SOI, EOI/EOC
]

valid_bitstream_markers = [
    M_PAD,
    0x90,                           # SOT
    M_RST0, M_RST1, M_RST2, M_RST3,
    M_RST4, M_RST5, M_RST6, M_RST7,
    M_SOI,  M_EOI,                  # SOI, EOI/EOC
]

start_of_bitsream_markers = [
    M_RST0, M_RST1, M_RST2, M_RST3,
    M_RST4, M_RST5, M_RST6, M_RST7,

    M_SOD,   M_SOS,                 # SOD, SOS
]

end_of_bitstream_markers = [
    M_EOI, 0x90                  # EOI/EOC, SOT
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
                marker_code = data[index + 1]
            except IndexError:
                break

            if bitstream_marker_code != M_SOD:  # not SOD, i.e. "plain" JPEG
                # padding or stuffing, and RST markers
                if (
                    marker_code == M_PAD # Padding
                    or marker_code == M_STUF # Stuffing
                    or M_RST0 <= marker_code <= M_RST7
                ):
                    #if M_RST0 <= marker_code <= M_RST7:
                    #    stream_markers[index] = jpeg_markers[marker_code]
                    search_offset = index + 2
                    continue
                else:  # SOS segment can contain any marker
                    data = data[:index]
                    # seek back to the first marker after bitstream data
                    file.seek(orig_fpos + index)
                    return (bytes(data), stream_markers) 
            else:  # SOD, JPEG 2000
                if marker_code == M_SOP or marker_code == M_EPH:  # SOP or EPH
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
    for arrays in sorted(qtables.values()):
        for array in arrays:
            concatenated_arrays.extend(array)

    concatenated_bytes = bytes(concatenated_arrays)
    hash_object = hashlib.md5(concatenated_bytes)
    return hash_object.hexdigest()



def segment_string(offset, marker_code, data):

    if marker_code:
        segment_len = len(data) - 2
        marker_name = jpeg_markers.get(marker_code, "RES")
        marker_name = f"{marker_name:5} (0xFF{marker_code:02X})  "
    else:
        segment_len = len(data)
        marker_code = ""
        marker_name = "[ECS]"
        marker_name = f"{marker_name:16}"

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
        [ 0,  1,  5,  6, 14, 15, 27, 28],
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
        [ 0,  1,  5,  6, 14, 15, 27, 28],
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


# Reimplementation of custom hash algo in GIMP source tree:
# plug-ins/file-jpeg/jpegqual.c 
def gimp_hash_string(qtables):
    hashval = 11
    for t in sorted(qtables.keys()):
        for row in qtables[t]:
            for val in row:
                # Simulate overflow of 32 bit unsigned integer
                hashval = (hashval * 4177 + val) & 0xFFFFFFFF

    return format(hashval, '08x')


# GDAL hashes all DQT segments in file order (including length bytes)
# Reimplementation of frmts/gtiff/generate_quant_table_md5sum.cpp
def gdal_hash_string(qtable_data_segments):
    #pprint([ ''.join(format(x, '02x') for x in byte_string) for byte_string in qtable_data_segments])

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

def adamp_qtable_string(qtable):
    return '!'.join([','.join(map(str, sublist)) for sublist in qtable])

def adamp_qtables(qtables):
    return ({k: adamp_qtable_string(v) for k, v in qtables.items()})

def adamp_hash_string(qtables):
    hash_string = ','.join(f"*DQT{k},{adamp_qtable_string(v)}" for k, v in qtables.items())
    hash_string = hash_string + "*END"
    print(hash_string)
    hash_string = hashlib.md5(hash_string.encode()).hexdigest()
    return hash_string


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


def read_htables(data_segment):

    # discard length bytes
    data = data_segment[2:]
    table_ids = [] # table ids
    while data:
        tbltype_and_id = data[0]
        tbltype = tbltype_and_id >> 4
        table_id = tbltype_and_id & 0x0F

        table_ids.append(str(table_id) + ":" + ["AC","DC"][tbltype])

        size_table          = data[1:17]

        symbol_table_length = sum(size_table)
        table_length        = 16 + symbol_table_length


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

        # Transpose the matrix
        transposed_matrix = transpose_matrix(matrix)

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

    return data_segment[:2] + new_data_segment


def merge_dicts_add_val_to_keys(dict1, dict2, add_value):
    #print("merge_dicts:", hex(add_value))

    new_dict2 = {k+add_value: v for k, v in dict2.items()}
    return dict2

def read_bytes(file, num_bytes):
    bytes = file.read(num_bytes)
    if not bytes:
        raise EOFError("End of file reached")
    return bytes

def get_jpegsnoop_description_string(js_data):
    category = js_data["eEditor"]

    if category == "ENUM_EDITOR_SW":
        return " ".join([js_data["strMSwDisp"], js_data["strUmQual"]])
    else:
        return " ".join([js_data["strXMake"], js_data["strUmQual"]])
                        

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
                    try:
                        marker_code = data[1]
                    except IndexError:
                        break   #End of file

                    # Skip if marker is not valid
                    if (data[0] != 0xff or marker_code == M_STUF or marker_code == M_PAD):
                        offset += 2
                        continue

                    markers[offset] = jpeg_markers[marker_code]

                    if marker_code not in paramterless_jpeg_markers:

                        data += read_bytes(file, 2)
                        segment_length = struct.unpack(">H", data[-2:])[0]

                        data += read_bytes(file, segment_length - 2)
                        # discard marker bytes
                        data_segment = data[2:]

                        if marker_code == M_DQT:   # DQT
                            table_ids = read_qtables(data_segment, qtables)
                            markers[offset] += "(" + ",".join(map(str, table_ids)) + ")"
                            qtable_data_segments.append(data_segment)
                        elif marker_code == M_DHT:     # DHT
                            table_ids = read_htables(data_segment)
                            markers[offset] += "(" + ",".join(table_ids) + ")"
                            htable_data_segments.append(data_segment)

                    else:
                        data_segment = b''
                        segment_length = 0

                    print(segment_string(offset, marker_code, data))
                    offset += len(data)

                    if marker_code in start_of_bitsream_markers:
                        (data, stream_markers) = read_image_data(file, marker_code)
                        stream_markers = merge_dicts_add_val_to_keys(markers, stream_markers, offset)
                        markers.update(stream_markers)
                        print(segment_string(offset, None, data))
                        offset += len(data)


                except EOFError:
                    break

            print("\nMarker sequence:")
            #print(np.array([markers[key] for key in sorted(markers)]))
            print([markers[key] for key in sorted(markers)])
            print("\n")


            qtables_linear = qdict_zigzag_to_linear(qtables)
            qtables_trans  = transpose_qtables(qtables_linear)

            #print("Adamp zigzag")
            #adamp_hash_string(qtables_linear)

            #print("Adamp linear")
            #adamp_hash_string(qtables_linear)


            match_tbl = PrettyTable()
            #match_tbl.field_names = ["Matching hash", "database", "Company", "Product", "QF", "Rotated"]

            trans_data_segs  = transpose_data_segments(qtable_data_segments)



            # Set field names and alignment for match table
            match_tbl.field_names = ["Matching hash", "database", "Description", "Rotated"]
            match_tbl.align = "l"
            match_tbl.sortby = "Description"


            et_hash_string = exiftool_hash_string(qtable_data_segments)
            et_hash_string_r = exiftool_hash_string(trans_data_segs)
            # If et_hash_string is in signatures
            if et_hash_string in sigs_exiftool.sigs:
                for hmatches in sigs_exiftool.sigs[et_hash_string]:
                    tbl_row = [et_hash_string, "Exiftool"]
                    tbl_row.append(hmatches["description"])
                    if "description" in hmatches:
                        tbl_row.append("Symmetrical" if et_hash_string == et_hash_string_r else "")
                        match_tbl.add_row(tbl_row)

            # If et_hash_string_r is in signatures
            elif et_hash_string_r in sigs_exiftool.sigs:
                for hmatches in sigs_exiftool.sigs[et_hash_string_r]:
                    tbl_row = [et_hash_string, "Exiftool"]
                    tbl_row.append(hmatches["description"])
                    print("match2")

                    if "description" in hmatches:
                        tbl_row.append("Symmetrical" if et_hash_string == et_hash_string_r else "Rotated")
                        print("tbl_row (rot):", tbl_row)
                        match_tbl.add_row(tbl_row)


            gd_hash_string = gdal_hash_string(qtable_data_segments)
            gd_hash_string_r = gdal_hash_string(trans_data_segs)

            # Check if GDAL hash strings are in signatures

            # If gdal_hash_string is in signatures
            if gd_hash_string in sigs_gdal.sigs:
                for hmatches in sigs_gdal.sigs[gd_hash_string]:
                    tbl_row = [gd_hash_string, "GDAL"]
                    tbl_row.append(hmatches)
                    tbl_row.append("Symmetrical" if et_hash_string == et_hash_string_r else "")
                    match_tbl.add_row(tbl_row)

            # If gd_hash_string_r is in signatures
            elif gd_hash_string_r in sigs_gdal.sigs:
                for hmatches in sigs_gdal.sigs[gd_hash_string_r]:
                    tbl_row = [gd_hash_string, "GDAL"]
                    tbl_row.append(hmatches)
                    tbl_row.append("Symmetrical" if et_hash_string == et_hash_string_r else "Rotated")
                    match_tbl.add_row(tbl_row)

            js_hash_string = jpegsnoop_hash_string(qtables_linear)
            js_hash_string_r = jpegsnoop_hash_string(qtables_trans)


            # Check if JPEGsnoop hash strings are in signatures
            # If js_hash_string is in signatures
            if js_hash_string in sigs_jpegsnoop.sigs:
                for hmatches in sigs_jpegsnoop.sigs[js_hash_string]:
                    tbl_row = [js_hash_string, "JPEGSnoop"]
                    tbl_row.append(get_jpegsnoop_description_string(hmatches))
                    tbl_row.append("Symmetrical" if js_hash_string == js_hash_string_r else "")
                    match_tbl.add_row(tbl_row)

            # If js_hash_string_r is in signatures
            elif js_hash_string_r in sigs_jpegsnoop.sigs:
                for hmatches in sigs_jpegsnoop.sigs[js_hash_string_r]:
                    print("js_hash_string_r: ", js_hash_string_r)
                    tbl_row = [js_hash_string, "JPEGSnoop"]
                    tbl_row.append(get_jpegsnoop_description_string(hmatches))
                    tbl_row.append("Symmetrical" if js_hash_string == js_hash_string_r else "Rotated")
                    match_tbl.add_row(tbl_row)


            gp_hash_string = gimp_hash_string(qtables_linear)
            gp_hash_string_r = gimp_hash_string(qtables_trans)

            
            # Check if GIMP hash strings are in signatures
            # If gp_hash_string is in signatures
            if gp_hash_string in sigs_gimp.sigs:
                for hmatches in sigs_gimp.sigs[gp_hash_string]:
                    tbl_row = [gp_hash_string, "GIMP"]
                    tbl_row.append(" ".join([hmatches["source_name"], hmatches["setting_name"]]))
                    tbl_row.append("Symmetrical" if gp_hash_string == gp_hash_string_r else "")
                    match_tbl.add_row(tbl_row)
            
                    
            # If gp_hash_string_r is in signatures
            elif gp_hash_string_r in sigs_gimp.sigs:
                for hmatches in sigs_gimp.sigs[gp_hash_string_r]:
                    print("gp_hash_string_r: ", gp_hash_string_r)
                    tbl_row = [gp_hash_string, "JPEGSnoop"]
                    tbl_row.append(" ".join([hmatches["source_name"], hmatches["setting_name"]]))
                    tbl_row.append("Symmetrical" if gp_hash_string == gp_hash_string_r else "Rotated")
                    match_tbl.add_row(tbl_row)


            print(match_tbl)

            '''
            print("\n")

            print(f"independantly hashed qtables (zigzag):\n{hash_matrices(qtables)}")
            print(f"independantly hashed qtables (linear):\n{hash_matrices(qtables_linear)}")

            print("\n")
            print(f"\nAll qtables concatenated, then hashed (zigzag):\n{concat_hash_qtables(qtables)}")
            print(f"\nAll qtables concatenated, then hashed (linear):\n{concat_hash_qtables(qtables_linear)}")
            '''
            
            '''
            if et_hash_string in sigs_exiftool.sigs:
                print("\nmatching_sigs_exiftool:")
                pprint(sigs_exiftool.sigs[et_hash_string])

            if et_hash_string_r in sigs_exiftool.sigs:
                print("\nmatching_sigs_exiftool_(rotated):")
                pprint(sigs_exiftool.sigs[et_hash_string_r])

            if gd_hash_string in sigs_gdal.sigs:
                print("\nmatching_sigs_gdal:")
                pprint(sigs_gdal.sigs[gd_hash_string])

            if gd_hash_string_r in sigs_gdal.sigs:
                print("\nmatching_sigs_gdal_(rotated):")
                pprint(sigs_gdal.sigs[gd_hash_string_r])

            if gp_hash_string in sigs_gimp.sigs:
                print("\nmatching_sigs_gimp:")
                pprint(sigs_gimp.sigs[gp_hash_string])

            if gp_hash_string_r in sigs_gimp.sigs:
                print("\nmatching_sigs_gimp_(rotated):")
                pprint(sigs_gimp.sigs[gp_hash_string_r])

            if js_hash_string in sigs_jpegsnoop.sigs:
                print("\nmatching_sigs_jpegsnoop:")
                pprint(sigs_jpegsnoop.sigs[js_hash_string])

            if js_hash_string_r in sigs_jpegsnoop.sigs:
                print("\nmatching_sigs_jpegsnoop_(rotated):")
                pprint(sigs_jpegsnoop.sigs[js_hash_string_r])
            '''

            '''
            et_hash_string = exiftool_hash_string(qtable_data_segments)
            print(f"\nexiftool_hash_string: {et_hash_string}")

            et_hash_string_r = exiftool_hash_string(trans_data_segs)
            print(f"\nexiftool_hash_string (rotated): {et_hash_string_r}")

            gp_hash_string = gimp_hash_string(qtables_linear)
            print(f"\ngimp_hash_string: {gp_hash_string}")

            gp_hash_string_r = gimp_hash_string(qtables_trans)
            print(f"\ngimp_hash_string (rotated): {gp_hash_string_r}")

            gd_hash_string = gdal_hash_string(qtable_data_segments)
            print(f"\ngdal_hash_string: {gd_hash_string}")

            gd_hash_string_r = gdal_hash_string(trans_data_segs)
            print(f"\ngdal_hash_string (rotated): {gd_hash_string_r}")

            js_hash_string = jpegsnoop_hash_string(qtables_linear)
            print(f"\njpegsnoop_hash_string: {js_hash_string}")

            js_hash_string_r = jpegsnoop_hash_string(qtables_trans)
            print(f"\njpegsnoop_hash_string (rotated): {js_hash_string_r}")
            '''
            
            
            #print("\nqtables_zigzag:\n")
            #pprint(qtables)

            qtables_linear = dict(sorted(qtables_linear.items()))

            print("qtables in adamp format")
            pprint(adamp_qtables(qtables_linear))

            print("\nqtables_linear:\n")
            pprint(qtables_linear)

            #print("\nqtables_transposed")
            #pprint(transpose_qtables(qtables_linear))
            



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
