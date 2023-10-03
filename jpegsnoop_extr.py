import re
import sys
from pprint import pprint

def extract_data():
    column_names = ['eEditor', 'strXMake', 'strXModel', 'strUmQual', 'strCSig', 'strCSigRot', 'strXSubsamp', 'strMSwTrim', 'strMSwDisp']
    data = {}

    for line in sys.stdin:
        # Check if line contains an MD5 hash
        if re.search(r'[a-fA-F0-9]{32}', line):
            # Extract the first constant and all "_T" strings
            constants = re.findall(r'\b[A-Z_]+\b', line)
            _T_strings = re.findall(r'_T\("([^"]*)"\)', line)

            # Check if there are enough "_T" strings
            if len(_T_strings) >= len(column_names) - 1:
                # Create a dictionary for this line
                line_data = {column_names[0]: constants[0]}
                for i in range(1, len(column_names)):
                    if column_names[i] == 'strCSig' or column_names[i] == 'strCSigRot':
                        line_data[column_names[i]] = _T_strings[i-1].lower()
                    else:
                        line_data[column_names[i]] = _T_strings[i-1]

                # Add the line data to the main data dictionary using strCSig as key
                strCSig = _T_strings[column_names.index('strCSig')-1].lower()
                if re.match(r'[a-f0-9]{32}', strCSig):
                    line_data_csig = line_data.copy()
                    line_data_csig.pop('strCSig', None)
                    if strCSig in data:
                        data[strCSig].append(line_data_csig)
                    else:
                        data[strCSig] = [line_data_csig]

                # Add the line data to the main data dictionary using strCSigRot as key
                strCSigRot = _T_strings[column_names.index('strCSigRot')-1].lower()
                if re.match(r'[a-f0-9]{32}', strCSigRot):
                    line_data_rot = line_data.copy()
                    line_data_rot.pop('strCSigRot', None)
                    if strCSigRot in data:
                        data[strCSigRot].append(line_data_rot)
                    else:
                        data[strCSigRot] = [line_data_rot]

    return data

# Use the function
pprint(extract_data())

#data = extract_data()
#print("len: ", len(data))
#pprint(data['01BBB1709AC9C1F89220D955A31A8F34'.lower()])
#for key in data.keys():
#    print(key)
