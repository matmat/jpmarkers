# Digital Forensics Project

This script looks at the structure of a JPEG image and reports markers, segment length (excluding)
the marker itself and a hash of the segment data. Bitstream data (image data) is handled as a
special case segment.

Example run:

```
$ ./jpmarkers.py cat.jpg  
Offset  Marker            Length
000000: SOI   (0xFFD8)         0  
000002: APP0  (0xFFE0)        16  d8475a1e0eeb5c32b85cc48f239d48da3a7955a11366ecc0d2527424594674b5
000014: APP2  (0xFFE2)       540  f08f321852dfc3286df5f2d3a491e5261bd02ac0200e89f5a1100e70f3d7384c
000232: DQT   (0xFFDB)       132  b9fc7dca997e12281ea9958bf83ad754c8e8914eba3a6635bb1ed28cc732ff71
0002B8: SOF2  (0xFFC2)        17  8067063a373d7c00044773b6f11f3aba2f0f626e737f1b464a7e0ee345cecf84
0002CB: DHT   (0xFFC4)        29  ee0d400f5923c271fc0f2a74dfa29cfcca2c2e5aa67af18908afab0ca57e81da
0002EA: SOS   (0xFFDA)         8  c224337603c70d07efdbf0f56292d9c2c94db622ecd4c2991cd4718ed6444f98
0002F4: [bitstream data]    2986  f979754f4b233de8b577545dcf15f301e69bafa6b2b55c35a9e59b33c27fe9e0
000E9E: SOS   (0xFFDA)         8  a65a7cc3d5839202ca1223184c5d1a3a25c9802a26e3d992f13ed16a18083e6a
000EA8: [bitstream data]     411  0492c2cfedf36de4f7155b8664ca4fd7aedb3e18eb7a5616c9bc6a53e021323a
001043: SOS   (0xFFDA)         8  f4ca5ba89f7dd0f3b208a0b7ebde19f9ef8fef31d12fc3f6c41bc921c6379699
00104D: [bitstream data]     399  546a7f47a3aec9d6a1f5aa32019511e984f0cedfc6db7d6a13bea7cd41d5e4cb
0011DC: SOS   (0xFFDA)         8  c7bdd8c166a668248bc313d434d8de1205f1ca51d7d97528f2567d14a0ecefa3
0011E6: [bitstream data]    3623  c73770f3c9f8738aa3074a9b131157a7f1afe76a97ecd1507da2078a377576ed
00200D: SOS   (0xFFDA)         8  ff0cbb55723064badbb7984654d15aac8bd6deb4dcc2d173d08c55faa2457cea
002017: [bitstream data]   10396  e75193f7cc837881d4d40d8e79bbbc5a0d5311a4d84cc4a7910bda5db00d2730
0048B3: SOS   (0xFFDA)         8  b15a6d3dc56ce2fee47f9656cf89635f6653bb7ce25d1b9a16cda34232b86171
0048BD: [bitstream data]   11059  cbfc83bc13d51bcc873e236c35e3f4ca09bdc3b20308211f5927cc6e66604fd8
0073F0: SOS   (0xFFDA)         8  3a7df4ff60709a02e1f3374d034b0d95047a2c8181c06e8f4ab334f08647c617
0073FA: [bitstream data]    1138  4cec6a5ed6f089fa034a9e397ff0240f494e611e3bbdc41c349dcc6013028704
00786C: SOS   (0xFFDA)         8  751543f2b2d6185151c105447d2cb453b61844be9ff7d1779f6b7a9a875e23af
007876: [bitstream data]     906  8b4b4a114b3993dfda359e6df73dcc5664d3396ef3a328e3b56d2e8ce84cd50e
007C00: EOI/C (0xFFD9)         0  
```


Example run on a .j2c file (JPEG200 code stream):

```
$ ./jpmarkers.py 001014.j2c 
Offset  Marker            Length
000000: SOC   (0xFF4F)         0  
000002: SIZ   (0xFF51)        47  ab8d6a45ad5e02584a2ad89b4804ace6310fe4770acba56fae46516af9d5d1f8
000033: COD   (0xFF52)        18  3793a7a0868e80e7edfe59b0c32aec245939c085f61f312e25c20d5a09142973
000047: QCD   (0xFF5C)        35  1d6f2b3f2989959728137f50fd3dee8e903464e0a0986c7ee0ab9a10508e4fec
00006C: COM   (0xFF64)        64  e7ca8ab44dcc70c2584bb56435340b9e683db36b6182fd1a98bdb51d9637731a
0000AE: TLM   (0xFF55)        22  4bf21e872e076539c0acc14edae613d5848ac6f414b6f1c42f31ab93db2b45c0
0000C6: SOT   (0xFF90)        10  5513432f6ba1919c4104ed100e549c7f5724bc912af3af6e261d7066b8bf7b37
0000D2: SOD   (0xFF93)         0  
0000D4: [bitstream data]  579181  3e045670161bddb67ce0d0951466d168c740021b78c17682ee556885209130bc
08D741: SOT   (0xFF90)        10  57a956b00b009a4d2470f733608a9c051d6363067cea0ac3895098992805508a
08D74D: SOD   (0xFF93)         0  
08D74F: [bitstream data]   40996  f4c2e8c60d9c8c246440e0d78dc208e26b96853a422b80ac0ebbf25f66325183
097773: SOT   (0xFF90)        10  b8660dc97d77a8186920f090f9cbb35f7d81eea65cfc54ba2ee3650576a5a3c1
09777F: SOD   (0xFF93)         0  
097781: [bitstream data]   18507  057682716c544aed285fe0c3e8ef30198f143c360b0daf3709cc6312bb3502e5
09BFCC: EOI/C (0xFFD9)         0
```
