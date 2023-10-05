'''
 ******************************************************************************
 * Copyright (c) 2023, Mattias Iko Mattsson <vitplister at gmail dot com>
 * Copyright (c) 2021, Even Rouault <even dot rouault at spatialys dot com>
 *
 * Permission is hereby granted, free of charge, to any person obtaining a
 * copy of this software and associated documentation files (the "Software"),
 * to deal in the Software without restriction, including without limitation
 * the rights to use, copy, modify, merge, publish, distribute, sublicense,
 * and/or sell copies of the Software, and to permit persons to whom the
 * Software is furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included
 * in all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
 * OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
 * THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 * FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
 * DEALINGS IN THE SOFTWARE.
 ****************************************************************************/


This file is (semi-manually) extracted from the GDAL source tree at
https://github.com/OSGeo/gdal

    frmts/gtiff/quant_table_md5sum.h
    frmts/gtiff/quant_table_md5sum_jpeg9e.h
'''

sig = {
    "f930bb47fbde76e39674631183055eb6": ["md5JPEGQuantTable_generic_8bit: quality 1"],
    "db392ef56b4cb61fec0b8d41dd654cf6": ["md5JPEGQuantTable_generic_8bit: quality 2"],
    "6a4dfa4fd424295f5add625fd8a7a5e1": ["md5JPEGQuantTable_generic_8bit: quality 3"],
    "5c0060c7984059c575dc10c968ee88e6": ["md5JPEGQuantTable_generic_8bit: quality 4"],
    "5bfe2d8749df483005750fa078af4956": ["md5JPEGQuantTable_generic_8bit: quality 5"],
    "f12a423d3c6b8a0132cfb837039a5dee": ["md5JPEGQuantTable_generic_8bit: quality 6"],
    "f4206548578f7bf1d5dd778392042e1c": ["md5JPEGQuantTable_generic_8bit: quality 7"],
    "08618554810c1fbb2e5f65b8de7bae96": ["md5JPEGQuantTable_generic_8bit: quality 8"],
    "a20752f9fb7771090e30bd42642d0afe": ["md5JPEGQuantTable_generic_8bit: quality 9"],
    "2fa43e7b25484fc1deaa8269ec614822": ["md5JPEGQuantTable_generic_8bit: quality 10"],
    "34074313cd2502548f5e895cf21eeaa1": ["md5JPEGQuantTable_generic_8bit: quality 11"],
    "48aae191ae65aa144381f559ab59a8e7": ["md5JPEGQuantTable_generic_8bit: quality 12"],
    "f1b4205ae59af1720722941bfe07e145": ["md5JPEGQuantTable_generic_8bit: quality 13"],
    "c31807aac1dc780fff7b0287c705aae6": ["md5JPEGQuantTable_generic_8bit: quality 14"],
    "c5afb9bfd065aa6235fba2b529efc6e7": ["md5JPEGQuantTable_generic_8bit: quality 15"],
    "93add44a3c75633b9de9c736c60622a1": ["md5JPEGQuantTable_generic_8bit: quality 16"],
    "4c9865dd5635f19d1a8b326e089e6333": ["md5JPEGQuantTable_generic_8bit: quality 17"],
    "f9d472d498f9200654e563e124ca4af4": ["md5JPEGQuantTable_generic_8bit: quality 18"],
    "9dbac7033abe5768029816793c2ad7aa": ["md5JPEGQuantTable_generic_8bit: quality 19"],
    "8a810cc0b5b886a14bd3e6e305cc78fa": ["md5JPEGQuantTable_generic_8bit: quality 20"],
    "6a620af9bc5e23167b198669246973f3": ["md5JPEGQuantTable_generic_8bit: quality 21"],
    "80eca48ecb7e61bf13fb3e878fc2f3ef": ["md5JPEGQuantTable_generic_8bit: quality 22"],
    "8359073a8222939f83f5478f85a597e0": ["md5JPEGQuantTable_generic_8bit: quality 23"],
    "f250a120fe7cd4d54f15a851778c6ece": ["md5JPEGQuantTable_generic_8bit: quality 24"],
    "0f74952dbc1e04fe00aaeaf5797d9eb6": ["md5JPEGQuantTable_generic_8bit: quality 25"],
    "b88f753c001a0a8cc0c38072240f5621": ["md5JPEGQuantTable_generic_8bit: quality 26"],
    "2d2ce8bb5dd6e90b06a54a1fab9b45be": ["md5JPEGQuantTable_generic_8bit: quality 27"],
    "cede691a46c909ba737e33e0031de1ec": ["md5JPEGQuantTable_generic_8bit: quality 28"],
    "f118c787084dd1f48828280b61c43a64": ["md5JPEGQuantTable_generic_8bit: quality 29"],
    "d02c540d988781a08501743763f028c9": ["md5JPEGQuantTable_generic_8bit: quality 30"],
    "a3b716dc2aa847807c19e7296478f7a6": ["md5JPEGQuantTable_generic_8bit: quality 31"],
    "3b3bd1db6c897f2d62969b97e598798b": ["md5JPEGQuantTable_generic_8bit: quality 32"],
    "267a8f1d16406ec77b817f6a210a0f28": ["md5JPEGQuantTable_generic_8bit: quality 33"],
    "c1479ced7a0730e71c7eb7fefa4e87c3": ["md5JPEGQuantTable_generic_8bit: quality 34"],
    "d32dd9b7c429e0c5bbff5ac20e8d7db6": ["md5JPEGQuantTable_generic_8bit: quality 35"],
    "d0b531e1d4a5856c217fb756edf00065": ["md5JPEGQuantTable_generic_8bit: quality 36"],
    "f3b3babe51b60f95e483682d050c516f": ["md5JPEGQuantTable_generic_8bit: quality 37"],
    "be48316cde3d67a043c966ff01484924": ["md5JPEGQuantTable_generic_8bit: quality 38"],
    "c11ca27e5fa00a5080a8a70dfc8864b4": ["md5JPEGQuantTable_generic_8bit: quality 39"],
    "2847ccd81766e28ea228bba44559b917": ["md5JPEGQuantTable_generic_8bit: quality 40"],
    "2679b9d4d57b6ec1d7ca64519a4b418d": ["md5JPEGQuantTable_generic_8bit: quality 41"],
    "44f043003c6a08054d68b83f6fd14724": ["md5JPEGQuantTable_generic_8bit: quality 42"],
    "7b3b1fc840bccc3888a2d3e663f2970f": ["md5JPEGQuantTable_generic_8bit: quality 43"],
    "fdeb7bc9925399ffacbec9bba626b2a2": ["md5JPEGQuantTable_generic_8bit: quality 44"],
    "bf39813b2a05f26984dcb42eac209fd7": ["md5JPEGQuantTable_generic_8bit: quality 45"],
    "9df12a97ecad0de72b47f815e7cf1f90": ["md5JPEGQuantTable_generic_8bit: quality 46"],
    "6acf79783149a4b79ef29c05b3d8b714": ["md5JPEGQuantTable_generic_8bit: quality 47"],
    "bc4e466f2f47200f01ea1761560b31c3": ["md5JPEGQuantTable_generic_8bit: quality 48"],
    "c5a0fc0bc06bb28218c438acca556d20": ["md5JPEGQuantTable_generic_8bit: quality 49"],
    "97a674ee97943d04d4abe0707f4d2a70": ["md5JPEGQuantTable_generic_8bit: quality 50"],
    "50568b434c8b8684a8cce5ebdb7a11f8": ["md5JPEGQuantTable_generic_8bit: quality 51"],
    "6386d78f7cec0ed8c7d0da9440c15e0a": ["md5JPEGQuantTable_generic_8bit: quality 52"],
    "4f67692eab1070ff059841212085e848": ["md5JPEGQuantTable_generic_8bit: quality 53"],
    "adb6c939884eb0528fbf942d78a1c8fb": ["md5JPEGQuantTable_generic_8bit: quality 54"],
    "d1e7fe2e327c3beb49ccd1f70e35f6ec": ["md5JPEGQuantTable_generic_8bit: quality 55"],
    "cd00e3c73c954e1105dc0857da2b7dd8": ["md5JPEGQuantTable_generic_8bit: quality 56"],
    "56fecf89c0b6bf384e57918f1aae40c3": ["md5JPEGQuantTable_generic_8bit: quality 57"],
    "93c019aed9baae7443ae692dcc2c7d53": ["md5JPEGQuantTable_generic_8bit: quality 58"],
    "40bee0e8b14de55b3c5b24fadd8721eb": ["md5JPEGQuantTable_generic_8bit: quality 59"],
    "889a3a6edd4e63dfb82251950dc7fa3e": ["md5JPEGQuantTable_generic_8bit: quality 60"],
    "356ae946498a3010c1a15a8ed0ed7028": ["md5JPEGQuantTable_generic_8bit: quality 61"],
    "b84e01f496f407ce939bf6681f2eeab8": ["md5JPEGQuantTable_generic_8bit: quality 62"],
    "3cf017ed2a68c6fd20f2cd4992c6b1f8": ["md5JPEGQuantTable_generic_8bit: quality 63"],
    "fac1419993727b3fe07339f326b53c95": ["md5JPEGQuantTable_generic_8bit: quality 64"],
    "182b27dbc8e8f36129ebef7d862432b6": ["md5JPEGQuantTable_generic_8bit: quality 65"],
    "a698af80f2dab58fcf8125ee39599896": ["md5JPEGQuantTable_generic_8bit: quality 66"],
    "765dc096fcb0600e63e5cac6dfcecae9": ["md5JPEGQuantTable_generic_8bit: quality 67"],
    "0e71251df89b6b79d432a661bb698b12": ["md5JPEGQuantTable_generic_8bit: quality 68"],
    "66eafc920154df0560ea5a14957d7121": ["md5JPEGQuantTable_generic_8bit: quality 69"],
    "c5b62b4c62a2375399d18544d829670d": ["md5JPEGQuantTable_generic_8bit: quality 70"],
    "4c0e057c28a45dc08ccc2edc0e10a6be": ["md5JPEGQuantTable_generic_8bit: quality 71"],
    "a10202928e8ec00e9f589d20cf78a1a9": ["md5JPEGQuantTable_generic_8bit: quality 72"],
    "43a7a89b0462def4cfe483c241c386d0": ["md5JPEGQuantTable_generic_8bit: quality 73"],
    "05546b938db9090621291de40151b6cb": ["md5JPEGQuantTable_generic_8bit: quality 74"],
    "29443d7a6f506ce953b18477c3b0f15c": ["md5JPEGQuantTable_generic_8bit: quality 75"],
    "73c39de127a42601bbeabe9be5315448": ["md5JPEGQuantTable_generic_8bit: quality 76"],
    "434895b1589fc41c14e6e391047a6e3a": ["md5JPEGQuantTable_generic_8bit: quality 77"],
    "ce2d95a115369e048a9b94c2a16b4a0f": ["md5JPEGQuantTable_generic_8bit: quality 78"],
    "b69b24387f0b8f16a019aef8ba7b0c03": ["md5JPEGQuantTable_generic_8bit: quality 79"],
    "2e67df9269b8f16d20169289e20b811f": ["md5JPEGQuantTable_generic_8bit: quality 80"],
    "21ab6aeb790dad1b6791997a4bb7d8f3": ["md5JPEGQuantTable_generic_8bit: quality 81"],
    "7c77cca695b0219c728e7d92e96e660e": ["md5JPEGQuantTable_generic_8bit: quality 82"],
    "a0e64f687090313ebf402d9d4e1ac0df": ["md5JPEGQuantTable_generic_8bit: quality 83"],
    "9c052a6b24d6da14a677116b3782f279": ["md5JPEGQuantTable_generic_8bit: quality 84"],
    "9db1b8d118f89b28346a1412a7616bd4": ["md5JPEGQuantTable_generic_8bit: quality 85"],
    "4ebd45b8f2ad25b7c6df97450ee2af86": ["md5JPEGQuantTable_generic_8bit: quality 86"],
    "f1a2b75e72dfeada26d8f99619b93f76": ["md5JPEGQuantTable_generic_8bit: quality 87"],
    "463cf38a951f1bd4111d6b777aec5310": ["md5JPEGQuantTable_generic_8bit: quality 88"],
    "97b4f64c6e462f824f17c741309d236a": ["md5JPEGQuantTable_generic_8bit: quality 89"],
    "2fe0a190e4154e82d7f039dbcc13614b": ["md5JPEGQuantTable_generic_8bit: quality 90"],
    "35cf8d630568e61b27b61070b52edb62": ["md5JPEGQuantTable_generic_8bit: quality 91"],
    "a9b9a227e64b762688c15faf4be7a81d": ["md5JPEGQuantTable_generic_8bit: quality 92"],
    "595a62ef2a9ce3de20e5ff92fd2045ff": ["md5JPEGQuantTable_generic_8bit: quality 93"],
    "0b2b0abee13f7443212c25bdabdc4b56": ["md5JPEGQuantTable_generic_8bit: quality 94"],
    "f9914118c83ea8bd79bfb94b82a34740": ["md5JPEGQuantTable_generic_8bit: quality 95"],
    "11d1dbd45fa438e0c3cab13930a13109": ["md5JPEGQuantTable_generic_8bit: quality 96"],
    "cba0e7f1083d117151acdc060822b67a": ["md5JPEGQuantTable_generic_8bit: quality 97"],
    "14eb1fd9dda3b7ff1e677e15bb3ceff3": ["md5JPEGQuantTable_generic_8bit: quality 98"],
    "89e3c32a57d950043c3330de8911cc91": ["md5JPEGQuantTable_generic_8bit: quality 99"],
    "478a916c3e526e8e3c2cf7c853924f3d": ["md5JPEGQuantTable_generic_8bit: quality 100"],
    "14e5707616bb8fd5d0d65e098a13be75": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 1"],
    "c3628e56a325fd81d39aead1f0d8cbbc": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 2"],
    "55f1d71309f78a9358200bcfd3c36249": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 3"],
    "56b53b106103016c58c346571694781c": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 4"],
    "4753aa2b521807f38d36dd1a4514565d": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 5"],
    "af05445541ef4dca66560c837a74417f": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 6"],
    "10e397ea08a0f34fbd146b5fb70745d8": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 7"],
    "1d94af42d0dcf6e05fb1478fe1d404fe": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 8"],
    "0d2ae2b4c00891c5703b7676a35bb25b": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 9"],
    "cda11d7b48b684b3591cfe0fc12aadd6": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 10"],
    "590bf7c6c82ddf9fcfbce2387013aedc": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 11"],
    "af1109e1eaa36360f78a85065aec4212": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 12"],
    "51c1349d281b10f86638710652600b4e": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 13"],
    "c6169d937af500eb3678f23070a53e71": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 14"],
    "03f5e9be7d4e18d7e7630d3af50ab6d5": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 15"],
    "be7345f6d85ce769ef95e6679e1182ff": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 16"],
    "ebac68105888de0b1559bbfdb44153fe": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 17"],
    "e67f62f10f728654412cbd0db3d9ef3a": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 18"],
    "6b7e182ebc831b058d1351cd76ca5fde": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 19"],
    "cbde6330d3913e16b6c2b4d1cebbeef2": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 20"],
    "d67595ae924f5d02840c15df20c5a249": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 21"],
    "c545a67b59762e27a5e7f566c9812f73": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 22"],
    "0235a9e89ed0a3ac65e95a87d29c611e": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 23"],
    "1592a9f85208bcd3cc00e87c77b887be": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 24"],
    "315181de1dbb3df9b84a6ece5f0a22ce": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 25"],
    "58ebdd6afa8cc14e37f7a57b71b8b8fa": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 26"],
    "8bf710ffeeba78527fa6008bd3e7c1a0": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 27"],
    "4feb2e4d2a042662a90ea21b11107dc1": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 28"],
    "fecce20525708ff67fbc10728cf0dc75": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 29"],
    "dc498543e263f3f6e1747dfef126ae7b": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 30"],
    "eb7204cea3cff036eec0917e68d65d99": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 31"],
    "cc2aaf55f44d10317032c672f331d89e": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 32"],
    "48074c29fe44895df8175b4337ff3c57": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 33"],
    "0a80d13c2d157ec2b55a767238d997d2": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 34"],
    "9de8b780e038449d1c0aaf36cf62af4a": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 35"],
    "e1875c51bf31de73712189c36f023974": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 36"],
    "7626f31dda90023ce36649aaf446dfdf": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 37"],
    "b25f604949d320f779a5911622cd5412": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 38"],
    "160b92f5c94b2693553f4e5d0396de6b": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 39"],
    "94989dc7fb7da09c7f688ae9a8e4bbfe": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 40"],
    "14ed95069361a597eb39ef3128a862e9": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 41"],
    "6c60224694780cd4066511d0e39d404d": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 42"],
    "cc4ca9e2cbcdf98e53c8dc7d4207ef3e": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 43"],
    "2d0612269677fd6369b321be7c919b76": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 44"],
    "9e292f14aa88c8b0e4135f2d494d31f8": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 45"],
    "ed26fc751997f272d266e6e8c9de520e": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 46"],
    "edce19caeb2990348701642ac2e7eb79": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 47"],
    "2165bbc2d77ede2ea6d7af94d63962ed": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 48"],
    "cf2b4886a398d4d205c3ef2c4b9b476f": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 49"],
    "e2df2906a8d3bebfe8db0022ad3fefb7": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 50"],
    "e5addf1aa642a164760171ecfe642b23": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 51"],
    "5aee55f61b1a0d8a1a28099b15a3487e": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 52"],
    "c75507bc6161f108e13886f74aa57f96": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 53"],
    "3387683bbd89a76e1264adb4cc9fe33f": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 54"],
    "7523dcae5898c56deee1e7792d7f1bcb": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 55"],
    "e87493f568670a56a5707d1fb941bd08": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 56"],
    "c8c3643df89693b275e6e761ca91ceca": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 57"],
    "70ba93b047ef64f2e3afdba7d1c09e69": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 58"],
    "786cf16fc9235501bcaf886ac99c0c84": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 59"],
    "5b9f5cd2e2c6cdf547008e5038504d11": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 60"],
    "433713a1eadd82dc490c092594f6199d": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 61"],
    "929e1d8f71744c0a521df674e2eb9bb3": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 62"],
    "0dc9977561a812307f81480ab0109f0b": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 63"],
    "7d6cc8b86844046f2718c2c243c4668a": [
        "md5JPEGQuantTable_3_YCBCR_8bit: quality 64",
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 64",
    ],
    "5e06bcbfeba331104aa1d5bfb5a40d66": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 65"],
    "5d38d939b1c2678d6a8a6708ad91d937": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 66"],
    "9fadcf58e6192091fef8c43265f2746c": [
        "md5JPEGQuantTable_3_YCBCR_8bit: quality 67",
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 67",
    ],
    "8e79ea522dce4333a8dfaaf29991350b": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 68"],
    "a356461d43a00b22ea4d486c1bd3ece0": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 69"],
    "fcf730a40f4963218baec5ebf9b2df6d": [
        "md5JPEGQuantTable_3_YCBCR_8bit: quality 70",
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 70",
    ],
    "d7ebd815e198ace5832ec281f0095476": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 71"],
    "3f420cdf13aa02dfaf093ed00d1c90a2": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 72"],
    "3bbe0fa9b9e23a88e4ed09e845e42f79": [
        "md5JPEGQuantTable_3_YCBCR_8bit: quality 73",
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 73",
    ],
    "0f53fc85df10e530c00bb55765906be7": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 74"],
    "d1d1c2937f3d3ab8797f3ca289a39705": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 75"],
    "f22822a4fc2b5b5a102e507552b59399": [
        "md5JPEGQuantTable_3_YCBCR_8bit: quality 76",
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 76",
    ],
    "4fdbb71af804f68ca8db0dd31d5862aa": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 77"],
    "127069e7892b0f4061c8a763edd57964": [
        "md5JPEGQuantTable_3_YCBCR_8bit: quality 78",
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 78",
    ],
    "a84984ab641ed482814900b53d63ee3e": [
        "md5JPEGQuantTable_3_YCBCR_8bit: quality 79",
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 79",
    ],
    "fccfc6a235b0a7d4354764dc1ea99d29": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 80"],
    "ab9b3a89d6deed60a449baeed1d82025": [
        "md5JPEGQuantTable_3_YCBCR_8bit: quality 81",
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 81",
    ],
    "d5159ddcd4b7e805148a275ddb171448": [
        "md5JPEGQuantTable_3_YCBCR_8bit: quality 82",
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 82",
    ],
    "438bf8f376179bd37dae623be336b0df": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 83"],
    "62e617f3c7ffb44ba521dc920f7ead00": [
        "md5JPEGQuantTable_3_YCBCR_8bit: quality 84",
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 84",
    ],
    "5537ddea3a79c613bab95c5ced23d800": [
        "md5JPEGQuantTable_3_YCBCR_8bit: quality 85",
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 85",
    ],
    "ba4e5e5ddba82e76d18f1bf9016faba8": ["md5JPEGQuantTable_3_YCBCR_8bit: quality 86"],
    "b92849ade60b8493500ce78a270f4e30": [
        "md5JPEGQuantTable_3_YCBCR_8bit: quality 87",
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 87",
    ],
    "2c6ac3d1b80706b4c63af00ba7853a51": [
        "md5JPEGQuantTable_3_YCBCR_8bit: quality 88",
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 88",
    ],
    "bf963e57a863b82dd76df545ebefd8b7": [
        "md5JPEGQuantTable_3_YCBCR_8bit: quality 89",
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 89",
    ],
    "e73d5c4cc59e9a68c892cab97c8bf57e": [
        "md5JPEGQuantTable_3_YCBCR_8bit: quality 90",
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 90",
    ],
    "4d6fe6684875c811be4df97718e8c61c": [
        "md5JPEGQuantTable_3_YCBCR_8bit: quality 91",
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 91",
    ],
    "56e3d2b36568d77c2b8ffeb8fecbb33b": [
        "md5JPEGQuantTable_3_YCBCR_8bit: quality 92",
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 92",
    ],
    "e1668f617e81cdb12a571963fda68efa": [
        "md5JPEGQuantTable_3_YCBCR_8bit: quality 93",
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 93",
    ],
    "0a60c8049224f4f6e795d1934063b1b7": [
        "md5JPEGQuantTable_3_YCBCR_8bit: quality 94",
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 94",
    ],
    "024ea541602ccf6fbebf896af61925c2": [
        "md5JPEGQuantTable_3_YCBCR_8bit: quality 95",
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 95",
    ],
    "5ef21287a0ddcd9812763663bd22c9f6": [
        "md5JPEGQuantTable_3_YCBCR_8bit: quality 96",
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 96",
    ],
    "3a392ab4ec38d7b39cdb4f533217f96f": [
        "md5JPEGQuantTable_3_YCBCR_8bit: quality 97",
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 97",
    ],
    "cc0624dae2798e112762cee338b9a659": [
        "md5JPEGQuantTable_3_YCBCR_8bit: quality 98",
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 98",
    ],
    "55831b93c8f92bff09f91029bb6b8ae6": [
        "md5JPEGQuantTable_3_YCBCR_8bit: quality 99",
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 99",
    ],
    "75a5e8379c028e51b3d4cb19d57f5cd4": [
        "md5JPEGQuantTable_3_YCBCR_8bit: quality 100",
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 100",
    ],
    "0915b609019f595dc71811c1f5e9b873": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 1"
    ],
    "64a07aca404d22a858cb7feb586f789f": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 2"
    ],
    "61e9c802500df4c5b12a7aa1517b8026": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 3"
    ],
    "874921d232bf9f248b18551408af66e1": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 4"
    ],
    "2707f8d7aa21508e23d22822687d2691": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 5"
    ],
    "7b794cd1880acf30a22132bb029ef338": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 6"
    ],
    "16aac58f9413429a614839ae610c52ea": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 7"
    ],
    "30c03b0b5d0ae86583de12d9c2e32ddd": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 8"
    ],
    "aac437c808f7d0bf2a444330d2d04654": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 9"
    ],
    "b3d444691f29b4ee903e63afe4a65b52": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 10"
    ],
    "8999602cbf6dfac278e3ba447966db43": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 11"
    ],
    "1d7eecbc824df8b831c34f4c9c27f948": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 12"
    ],
    "308baca2c83817760c972f6e6f14fc46": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 13"
    ],
    "54d8110fc99a4116a27a698f1027aaf2": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 14"
    ],
    "b842bb0b054e4dea1340be2d347c9e53": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 15"
    ],
    "bb449674cac0677ad1cd48781846f015": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 16"
    ],
    "e1dd573c1470564dd71c66d2fa87ef77": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 17"
    ],
    "baf18ff54a81f353cbdc41517451d450": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 18"
    ],
    "5f62d36b46985336f185cd242aeef0a9": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 19"
    ],
    "bb000efa249587e41821c30bbcf46192": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 20"
    ],
    "d8c353150627a431fd5db324b8a586fc": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 21"
    ],
    "11c4007164baaa6b83877cb67eeee356": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 22"
    ],
    "939cb2056cccc791f13bb9bcf85c226f": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 23"
    ],
    "04b1b476f7d4733d157a6bdabea70716": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 24"
    ],
    "90fd542a834957dfe1375f261ec3cf7d": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 25"
    ],
    "117667ea71b8f98b699794c15fac981e": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 26"
    ],
    "b662528bd1e85e3551ea5c420f726267": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 27"
    ],
    "66ed9871d8b461490781f312115c9115": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 28"
    ],
    "df41882fd5980b63d2224ba85bcb77eb": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 29"
    ],
    "01b6ec0e48e7d577e1009d00bee2a182": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 30"
    ],
    "64151802afe2dcdef7bcf4467fbe418c": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 31"
    ],
    "db68f69d0af07222b71398ca797c2f8c": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 32"
    ],
    "6f94e9ddcc89f6ae29ee5f17d442c90a": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 33"
    ],
    "a03368e64d7f4a35b16243ac1183f115": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 34"
    ],
    "34e234dc6b1a61f5b9d43eda036a769d": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 35"
    ],
    "d0cceaa423a6766d10eda6691071ea35": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 36"
    ],
    "fa307ea4ac4c419ab35d2df175f063d0": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 37"
    ],
    "dcc787ea1270dce0f908a16e3b69da33": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 38"
    ],
    "04cd0275f680002ad2a2274b845f2169": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 39"
    ],
    "4c8df0a1b06efa55d035014be9868177": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 40"
    ],
    "37ae789a218894af0e38e06d8f8475c0": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 41"
    ],
    "3b96d5fe0f12f4737f457ed7ea3b3dc3": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 42"
    ],
    "a8460d779a4d45f307b49432a835b47f": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 43"
    ],
    "06c27a76bb39479c2669057efc438278": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 44"
    ],
    "8b91d70057001ff28b8b76f7f0ab43a7": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 45"
    ],
    "d54ee9b25da82f3342071c44b0c60ecf": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 46"
    ],
    "933b197b80ed81f09ebae15eb6344cc8": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 47"
    ],
    "0ba4505ad0d3f99428be8e72c73ab161": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 48"
    ],
    "4cf23130126aa06ea0344e74e5acf2d1": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 49"
    ],
    "4db26102bdbf54885ccb866e65d2086b": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 50"
    ],
    "7ec9886b0eba76e0298f3c8abee50708": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 51"
    ],
    "b5c13b41d68306085ce91e146503b919": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 52"
    ],
    "b8df76be92d452d9b1ade03e1f2f38c9": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 53"
    ],
    "8cee0bad5b647d3bca972ac4d1f61170": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 54"
    ],
    "c6abd06df3d20f2a2af2a8345a558afb": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 55"
    ],
    "9525f0b83ca084062ade7a5d0bb7726c": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 56"
    ],
    "013fddaa9ab7ea4e9b60c535693eb235": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 57"
    ],
    "931a5b2d24e37533ed610a7d9fea576a": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 58"
    ],
    "b155a0883e74fb2777883bd54df94b52": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 59"
    ],
    "9210ae6fa8987bad7fe24fa7cb67d34d": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 60"
    ],
    "1b426b74180f3857707b63cbbdac7532": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 61"
    ],
    "8a9d6c3e3342122ff9ce46656fbcec53": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 62"
    ],
    "423e330aec52b36a3141573eca3eb4c7": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 63"
    ],
    "9e760db2032cf315793c18bb8ffe0093": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 65"
    ],
    "de1444357343710ff69d19143a3d71b0": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 66"
    ],
    "a585c4bf390f74868f9b6a2a3ac7f329": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 68"
    ],
    "5a28af3b3d62b29293da17dcbf7a2ab4": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 69"
    ],
    "93a0c9492beb22b9b4aa2158480eb2db": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 71"
    ],
    "5b7c75462009bd0c16c21d943f90154e": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 72"
    ],
    "c1da2c9b41e7ac27015a65d523fa06f4": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 74"
    ],
    "20acc189183b13078acf18e2fefc85fa": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 75"
    ],
    "4a20577d695325d732d95e2eaacc981c": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 77"
    ],
    "5734f5f6dcf476ec0ec9c97db371bde3": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 80"
    ],
    "f0ec19cce0e94125f1ffbaaf196cbf4c": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 83"
    ],
    "3033af62b7c89a87289e6ef596640460": [
        "md5JPEGQuantTable_3_YCBCR_8bit_jpeg9e: quality 86"
    ],
}
