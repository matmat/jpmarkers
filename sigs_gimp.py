'''
/* 
 *
 * Copyright (C) 2023 Mattias Iko Mattsson <vitplister@gmail.com>
 * Copyright (C) 2007 Raphaël Quinet <raphael@gimp.org>
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <https://www.gnu.org/licenses/>.
 */


This file is extracted from GIMP https://github.com/GNOME/gimp/

    plug-ins/file-jpeg/jpegqual.c
'''


sigs = {
    "0a82648b": [
        {
            "lum_sum": 64,
            "chrom_sum": 64,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 100",
            "ijg_qual": 100,
        }
    ],
    "4d981764": [
        {
            "lum_sum": 86,
            "chrom_sum": 115,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 99",
            "ijg_qual": 99,
        }
    ],
    "62b71702": [
        {
            "lum_sum": 151,
            "chrom_sum": 224,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 98",
            "ijg_qual": 98,
        }
    ],
    "29e095c5": [
        {
            "lum_sum": 221,
            "chrom_sum": 333,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 97",
            "ijg_qual": 97,
        }
    ],
    "b62c754a": [
        {
            "lum_sum": 292,
            "chrom_sum": 443,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 96",
            "ijg_qual": 96,
        }
    ],
    "8e55c78a": [
        {
            "lum_sum": 369,
            "chrom_sum": 558,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 95",
            "ijg_qual": 95,
        }
    ],
    "0664d770": [
        {
            "lum_sum": 441,
            "chrom_sum": 668,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 94",
            "ijg_qual": 94,
        }
    ],
    "59e5c5bc": [
        {
            "lum_sum": 518,
            "chrom_sum": 779,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 93",
            "ijg_qual": 93,
        }
    ],
    "d6f26606": [
        {
            "lum_sum": 592,
            "chrom_sum": 891,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 92",
            "ijg_qual": 92,
        }
    ],
    "8aa986ad": [
        {
            "lum_sum": 667,
            "chrom_sum": 999,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 91",
            "ijg_qual": 91,
        }
    ],
    "17816eb1": [
        {
            "lum_sum": 736,
            "chrom_sum": 1110,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 90",
            "ijg_qual": 90,
        }
    ],
    "75de9350": [
        {
            "lum_sum": 814,
            "chrom_sum": 1223,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 89",
            "ijg_qual": 89,
        }
    ],
    "88fdf223": [
        {
            "lum_sum": 884,
            "chrom_sum": 1332,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 88",
            "ijg_qual": 88,
        }
    ],
    "f40a6a50": [
        {
            "lum_sum": 961,
            "chrom_sum": 1444,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 87",
            "ijg_qual": 87,
        }
    ],
    "e9f2c235": [
        {
            "lum_sum": 1031,
            "chrom_sum": 1555,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 86",
            "ijg_qual": 86,
        }
    ],
    "82683892": [
        {
            "lum_sum": 1109,
            "chrom_sum": 1666,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 85",
            "ijg_qual": 85,
        }
    ],
    "b1aecce8": [
        {
            "lum_sum": 1179,
            "chrom_sum": 1778,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 84",
            "ijg_qual": 84,
        }
    ],
    "83375efe": [
        {
            "lum_sum": 1251,
            "chrom_sum": 1888,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 83",
            "ijg_qual": 83,
        }
    ],
    "1e99f479": [
        {
            "lum_sum": 1326,
            "chrom_sum": 2000,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 82",
            "ijg_qual": 82,
        }
    ],
    "1a02d360": [
        {
            "lum_sum": 1398,
            "chrom_sum": 2111,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 81",
            "ijg_qual": 81,
        }
    ],
    "96129a0d": [
        {
            "lum_sum": 1477,
            "chrom_sum": 2221,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 80",
            "ijg_qual": 80,
        }
    ],
    "64d4144b": [
        {
            "lum_sum": 1552,
            "chrom_sum": 2336,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 79",
            "ijg_qual": 79,
        }
    ],
    "48a344ac": [
        {
            "lum_sum": 1620,
            "chrom_sum": 2445,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 78",
            "ijg_qual": 78,
        }
    ],
    "16e820e3": [
        {
            "lum_sum": 1692,
            "chrom_sum": 2556,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 77",
            "ijg_qual": 77,
        }
    ],
    "246b2e95": [
        {
            "lum_sum": 1773,
            "chrom_sum": 2669,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 76",
            "ijg_qual": 76,
        }
    ],
    "10b035e9": [
        {
            "lum_sum": 1858,
            "chrom_sum": 2780,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 75",
            "ijg_qual": 75,
        },
        {
            "lum_sum": 1858,
            "chrom_sum": 2780,
            "subsmp_h": 2,
            "subsmp_v": 2,
            "num_quant_tables": 2,
            "source_name": "Microsoft Office",
            "setting_name": "Default",
            "ijg_qual": 75,
        },
    ],
    "d5c653da": [
        {
            "lum_sum": 1915,
            "chrom_sum": 2836,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 74",
            "ijg_qual": 74,
        }
    ],
    "e349618c": [
        {
            "lum_sum": 1996,
            "chrom_sum": 2949,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 73",
            "ijg_qual": 73,
        }
    ],
    "b18e3dc3": [
        {
            "lum_sum": 2068,
            "chrom_sum": 3060,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 72",
            "ijg_qual": 72,
        }
    ],
    "955d6e24": [
        {
            "lum_sum": 2136,
            "chrom_sum": 3169,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 71",
            "ijg_qual": 71,
        }
    ],
    "641ee862": [
        {
            "lum_sum": 2211,
            "chrom_sum": 3284,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 70",
            "ijg_qual": 70,
        }
    ],
    "e02eaf0f": [
        {
            "lum_sum": 2290,
            "chrom_sum": 3394,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 69",
            "ijg_qual": 69,
        }
    ],
    "db978df6": [
        {
            "lum_sum": 2362,
            "chrom_sum": 3505,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 68",
            "ijg_qual": 68,
        }
    ],
    "76fa2371": [
        {
            "lum_sum": 2437,
            "chrom_sum": 3617,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 67",
            "ijg_qual": 67,
        }
    ],
    "4882b587": [
        {
            "lum_sum": 2509,
            "chrom_sum": 3727,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 66",
            "ijg_qual": 66,
        }
    ],
    "25556ae1": [
        {
            "lum_sum": 2583,
            "chrom_sum": 3839,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 65",
            "ijg_qual": 65,
        }
    ],
    "103ec03a": [
        {
            "lum_sum": 2657,
            "chrom_sum": 3950,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 64",
            "ijg_qual": 64,
        }
    ],
    "0627181f": [
        {
            "lum_sum": 2727,
            "chrom_sum": 4061,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 63",
            "ijg_qual": 63,
        }
    ],
    "7133904c": [
        {
            "lum_sum": 2804,
            "chrom_sum": 4173,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 62",
            "ijg_qual": 62,
        }
    ],
    "8452ef1f": [
        {
            "lum_sum": 2874,
            "chrom_sum": 4282,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 61",
            "ijg_qual": 61,
        }
    ],
    "e2b013be": [
        {
            "lum_sum": 2952,
            "chrom_sum": 4395,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 60",
            "ijg_qual": 60,
        }
    ],
    "6f87fbc2": [
        {
            "lum_sum": 3021,
            "chrom_sum": 4506,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 59",
            "ijg_qual": 59,
        }
    ],
    "233f1c69": [
        {
            "lum_sum": 3096,
            "chrom_sum": 4614,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 58",
            "ijg_qual": 58,
        }
    ],
    "a04bbcb3": [
        {
            "lum_sum": 3170,
            "chrom_sum": 4726,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 57",
            "ijg_qual": 57,
        }
    ],
    "f3ccaaff": [
        {
            "lum_sum": 3247,
            "chrom_sum": 4837,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 56",
            "ijg_qual": 56,
        }
    ],
    "1967dbe9": [
        {
            "lum_sum": 3323,
            "chrom_sum": 4947,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 55",
            "ijg_qual": 55,
        }
    ],
    "44050d25": [
        {
            "lum_sum": 3396,
            "chrom_sum": 5062,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 54",
            "ijg_qual": 54,
        }
    ],
    "d050ecaa": [
        {
            "lum_sum": 3467,
            "chrom_sum": 5172,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 53",
            "ijg_qual": 53,
        }
    ],
    "9e99f8f1": [
        {
            "lum_sum": 3541,
            "chrom_sum": 5281,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 52",
            "ijg_qual": 52,
        }
    ],
    "df2423f4": [
        {
            "lum_sum": 3621,
            "chrom_sum": 5396,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 51",
            "ijg_qual": 51,
        }
    ],
    "e0f48a64": [
        {
            "lum_sum": 3688,
            "chrom_sum": 5505,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 50",
            "ijg_qual": 50,
        }
    ],
    "e2c4f0d4": [
        {
            "lum_sum": 3755,
            "chrom_sum": 5614,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 49",
            "ijg_qual": 49,
        }
    ],
    "234f1bd7": [
        {
            "lum_sum": 3835,
            "chrom_sum": 5729,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 48",
            "ijg_qual": 48,
        }
    ],
    "f198281e": [
        {
            "lum_sum": 3909,
            "chrom_sum": 5838,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 47",
            "ijg_qual": 47,
        }
    ],
    "7de407a3": [
        {
            "lum_sum": 3980,
            "chrom_sum": 5948,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 46",
            "ijg_qual": 46,
        }
    ],
    "b3aa597b": [
        {
            "lum_sum": 4092,
            "chrom_sum": 6116,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 45",
            "ijg_qual": 45,
        }
    ],
    "32b48093": [
        {
            "lum_sum": 4166,
            "chrom_sum": 6226,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 44",
            "ijg_qual": 44,
        }
    ],
    "9ea9f85f": [
        {
            "lum_sum": 4280,
            "chrom_sum": 6396,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 43",
            "ijg_qual": 43,
        }
    ],
    "335d6006": [
        {
            "lum_sum": 4393,
            "chrom_sum": 6562,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 42",
            "ijg_qual": 42,
        }
    ],
    "a727ea4a": [
        {
            "lum_sum": 4463,
            "chrom_sum": 6672,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 41",
            "ijg_qual": 41,
        }
    ],
    "1889cfc4": [
        {
            "lum_sum": 4616,
            "chrom_sum": 6897,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 40",
            "ijg_qual": 40,
        }
    ],
    "b1aa548e": [
        {
            "lum_sum": 4719,
            "chrom_sum": 7060,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 39",
            "ijg_qual": 39,
        }
    ],
    "99bebdd3": [
        {
            "lum_sum": 4829,
            "chrom_sum": 7227,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 38",
            "ijg_qual": 38,
        }
    ],
    "f728d062": [
        {
            "lum_sum": 4976,
            "chrom_sum": 7447,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 37",
            "ijg_qual": 37,
        }
    ],
    "e1ba65b9": [
        {
            "lum_sum": 5086,
            "chrom_sum": 7616,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 36",
            "ijg_qual": 36,
        }
    ],
    "2c8ba6a4": [
        {
            "lum_sum": 5240,
            "chrom_sum": 7841,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 35",
            "ijg_qual": 35,
        }
    ],
    "03f7963a": [
        {
            "lum_sum": 5421,
            "chrom_sum": 8114,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 34",
            "ijg_qual": 34,
        }
    ],
    "a19bed1e": [
        {
            "lum_sum": 5571,
            "chrom_sum": 8288,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 33",
            "ijg_qual": 33,
        }
    ],
    "7945d01c": [
        {
            "lum_sum": 5756,
            "chrom_sum": 8565,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 32",
            "ijg_qual": 32,
        }
    ],
    "cc36df1a": [
        {
            "lum_sum": 5939,
            "chrom_sum": 8844,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 31",
            "ijg_qual": 31,
        }
    ],
    "3eb1b5ca": [
        {
            "lum_sum": 6125,
            "chrom_sum": 9122,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 30",
            "ijg_qual": 30,
        }
    ],
    "d7f65293": [
        {
            "lum_sum": 6345,
            "chrom_sum": 9455,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 29",
            "ijg_qual": 29,
        }
    ],
    "4c0a8178": [
        {
            "lum_sum": 6562,
            "chrom_sum": 9787,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 28",
            "ijg_qual": 28,
        }
    ],
    "8281d1a1": [
        {
            "lum_sum": 6823,
            "chrom_sum": 10175,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 27",
            "ijg_qual": 27,
        }
    ],
    "0bbc9f7e": [
        {
            "lum_sum": 7084,
            "chrom_sum": 10567,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 26",
            "ijg_qual": 26,
        }
    ],
    "a8ac1cbd": [
        {
            "lum_sum": 7376,
            "chrom_sum": 11010,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 25",
            "ijg_qual": 25,
        }
    ],
    "459b99fc": [
        {
            "lum_sum": 7668,
            "chrom_sum": 11453,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 24",
            "ijg_qual": 24,
        }
    ],
    "da09c178": [
        {
            "lum_sum": 7995,
            "chrom_sum": 11954,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 23",
            "ijg_qual": 23,
        }
    ],
    "1c651f15": [
        {
            "lum_sum": 8331,
            "chrom_sum": 12511,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 22",
            "ijg_qual": 22,
        }
    ],
    "59025244": [
        {
            "lum_sum": 8680,
            "chrom_sum": 13121,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 21",
            "ijg_qual": 21,
        }
    ],
    "a130f919": [
        {
            "lum_sum": 9056,
            "chrom_sum": 13790,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 20",
            "ijg_qual": 20,
        }
    ],
    "109756cf": [
        {
            "lum_sum": 9368,
            "chrom_sum": 14204,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 19",
            "ijg_qual": 19,
        }
    ],
    "e929cab5": [
        {
            "lum_sum": 9679,
            "chrom_sum": 14267,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 18",
            "ijg_qual": 18,
        }
    ],
    "cddca370": [
        {
            "lum_sum": 10027,
            "chrom_sum": 14346,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 17",
            "ijg_qual": 17,
        }
    ],
    "d5fc76c0": [
        {
            "lum_sum": 10360,
            "chrom_sum": 14429,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 16",
            "ijg_qual": 16,
        }
    ],
    "533a1a03": [
        {
            "lum_sum": 10714,
            "chrom_sum": 14526,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 15",
            "ijg_qual": 15,
        }
    ],
    "0d8adaff": [
        {
            "lum_sum": 11081,
            "chrom_sum": 14635,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 14",
            "ijg_qual": 14,
        }
    ],
    "0d2ee95d": [
        {
            "lum_sum": 11456,
            "chrom_sum": 14754,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 13",
            "ijg_qual": 13,
        }
    ],
    "3a1d59a0": [
        {
            "lum_sum": 11861,
            "chrom_sum": 14864,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 12",
            "ijg_qual": 12,
        }
    ],
    "66555d04": [
        {
            "lum_sum": 12240,
            "chrom_sum": 14985,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 11",
            "ijg_qual": 11,
        }
    ],
    "7fa051b1": [
        {
            "lum_sum": 12560,
            "chrom_sum": 15110,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 10",
            "ijg_qual": 10,
        }
    ],
    "7b668ca3": [
        {
            "lum_sum": 12859,
            "chrom_sum": 15245,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 9",
            "ijg_qual": 9,
        }
    ],
    "b44d7082": [
        {
            "lum_sum": 13230,
            "chrom_sum": 15369,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 8",
            "ijg_qual": 8,
        }
    ],
    "e838d325": [
        {
            "lum_sum": 13623,
            "chrom_sum": 15523,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 7",
            "ijg_qual": 7,
        }
    ],
    "b6f58977": [
        {
            "lum_sum": 14073,
            "chrom_sum": 15731,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 6",
            "ijg_qual": 6,
        }
    ],
    "fd3e9fc4": [
        {
            "lum_sum": 14655,
            "chrom_sum": 16010,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 5",
            "ijg_qual": 5,
        }
    ],
    "7782b922": [
        {
            "lum_sum": 15277,
            "chrom_sum": 16218,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 4",
            "ijg_qual": 4,
        }
    ],
    "5a03ac45": [
        {
            "lum_sum": 15946,
            "chrom_sum": 16320,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 3",
            "ijg_qual": 3,
        }
    ],
    "e0afaa36": [
        {
            "lum_sum": 16315,
            "chrom_sum": 16320,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 2",
            "ijg_qual": 2,
        }
    ],
    "6d640b8b": [
        {
            "lum_sum": 16320,
            "chrom_sum": 16320,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 1",
            "ijg_qual": 1,
        },
        {
            "lum_sum": 16320,
            "chrom_sum": 16320,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "quality 0",
            "ijg_qual": 1,
        },
    ],
    "675ecd7a": [
        {
            "lum_sum": 13166,
            "chrom_sum": 19633,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "not baseline 14",
            "ijg_qual": 0,
        }
    ],
    "7a65d374": [
        {
            "lum_sum": 14160,
            "chrom_sum": 21129,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "not baseline 13",
            "ijg_qual": 0,
        }
    ],
    "f5d0af6a": [
        {
            "lum_sum": 15344,
            "chrom_sum": 22911,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "not baseline 12",
            "ijg_qual": 0,
        }
    ],
    "0227aaf0": [
        {
            "lum_sum": 16748,
            "chrom_sum": 24969,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "not baseline 11",
            "ijg_qual": 0,
        }
    ],
    "ffd2d3c8": [
        {
            "lum_sum": 18440,
            "chrom_sum": 27525,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "not baseline 10",
            "ijg_qual": 0,
        }
    ],
    "27f48623": [
        {
            "lum_sum": 20471,
            "chrom_sum": 30529,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "not baseline 9",
            "ijg_qual": 0,
        }
    ],
    "ff1fab81": [
        {
            "lum_sum": 23056,
            "chrom_sum": 34422,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "not baseline 8",
            "ijg_qual": 0,
        }
    ],
    "cfeac62b": [
        {
            "lum_sum": 26334,
            "chrom_sum": 39314,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "not baseline 7",
            "ijg_qual": 0,
        }
    ],
    "4a8e947e": [
        {
            "lum_sum": 30719,
            "chrom_sum": 45876,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "not baseline 6",
            "ijg_qual": 0,
        }
    ],
    "e668af85": [
        {
            "lum_sum": 36880,
            "chrom_sum": 55050,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "not baseline 5",
            "ijg_qual": 0,
        }
    ],
    "6d4b1215": [
        {
            "lum_sum": 46114,
            "chrom_sum": 68840,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "not baseline 4",
            "ijg_qual": 0,
        }
    ],
    "f2734901": [
        {
            "lum_sum": 61445,
            "chrom_sum": 91697,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "not baseline 3",
            "ijg_qual": 0,
        }
    ],
    "9a2a42bc": [
        {
            "lum_sum": 92200,
            "chrom_sum": 137625,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "not baseline 2",
            "ijg_qual": 0,
        }
    ],
    "1b178d6d": [
        {
            "lum_sum": 184400,
            "chrom_sum": 275250,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "not baseline 1",
            "ijg_qual": 0,
        },
        {
            "lum_sum": 184400,
            "chrom_sum": 275250,
            "subsmp_h": 0,
            "subsmp_v": 0,
            "num_quant_tables": 2,
            "source_name": "IJG JPEG Library",
            "setting_name": "not baseline 0",
            "ijg_qual": 0,
        },
    ],
    "3841f91b": [
        {
            "lum_sum": 736,
            "chrom_sum": 0,
            "subsmp_h": 1,
            "subsmp_v": 1,
            "num_quant_tables": 1,
            "source_name": "Kodak Imaging",
            "setting_name": "High (grayscale)",
            "ijg_qual": 90,
        }
    ],
    "9ebccf53": [
        {
            "lum_sum": 3688,
            "chrom_sum": 0,
            "subsmp_h": 1,
            "subsmp_v": 1,
            "num_quant_tables": 1,
            "source_name": "Kodak Imaging",
            "setting_name": "Medium (grayscale)",
            "ijg_qual": 50,
        }
    ],
    "34216b8b": [
        {
            "lum_sum": 9056,
            "chrom_sum": 0,
            "subsmp_h": 1,
            "subsmp_v": 1,
            "num_quant_tables": 1,
            "source_name": "Kodak Imaging",
            "setting_name": "Low (grayscale)",
            "ijg_qual": 20,
        }
    ],
}
