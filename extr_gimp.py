'''
Crude script to import hashes from GIMP's plug-ins/file-jpeg/jpegqual.c and
output a python dics
'''

import re
import sys

def parse_input():
    sigs = {}
    for line in sys.stdin:
        match = re.search(r'\{ 0x([0-9a-f]{8}), +(\d+), +(\d+), +(\d+), +(\d+), +(\d+), +"(.*?)", +"(.*?)", +(\d+) \}', line)
        if match:
            hash_key = match.group(1)
            lum_sum = int(match.group(2))
            chrom_sum = int(match.group(3))
            subsmp_h = int(match.group(4))
            subsmp_v = int(match.group(5))
            num_quant_tables = int(match.group(6))
            source_name = match.group(7)
            setting_name = match.group(8)
            ijg_qual = int(match.group(9))

            if hash_key not in sigs:
                sigs[hash_key] = []

            sigs[hash_key].append({
                'lum_sum': lum_sum,
                'chrom_sum': chrom_sum,
                'subsmp_h': subsmp_h,
                'subsmp_v': subsmp_v,
                'num_quant_tables': num_quant_tables,
                'source_name': source_name,
                'setting_name': setting_name,
                'ijg_qual': ijg_qual
            })
    return sigs

sigs = parse_input()

print('sigs = ' + repr(sigs))
