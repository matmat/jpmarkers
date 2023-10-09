'''
Copyright (C) 2023 - Mattias Iko Mattsson
Copyright (C) 2016 - PH
Copyright (C) 2008 - P. Harvey Created

This file is extracted from lib/Image/ExifTool/JPEGDigest.pm of exiftool 
'''

sigs = {
    "00687c4e4852ed1cd446c09a3764e505": [
        {"description": "Apple QuickTime, " "Quality 560 (55%)", "subsampling": "11"}
    ],
    "00f03e367cd316b71de360c6e7af0e6b": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 92",
            "subsampling": "111111",
        }
    ],
    "00f76480eafd05aa5267053aec3aa122": [
        {
            "description": "Apple QuickTime, " "Quality 423 (41%)",
            "subsampling": "221111",
        }
    ],
    "00f929d549fdd9f89fbb10303445cc2c": [
        {
            "description": "Apple QuickTime, " "Quality 328 (32%)",
            "subsampling": "221111",
        }
    ],
    "0106cf02dcf4109cc6f02fa4ec0e2700": [
        {
            "description": "Apple QuickTime, " "Quality 693 (68%)",
            "subsampling": "221111",
        }
    ],
    "01137dc7ef90f0aee15362c221f7b1d3": [
        {
            "description": "Apple QuickTime, " "Quality 756-758 (74%)",
            "subsampling": "221111",
        }
    ],
    "0147c5088beb16642f9754f8671f13b3": [
        {"description": "Canon PowerShot, Fine", "subsampling": "211111"}
    ],
    "016600f44a61cc5a5673c9bad85e23a3": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 66",
            "subsampling": "111111",
        }
    ],
    "01b48291bfeccf2fadab996816225b9b": [
        {
            "description": "Apple QuickTime, " "Quality 180-182 (18%)",
            "subsampling": "221111",
        }
    ],
    "01f997907a4c1dfd1e6b00aca9ff5d80": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 84", "subsampling": ""}
    ],
    "0233ba670d2891e75da3ce5e7664cb67": [
        {"description": "Apple QuickTime, " "Quality 745 (73%)", "subsampling": "11"}
    ],
    "02374d6405239e8fe5ab939b92f4fd03": [
        {
            "description": "Apple QuickTime, " "Quality 999-1000 (98%)",
            "subsampling": "11",
        }
    ],
    "026780f2172c289bc1ff73a34c6aee57": [
        {
            "description": "Apple QuickTime, " "Quality 759-760 (74%)",
            "subsampling": "221111",
        }
    ],
    "0268c3e9e3e1c3e6eb25fe0d31940c7f": [
        {"description": "Apple QuickTime, " "Quality 525 (51%)", "subsampling": "11"}
    ],
    "028caa124d0837dd9b1a64028e4f2965": [
        {
            "description": "Apple QuickTime, " "Quality 819 (80%)",
            "subsampling": "211111",
        }
    ],
    "028fafd94aa66ee269f58d800c89d838": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 15",
            "subsampling": "221111",
        }
    ],
    "029b3a6f0b92af6786d753788eafabfe": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 3",
            "subsampling": "221111",
        }
    ],
    "02c0554e4a004ceaddd0d7772e68a38b": [
        {
            "description": "Apple QuickTime, " "Quality 364 (36%)",
            "subsampling": "221111",
        }
    ],
    "02e9a58edf45d75be000dee144316c66": [
        {"description": "Apple QuickTime, " "Quality 593 (58%)", "subsampling": "11"}
    ],
    "030736cda242f0583a7064cb60cc026e": [
        {
            "description": "Apple QuickTime, " "Quality 329 (32%)",
            "subsampling": "221111",
        }
    ],
    "03201bd5642a451d99b99bfd10fc42df": [
        {"description": "Nikon Capture NX, " "Quality 18", "subsampling": "221111"}
    ],
    "032678d9de74e5530896c28079f666af": [
        {"description": "Nikon Capture NX, " "Quality 72", "subsampling": "211111"}
    ],
    "03295b26893cab9c7dea4ec15ed56d08": [
        {
            "description": "Apple QuickTime, " "Quality 494 (48%)",
            "subsampling": "221111",
        }
    ],
    "033472a8a855fab8cd8f6a5788dd07c8": [
        {
            "description": "Apple QuickTime, " "Quality 725 (71%)",
            "subsampling": "221111",
        }
    ],
    "03651ac1d15043f77949a63ac3762584": [
        {"description": "Nikon Capture NX, " "Quality 16", "subsampling": "221111"}
    ],
    "036d2395718f99bf916486e1af42cb92": [
        {"description": "Apple QuickTime, " "Quality 251 (25%)", "subsampling": "11"}
    ],
    "037d043c8a8d5332c28d59f71a0dcfd2": [
        {"description": "Pentax Optio E35", "subsampling": "211111"}
    ],
    "03809d08372d3a9fd86ff254854f45b7": [
        {
            "description": "Apple QuickTime, " "Quality 344 (34%)",
            "subsampling": "221111",
        }
    ],
    "0381b4e34e700adecd618afdcfb5513e": [
        {"description": "Apple QuickTime, " "Quality 347 (34%)", "subsampling": "11"}
    ],
    "039a3f0e101f1bcdb6bb81478cf7ae6b": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "15 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 15",
            "subsampling": "111111",
        },
    ],
    "03c035b39889356e0b10805d8549a1f7": [
        {
            "description": "Apple QuickTime, " "Quality 810 (79%)",
            "subsampling": "211111",
        }
    ],
    "040c8ed8b19485d8677b964b03bc9929": [
        {
            "description": "Apple QuickTime, " "Quality 791-792 (77%)",
            "subsampling": "11",
        }
    ],
    "040e09f495355470a44c580bca654693": [
        {"description": "Apple QuickTime, " "Quality 337 (33%)", "subsampling": "11"}
    ],
    "041c9e3cf0d34a8b89539e3115bca31b": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 2",
            "subsampling": "221111",
        }
    ],
    "042ae0dbef2b1e91c4eb36e66a39b5b9": [
        {"description": "Apple QuickTime, " "Quality 81-92 (8-9%)", "subsampling": "11"}
    ],
    "043645382c79035b6f2afc62d373a37f": [
        {"description": "Apple Aperture Quality " "9", "subsampling": "221111"}
    ],
    "0440231d1a4a1187bffaa5b5576827f9": [
        {
            "description": "Apple QuickTime, " "Quality 820 (80%)",
            "subsampling": "211111",
        }
    ],
    "0442196d850319833f27df632e92f064": [
        {"description": "Apple QuickTime, " "Quality 425 (42%)", "subsampling": "11"}
    ],
    "0443da2c934e95fca0df8a0a1433eea4": [
        {
            "description": "Apple QuickTime, " "Quality 878-880 (86%)",
            "subsampling": "11",
        }
    ],
    "0468ecbf6fc1303467adfdcab8edfe6d": [
        {"description": "Apple QuickTime, " "Quality 362 (35%)", "subsampling": "11"}
    ],
    "04710d4ba5233b4f82bd260263f9e992": [
        {
            "description": "Apple QuickTime, " "Quality 335 (33%)",
            "subsampling": "221111",
        }
    ],
    "047e1711c44262f352034452d0b0d07b": [
        {"description": "Apple QuickTime, " "Quality 406 (40%)", "subsampling": "11"}
    ],
    "04a5bb959bc203221e72e6575ff39602": [
        {
            "description": "Apple QuickTime, " "Quality 698 (68%)",
            "subsampling": "221111",
        }
    ],
    "054f418c24a6a733186a27aa739dc93a": [
        {"description": "ACD Systems Digital " "Imaging, Quality 63", "subsampling": ""}
    ],
    "058fc759cff9d615f91d9ffb4b46436a": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 28", "subsampling": ""}
    ],
    "05e53fb216ba4a1734eefaccd249d8e2": [
        {"description": "Apple QuickTime, " "Quality 599 (58%)", "subsampling": "11"}
    ],
    "05f98e12bfa14ba6347fb43f2241ba43": [
        {"description": "Apple QuickTime, " "Quality 620 (61%)", "subsampling": "11"}
    ],
    "06186292fe0ccaaeb5999319a366c4b4": [
        {"description": "Nikon Capture NX, " "Quality 47", "subsampling": "221111"}
    ],
    "0643b87475939754c8d56825cd96242f": [
        {
            "description": "Apple QuickTime, " "Quality 667 (65%)",
            "subsampling": "221111",
        }
    ],
    "064f160a8504465551738c9071f3850f": [
        {"description": "ACD Systems Digital " "Imaging, Quality 52", "subsampling": ""}
    ],
    "066fd6cb3a5dd994fc6159987afde581": [
        {
            "description": "Apple QuickTime, " "Quality 565 (55%)",
            "subsampling": "221111",
        }
    ],
    "067a76c2e5386ae85f9187e3e2134621": [
        {"description": "Apple QuickTime, " "Quality 565 (55%)", "subsampling": "11"}
    ],
    "070620a25578b4a38ed0c09d6d512de8": [
        {
            "description": "Apple QuickTime, " "Quality 955 (93%)",
            "subsampling": "211111",
        }
    ],
    "0709c0afc0eae932a50903e56ec95ad2": [
        {"description": "Apple QuickTime, " "Quality 490 (48%)", "subsampling": "11"}
    ],
    "07259679e2a842478df97c7f0ddd4df3": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 58", "subsampling": ""}
    ],
    "07318a0acfebe9086f0e04a4c4f5398a": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "22 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 22",
            "subsampling": "111111",
        },
    ],
    "0740db8af7951c1363f2c8d75462d378": [
        {"description": "Apple QuickTime, " "Quality 327 (32%)", "subsampling": "11"}
    ],
    "07464723ecfd8e5ed8fd6904e9d15a23": [
        {
            "description": "Apple QuickTime, " "Quality 939 (92%)",
            "subsampling": "211111",
        }
    ],
    "076598d43c5186f6d7a1020b64b93625": [
        {"description": "Adobe Photoshop, " "Quality 9", "subsampling": "11"}
    ],
    "078db0d0bffafa44def2e8b85eec26f6": [
        {
            "description": "ACD Systems Digital " "Imaging, Quality 45 or " "46",
            "subsampling": "",
        }
    ],
    "07bd22218437079a86ce0b93ffa9cc90": [
        {
            "description": "Apple QuickTime, " "Quality 784 (77%)",
            "subsampling": "211111",
        }
    ],
    "07d3cd227395b060a132411cbfc22593": [
        {"description": "Panasonic DMC-FZ50, " "High (A)", "subsampling": "211111"}
    ],
    "0807f8b3b41b01054509858fa74dcf4d": [
        {
            "description": "Apple QuickTime, " "Quality 418 (41%)",
            "subsampling": "221111",
        }
    ],
    "0818578fc5fc571b4f8d5ffefc9dc0d8": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "62 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 62",
            "subsampling": "111111",
        },
    ],
    "081da80ed314194b571ff9880a7c11d3": [
        {
            "description": "Apple QuickTime, " "Quality 264-265 (26%)",
            "subsampling": "221111",
        }
    ],
    "082779cf55f6b922036f11b74df54110": [
        {
            "description": "Apple QuickTime, " "Quality 564 (55%)",
            "subsampling": "221111",
        }
    ],
    "08549fa433585b86d6eab75b6dcb1fe3": [
        {
            "description": "Apple QuickTime, " "Quality 340 (33%)",
            "subsampling": "221111",
        }
    ],
    "085db73bd47194c8fdf567fc619c3b62": [
        {
            "description": "Apple QuickTime, " "Quality 570 (56%)",
            "subsampling": "221111",
        }
    ],
    "0867bdf854d1fbb141411de518a66ba6": [
        {"description": "Pentax Optio T20 (A)", "subsampling": "211111"}
    ],
    "086e5ce1149e14efd9e424956734fe05": [
        {"description": "Nikon Capture NX, " "Quality 24", "subsampling": "221111"}
    ],
    "087c1c1a368adc82900d83235f432d3f": [
        {"description": "Nikon Capture NX, " "Quality 35", "subsampling": "221111"}
    ],
    "08c063f0997262d9977df4b44e682d82": [
        {"description": "Nikon Capture NX, " "Quality 86", "subsampling": "111111"}
    ],
    "09321d810a54503da7ad7b8e883227ea": [
        {"description": "Apple QuickTime, " "Quality 903 (88%)", "subsampling": "11"}
    ],
    "093b011ce21ae794d3eca7c64eecf5b6": [
        {
            "description": "Apple QuickTime, " "Quality 269 (26%)",
            "subsampling": "221111",
        }
    ],
    "09563e47ab174b05fb19f722e9aa43c3": [
        {
            "description": "Apple QuickTime, " "Quality 470 (46%)",
            "subsampling": "221111",
        }
    ],
    "097b684846696b3a8bbdf2bd2f9ded9c": [
        {"description": "Nikon Capture NX, " "Quality 32", "subsampling": "221111"}
    ],
    "09a13f94022839a24065b82d5f4ffdbd": [
        {"description": "Apple QuickTime, " "Quality 429 (42%)", "subsampling": "11"}
    ],
    "09b689f7d0c1d4bb0d96d06c02b8dcf8": [
        {"description": "Apple QuickTime, " "Quality 566 (55%)", "subsampling": "11"}
    ],
    "09c168d2e075070d3a2535e7f2e455df": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 25",
            "subsampling": "221111",
        }
    ],
    "09cf94311753aa9796ffd720749c51f7": [
        {
            "description": "Apple QuickTime, " "Quality 896 (88%)",
            "subsampling": "211111",
        }
    ],
    "09ec03f5096df106c692123f3fd34296": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "35 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 35",
            "subsampling": "111111",
        },
    ],
    "09f9009406d2fe8dfa1b35236f8b1bdb": [
        {
            "description": "Apple QuickTime, " "Quality 454 (44%)",
            "subsampling": "221111",
        }
    ],
    "0a0268c655d616b0e4af2851533aa3af": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "86 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 86",
            "subsampling": "111111",
        },
    ],
    "0a50266ad8d1dff11c90cd1480c0a2be": [
        {"description": "Adobe Photoshop, " "Quality 6", "subsampling": "11"}
    ],
    "0a7497e67acef345c655f79fd00b26de": [
        {"description": "Apple QuickTime, " "Quality 276 (27%)", "subsampling": "11"}
    ],
    "0a80e5bf01a9c5650384dfe1a428f61d": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 23",
            "subsampling": "221111",
        }
    ],
    "0a899361ed0d51e224dc535ceb02f9a1": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 36", "subsampling": ""}
    ],
    "0a953ba56b59fa0bbbdac0162ea1c96b": [
        {"description": "Pentax K10D (Z)", "subsampling": "211111"}
    ],
    "0ac5cb651c496369d0e924ae070b7c53": [
        {
            "description": "Pentax Optio A40, " "Better (edit in camera)",
            "subsampling": "211111",
        }
    ],
    "0b52b82694040193aee10e8074cd7ad5": [
        {"description": "Apple Aperture Quality " "11", "subsampling": "221111"}
    ],
    "0b933cf90e62682da926267d6356ac2b": [
        {
            "description": "Apple QuickTime, " "Quality 653 (64%)",
            "subsampling": "221111",
        }
    ],
    "0bac94d5b6ef090da7875e294a7f8040": [
        {
            "description": "Apple QuickTime, " "Quality 331 (32%)",
            "subsampling": "221111",
        }
    ],
    "0bb6bf7365676f75d285bb38a40b8e3f": [
        {
            "description": "Apple QuickTime, " "Quality 334 (33%)",
            "subsampling": "221111",
        }
    ],
    "0bb76dd0e08175a90343a9c7dab48bfa": [
        {
            "description": "Apple QuickTime, " "Quality 264-265 (26%)",
            "subsampling": "11",
        }
    ],
    "0bc0941c2a59d9a12b66d1d34117cfd7": [
        {
            "description": "Apple QuickTime, " "Quality 386 (38%)",
            "subsampling": "221111",
        }
    ],
    "0c0351c3a444b851cd105dd5cc4db59c": [
        {
            "description": "Apple QuickTime, " "Quality 729 (71%)",
            "subsampling": "221111",
        }
    ],
    "0c7d4861b3bee5d766a93f2d34027bfa": [
        {"description": "Nikon Capture NX, " "Quality 94", "subsampling": "111111"},
        {
            "description": "ACD Systems Digital " "Imaging, Quality 97",
            "subsampling": "",
        },
    ],
    "0c9f89a3728234e0e85645c968d1d84a": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "45",
            "subsampling": "",
        }
    ],
    "0cb697537acde3d2e85078377461a8e0": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 57",
            "subsampling": "111111",
        }
    ],
    "0cec2c8f96c092bd6e7cf0f7ea294c99": [
        {"description": "Apple QuickTime, " "Quality 527 (51%)", "subsampling": "11"}
    ],
    "0cec88a0cd8fe35720e78cdcdbdadef6": [
        {"description": "Canon EOS 1DmkII, Fine " "(A)", "subsampling": "121111"}
    ],
    "0d3de456aa5cbb8a2578208250aa9b88": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "7 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 7",
            "subsampling": "111111",
        },
    ],
    "0d501a036c984d2caf49fd298b2d0d16": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 21",
            "subsampling": "221111",
        }
    ],
    "0d5b0af72561f68c671731f22d9e41e2": [
        {
            "description": "Adobe Lightroom, " "Quality 47% - 53%",
            "subsampling": "221111",
        }
    ],
    "0d605d279c48a74ef71a24e89ca426a8": [
        {
            "description": "Apple QuickTime, " "Quality 491 (48%)",
            "subsampling": "221111",
        }
    ],
    "0d70031c9962dba7c39da59ada2f1660": [
        {
            "description": "Apple QuickTime, " "Quality 616-617 (60%)",
            "subsampling": "221111",
        }
    ],
    "0da77ccec22a9cff9a049a47e86d3502": [
        {
            "description": "Apple QuickTime, " "Quality 754 (74%)",
            "subsampling": "221111",
        }
    ],
    "0db59bd18beb49f9beb901f3435e22a5": [
        {"description": "Apple QuickTime, " "Quality 558 (54%)", "subsampling": "11"}
    ],
    "0df2be705ae86e5de1e508db95efb182": [
        {"description": "ACD Systems Digital " "Imaging, Quality 64", "subsampling": ""}
    ],
    "0e08dc629e883530cb2ae78c90f125b3": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 66", "subsampling": ""}
    ],
    "0e0a151e0a52097cbd7683c9385e3a7c": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 13",
            "subsampling": "221111",
        }
    ],
    "0e36104efe90a5a77e9b686d0a6528ab": [
        {
            "description": "Apple QuickTime, " "Quality 385 (38%)",
            "subsampling": "221111",
        }
    ],
    "0e570bc627acaee0962472a1a646816b": [
        {"description": "Apple QuickTime, " "Quality 430 (42%)", "subsampling": "11"}
    ],
    "0e618a0e79b4d540da1f6e07fcdce354": [
        {"description": "Canon PowerShot, " "Superfine Small", "subsampling": "211111"}
    ],
    "0e6c6a5440d33d25f1c25836a45cfa69": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "53 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 53",
            "subsampling": "111111",
        },
    ],
    "0e9648c1f28b99a377dcf7deec6450e6": [
        {
            "description": "Apple QuickTime, " "Quality 851-852 (83%)",
            "subsampling": "211111",
        }
    ],
    "0ee4ea4687d3c57d060e3afd2559b7bb": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "77",
            "subsampling": "",
        }
    ],
    "0ee9ca02a1fe8a17b6e50a2e86d19a7c": [
        {"description": "Nikon Capture NX, " "Quality 28", "subsampling": "221111"}
    ],
    "0eef5c6ff8ba65ff799081a9c96a2297": [
        {
            "description": "Apple QuickTime, " "Quality 618-619 (60%)",
            "subsampling": "11",
        }
    ],
    "0ef4f8fa922f87f1be646fccaa0ef42e": [
        {
            "description": "Apple QuickTime, " "Quality 854 (83%)",
            "subsampling": "211111",
        }
    ],
    "0ef85155f08194f8fed3f4e7197126e6": [
        {
            "description": "Apple QuickTime, " "Quality 214-215 (21%)",
            "subsampling": "221111",
        }
    ],
    "0ef9d9f62ab68807eedf6cb8c2ec120b": [
        {"description": "Nikon Capture NX, " "Quality 0", "subsampling": "221111"}
    ],
    "0efd0d9423b440cfc8efacf2e4dfcb7f": [
        {
            "description": "Apple QuickTime, " "Quality 940 (92%)",
            "subsampling": "211111",
        }
    ],
    "0f125e2c5ee6b123cf67b586ea23d422": [
        {"description": "Apple QuickTime, " "Quality 647 (63%)", "subsampling": "11"}
    ],
    "0f58458f2b9959dbc57b4868200c0432": [
        {
            "description": "Apple QuickTime, " "Quality 830-832 (81%)",
            "subsampling": "211111",
        }
    ],
    "0fdd23e8274090da3c925a3db7303adf": [
        {"description": "Apple QuickTime, " "Quality 602 (59%)", "subsampling": "11"}
    ],
    "0fe0c7e65c0696d9e76ad819d61e44ae": [
        {
            "description": "Apple QuickTime, " "Quality 402 (39%)",
            "subsampling": "221111",
        }
    ],
    "0fe5225afaf055efd8453426c00e81e1": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "40",
            "subsampling": "",
        }
    ],
    "0ff225f58a214f79d1d85d78f6f5dab8": [
        {
            "description": "Adobe Lightroom, " "Quality 47% - 53%",
            "subsampling": "221111",
        },
        {"description": "Adobe Photoshop, " "Quality 6", "subsampling": "221111"},
    ],
    "0ffe7e9fc17393a338b95c345052b7c5": [
        {
            "description": "Apple QuickTime, " "Quality 210-211 (21%)",
            "subsampling": "221111",
        }
    ],
    "100f3392aa8292fb78548513a619671a": [
        {"description": "Apple QuickTime, " "Quality 285 (28%)", "subsampling": "11"}
    ],
    "1027a4af6a2a07e58bbd6df5b197d44e": [
        {"description": "Pentax K10D (A)", "subsampling": "211111"}
    ],
    "104c3b63e4ca667a4ee2e4250340052c": [
        {
            "description": "Apple QuickTime, " "Quality 315 (31%)",
            "subsampling": "221111",
        }
    ],
    "1068be028c278941bd8abf3b0021655e": [
        {
            "description": "Pentax Optio A40, Good " "(edit in camera)",
            "subsampling": "211111",
        }
    ],
    "10c931d7bff7bfcc20e37f0868887228": [
        {
            "description": "Apple QuickTime, " "Quality 545 (53%)",
            "subsampling": "221111",
        }
    ],
    "10d87624d888b75b29e156be8dad35f4": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 26", "subsampling": ""}
    ],
    "111848d9e41f6f408ef70841f90c0519": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "26 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 26",
            "subsampling": "111111",
        },
    ],
    "116e3d5fee4e3a695c0f79c09c89ff84": [
        {
            "description": "Apple QuickTime, " "Quality 699 (68%)",
            "subsampling": "221111",
        }
    ],
    "118a60a90c56bcb363fdd93b911a3371": [
        {"description": "Nikon D50 / D80, Fine", "subsampling": "211111"},
        {"description": "Panasonic DMC-FZ50/TZ3, " "High (A)", "subsampling": "211111"},
    ],
    "118c7b118b1df404c90cfb1d10cf2a77": [
        {"description": "Apple QuickTime, " "Quality 523 (51%)", "subsampling": "11"}
    ],
    "11a232fa9de634fadde1869007baab9c": [
        {
            "description": "Apple QuickTime, " "Quality 997-998 (97%)",
            "subsampling": "11",
        }
    ],
    "11f5fbd5e74e5c5e305b95dbbc4356a8": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 74", "subsampling": ""}
    ],
    "120b93a6ab4a1e8c78578e86e3ef837f": [
        {"description": "Apple QuickTime, " "Quality 819 (80%)", "subsampling": "11"}
    ],
    "12196a46c697fbb88d8bef279b52b106": [
        {
            "description": "Apple QuickTime, " "Quality 241 (24%)",
            "subsampling": "221111",
        }
    ],
    "12239aa16bb4091d8f873f9536e40371": [
        {
            "description": "Apple QuickTime, " "Quality 379 (37%)",
            "subsampling": "221111",
        }
    ],
    "1228da2b97793a88a41542ddcfca7ad2": [
        {
            "description": "Apple QuickTime, " "Quality 921-922 (90%)",
            "subsampling": "211111",
        }
    ],
    "1228f1572d76b53658f4042bda8e99a2": [
        {"description": "Apple QuickTime, " "Quality 287 (28%)", "subsampling": "11"}
    ],
    "127b0599fc6804909a33832be7a9dd36": [
        {
            "description": "Apple QuickTime, " "Quality 887 (87%)",
            "subsampling": "211111",
        }
    ],
    "12aefbf7689633c83da714c9f0e90e05": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "91 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 91",
            "subsampling": "111111",
        },
    ],
    "12b4cc13891c5aef3dadb3405b6fa65d": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "79 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 79",
            "subsampling": "111111",
        },
    ],
    "12d303b2e6a467b4f20a34e695f9da7e": [
        {"description": "Apple QuickTime, " "Quality 837 (82%)", "subsampling": "11"}
    ],
    "12fc29c1d8940c93a47ee9d927a17561": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "94 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 94",
            "subsampling": "111111",
        },
    ],
    "12fe6b9bfd20f4d7f0ac2a221c566c45": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "90 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 90",
            "subsampling": "111111",
        },
    ],
    "1312bc5c7456856400f43749d407fb9f": [
        {"description": "Apple QuickTime, " "Quality 268 (26%)", "subsampling": "11"}
    ],
    "131ddd6eec5f51e825cf7afd9c7ab3b2": [
        {
            "description": "Apple QuickTime, " "Quality 303 (30%)",
            "subsampling": "221111",
        }
    ],
    "133351a0f39427f1199312585cd6c997": [
        {
            "description": "Apple QuickTime, " "Quality 566 (55%)",
            "subsampling": "221111",
        }
    ],
    "1343a117f5fab26d556a3e7558366591": [
        {"description": "FixFoto, Quality 4", "subsampling": ""}
    ],
    "13570e05da917fe51235ef66a295bc78": [
        {
            "description": "Apple QuickTime, " "Quality 151-154 (15%)",
            "subsampling": "221111",
        }
    ],
    "13b1310840627eddaf435e9feffebebe": [
        {"description": "Apple QuickTime, " "Quality 395 (39%)", "subsampling": "11"}
    ],
    "13b2644cdad6f75767667e8ea5c218a3": [
        {"description": "Pentax Optio S, Best " "(B)", "subsampling": "221111"}
    ],
    "13d6536913342860ab993be8b141f644": [
        {
            "description": "Apple QuickTime, " "Quality 199-201 " "(19-20%)",
            "subsampling": "221111",
        }
    ],
    "13e218420429e2c94d4b9474ab03f8e4": [
        {
            "description": "Apple QuickTime, " "Quality 435 (42%)",
            "subsampling": "221111",
        }
    ],
    "14040c7711b6fa62383da3edc9ade1b7": [
        {
            "description": "Apple QuickTime, " "Quality 1018-1020 " "(99-100%)",
            "subsampling": "11",
        }
    ],
    "140cc5a99ef865e318a217ea069aa84d": [
        {"description": "Apple QuickTime, " "Quality 557 (54%)", "subsampling": "11"}
    ],
    "1426dd9c1c8098936f395e201f1eb56d": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "30",
            "subsampling": "",
        }
    ],
    "14276fffb98deb42b7dbce30abb8425f": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "5 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 5",
            "subsampling": "111111",
        },
    ],
    "145bfd5481e99e18c4c3707228557fa5": [
        {
            "description": "Apple QuickTime, " "Quality 700 (68%)",
            "subsampling": "221111",
        }
    ],
    "145c52a48a9b2e954e785c3f8df5c27e": [
        {"description": "Apple QuickTime, " "Quality 385 (38%)", "subsampling": "11"}
    ],
    "147598404233439485574200e253f88e": [
        {"description": "ACD Systems Digital " "Imaging, Quality 57", "subsampling": ""}
    ],
    "1487f0cfc64949393aee2eab71b6b72c": [
        {"description": "Apple QuickTime, " "Quality 810 (79%)", "subsampling": "11"}
    ],
    "14a352b80a350e2df6b2bc444ccc74f6": [
        {
            "description": "Apple QuickTime, " "Quality 907-908 (89%)",
            "subsampling": "11",
        }
    ],
    "14a5534e4216458662a43101d56d84c8": [
        {
            "description": "Apple QuickTime, " "Quality 666 (65%)",
            "subsampling": "221111",
        }
    ],
    "14afe9b58e0eacef42db61e1d7fdd09c": [
        {
            "description": "ACD Systems Digital " "Imaging, Quality 55 or " "56",
            "subsampling": "",
        }
    ],
    "14b57dc6d5381fd0a743c7bd8b28bed1": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 68", "subsampling": ""}
    ],
    "14b7d58b539ad8d6f1c4f8fd82c91358": [
        {
            "description": "Apple QuickTime, " "Quality 284 (28%)",
            "subsampling": "221111",
        }
    ],
    "14c62682032efe8dc2de80c9330c6206": [
        {
            "description": "Apple QuickTime, " "Quality 871-872 (85%)",
            "subsampling": "211111",
        }
    ],
    "14efb0bb5124910a37bcbd5f06de9aa9": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 13", "subsampling": ""}
    ],
    "151731e5cd38be847f4dad794c023a69": [
        {"description": "Apple QuickTime, " "Quality 361 (35%)", "subsampling": "11"}
    ],
    "151d7cd5a95929d45c6790beb87705fe": [
        {
            "description": "Apple QuickTime, " "Quality 858 (84%)",
            "subsampling": "211111",
        }
    ],
    "153196d4f99569f9bbd3fe0e96d2909c": [
        {"description": "Apple QuickTime, " "Quality 679 (66%)", "subsampling": "11"}
    ],
    "153a6f0994d16003aa4f1112e6757467": [
        {
            "description": "Apple QuickTime, " "Quality 625 (61%)",
            "subsampling": "221111",
        }
    ],
    "15de51ede231cfbe123daa42a1a46070": [
        {
            "description": "Apple QuickTime, " "Quality 811-813 (79%)",
            "subsampling": "211111",
        }
    ],
    "15e1d2321b96b355d4ad109a8d2fe882": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 99",
            "subsampling": "111111",
        }
    ],
    "15f375a620952738ff21ff4aa496b8f7": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 86", "subsampling": ""}
    ],
    "163be99e863436e9b3d32615785ec8e1": [
        {
            "description": "Apple QuickTime, " "Quality 445 (43%)",
            "subsampling": "221111",
        }
    ],
    "167959a11aff7940df84ed9f3379ed0a": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "73",
            "subsampling": "",
        }
    ],
    "16b6c2d8688113b1a28afbbc57f46f80": [
        {
            "description": "Apple QuickTime, " "Quality 532-533 (52%)",
            "subsampling": "221111",
        }
    ],
    "16c443478b9417d44893f8748d49b790": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 50",
            "subsampling": "221111",
        }
    ],
    "16de07616490b8439576d837c74aefbe": [
        {
            "description": "Apple QuickTime, " "Quality 332 (32%)",
            "subsampling": "221111",
        }
    ],
    "16df79eb7c5f062aeebde385fbce1553": [
        {"description": "Apple QuickTime, " "Quality 477 (47%)", "subsampling": "11"}
    ],
    "1727e720300403e5f315b5e17ef84d3f": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 39",
            "subsampling": "221111",
        }
    ],
    "17479c1e73d2c062872c871db80d949b": [
        {"description": "ACD Systems Digital " "Imaging, Quality 58", "subsampling": ""}
    ],
    "17782e930dc2cba42da909d95278fe9b": [
        {
            "description": "Apple QuickTime, " "Quality 268 (26%)",
            "subsampling": "221111",
        }
    ],
    "178aa0138d7a08be081aeff794956a71": [
        {
            "description": "Apple QuickTime, " "Quality 266 (26%)",
            "subsampling": "221111",
        }
    ],
    "1799a236c36da0b30729d9005ca7c7f9": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "19 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 19",
            "subsampling": "111111",
        },
    ],
    "17a77c2574ff5b72b3284f57977187f3": [
        {"description": "Pentax K10D (B)", "subsampling": "211111"}
    ],
    "17bce376f588ebf2b3e9002a337c239d": [
        {"description": "Nikon Capture NX, " "Quality 65", "subsampling": "211111"}
    ],
    "17cb779485969589a5c7eb07a5d53247": [
        {
            "description": "Canon EOS 1DmkIII, Fine " "(pre-production)",
            "subsampling": "211111",
        }
    ],
    "1801686a97836f690ce3d5523ffcfa9a": [
        {"description": "Apple QuickTime, " "Quality 459 (45%)", "subsampling": "11"}
    ],
    "18392b08bf8cf788a579f376297c3334": [
        {"description": "Nikon Capture NX, " "Quality 20", "subsampling": "221111"}
    ],
    "184d01e77f6239f63fd6ab6d36761e64": [
        {
            "description": "Apple QuickTime, " "Quality 900-901 (88%)",
            "subsampling": "11",
        }
    ],
    "185893c53196f6156d458a84e1135c43": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "0 or 1 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 1",
            "subsampling": "111111",
        },
    ],
    "18593e50c21c8ad521b30933ef7479b1": [
        {
            "description": "Apple QuickTime, " "Quality 627 (61%)",
            "subsampling": "221111",
        }
    ],
    "1860106097672532e7ebc2026d7f9681": [
        {"description": "Nikon Capture NX, " "Quality 93", "subsampling": "111111"},
        {
            "description": "ACD Systems Digital " "Imaging, Quality 95 or " "96",
            "subsampling": "",
        },
    ],
    "186948d91ea43a64f874ebb9dee44564": [
        {"description": "Apple QuickTime, " "Quality 370 (36%)", "subsampling": "11"}
    ],
    "18836b72e5399e2a19cd6420562ab1ff": [
        {
            "description": "Apple QuickTime, " "Quality 428 (42%)",
            "subsampling": "221111",
        }
    ],
    "18c10ea6fe5918e09daf1a3a7a74e678": [
        {"description": "Apple QuickTime, " "Quality 496 (48%)", "subsampling": "11"}
    ],
    "18e3ac85da74fe92ab5da3d5f7614e09": [
        {"description": "Apple QuickTime, " "Quality 586 (57%)", "subsampling": "11"}
    ],
    "18fa29d1164984883a6af76377b60d5a": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "43 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 43",
            "subsampling": "111111",
        },
    ],
    "18fce3103e312ce26252ec4af6cd1350": [
        {"description": "Apple QuickTime, " "Quality 724 (71%)", "subsampling": "11"}
    ],
    "190a54eb1127ee87231795bc3d661b5a": [
        {
            "description": "Apple QuickTime, " "Quality 944-946 (92%)",
            "subsampling": "11",
        }
    ],
    "193ace8d9e274bb9188b1a9a7bdee777": [
        {
            "description": "Apple QuickTime, " "Quality 871-872 (85%)",
            "subsampling": "11",
        }
    ],
    "198f3a32e4036d7c37fbc0c343d883af": [
        {"description": "Apple QuickTime, " "Quality 590 (58%)", "subsampling": "11"}
    ],
    "19c03533b9b2e3304a0b02d9b1054497": [
        {
            "description": "Apple QuickTime, " "Quality 658 (64%)",
            "subsampling": "221111",
        }
    ],
    "19c5c7c0270bd36c49f695475a62c293": [
        {"description": "Apple QuickTime, " "Quality 580 (57%)", "subsampling": "11"}
    ],
    "19ceef79e864691318beea6502ddc3e1": [
        {
            "description": "Apple QuickTime, " "Quality 701 (68%)",
            "subsampling": "221111",
        }
    ],
    "1a0487e7e1a8f4ade97b2e8a4cab46ec": [
        {"description": "Apple QuickTime, " "Quality 747 (73%)", "subsampling": "11"}
    ],
    "1a603cba63dbba0d0815fc7319271b93": [
        {
            "description": "Apple QuickTime, " "Quality 934-936 (91%)",
            "subsampling": "11",
        }
    ],
    "1a7da03994ee019a30dbd37117761467": [
        {
            "description": "Apple QuickTime, " "Quality 952-954 (93%)",
            "subsampling": "211111",
        }
    ],
    "1aa58cb85dda84de2ddf436667124dcd": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "29 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 29",
            "subsampling": "111111",
        },
    ],
    "1acceb7ae4f9edbb835006d97ca30094": [
        {"description": "Apple QuickTime, " "Quality 410 (40%)", "subsampling": "11"}
    ],
    "1ae782c12797f5e5c9b083099148e43a": [
        {"description": "Apple QuickTime, " "Quality 870 (85%)", "subsampling": "11"}
    ],
    "1aee684c7eb75320d988f6296c4c16ea": [
        {"description": "Pentax K10D (C)", "subsampling": "211111"}
    ],
    "1b8d04b1d56a4c0c811a0d3a68e86d06": [
        {"description": "Panasonic DMC-FZ50, " "High (B)", "subsampling": "211111"}
    ],
    "1b9e7e39831b05b058025ae0a7482d44": [
        {
            "description": "Apple QuickTime, " "Quality 572 (56%)",
            "subsampling": "221111",
        }
    ],
    "1bca645051a125cd2c3af262074f70e7": [
        {
            "description": "Apple QuickTime, " "Quality 337 (33%)",
            "subsampling": "221111",
        }
    ],
    "1bdac971e8cddd198ad3123849370037": [
        {
            "description": "Apple QuickTime, " "Quality 613 (60%)",
            "subsampling": "221111",
        }
    ],
    "1bf7a5d7477ad75b9c7b281de622d53b": [
        {"description": "Apple QuickTime, " "Quality 655 (64%)", "subsampling": "11"}
    ],
    "1c19e4fde384a33f208074c73775d990": [
        {
            "description": "Apple QuickTime, " "Quality 861-863 (84%)",
            "subsampling": "11",
        }
    ],
    "1c4c74ccc581b11050cfe18792246e5e": [
        {
            "description": "Apple QuickTime, " "Quality 816 (80%)",
            "subsampling": "211111",
        }
    ],
    "1c78c0daaa0bbfd4a1678b5569b0fa13": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 1", "subsampling": ""}
    ],
    "1c87cb13f4b7a5ed45b09fc4f0e52d68": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "32",
            "subsampling": "",
        }
    ],
    "1c9bb67190ee64e82d3c67f7943bf4a4": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "9 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 9",
            "subsampling": "111111",
        },
    ],
    "1cbd419717a2916b53f9f504ec1167ca": [
        {
            "description": "Apple QuickTime, " "Quality 675 (66%)",
            "subsampling": "221111",
        }
    ],
    "1d069604250e871bd92a4a24c7be2bd5": [
        {
            "description": "Apple QuickTime, " "Quality 607 (59%)",
            "subsampling": "221111",
        }
    ],
    "1d099901cfe37674e4aeb2cdbddf0703": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "82",
            "subsampling": "",
        }
    ],
    "1d7ac617d70b1880be9c7ba16f96a3ec": [
        {
            "description": "Apple QuickTime, " "Quality 218 (21%)",
            "subsampling": "221111",
        }
    ],
    "1d956197da5eb19ffe8855a0e2a52c98": [
        {
            "description": "Apple QuickTime, " "Quality 279 (27%)",
            "subsampling": "221111",
        }
    ],
    "1dfb48b5955cf2a50011f52b9a05f1a4": [
        {
            "description": "Apple QuickTime, " "Quality 361 (35%)",
            "subsampling": "221111",
        }
    ],
    "1e133f4bf9f7c7c1e0accf44c0b1107d": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 96",
            "subsampling": "111111",
        }
    ],
    "1e2be0dde2c5d2216bca879a3f89c565": [
        {
            "description": "Apple QuickTime, " "Quality 277-278 (27%)",
            "subsampling": "11",
        }
    ],
    "1e400ba25fa835e2771772bbfb15b94b": [
        {"description": "FixFoto, Quality 2", "subsampling": ""}
    ],
    "1e619cbdee1f8ff196d34dad9140876f": [
        {"description": "Panasonic DMC-FZ50, " "High (C)", "subsampling": "211111"}
    ],
    "1e81ee25c96cdf46f44a9b930780f8c0": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "2",
            "subsampling": "",
        }
    ],
    "1e861ce223babf95bc795e18cbdb49d1": [
        {"description": "Nikon Capture NX, " "Quality 8", "subsampling": "221111"}
    ],
    "1e91365abfe1d9f7a008c363c834a66e": [
        {
            "description": "Apple QuickTime, " "Quality 204-205 (20%)",
            "subsampling": "221111",
        }
    ],
    "1e93645e6163af46937c35a18b55c601": [
        {"description": "Apple QuickTime, " "Quality 392 (38%)", "subsampling": "11"}
    ],
    "1ea3f373d0adf989e8416ecb11c38608": [
        {
            "description": "Apple QuickTime, " "Quality 239-240 (23%)",
            "subsampling": "221111",
        }
    ],
    "1eb8b98bef8b062e4bc10cffea2d8372": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "14",
            "subsampling": "",
        }
    ],
    "1f21bf5b7e0e79c229ef4d06fc9d3cc8": [
        {
            "description": "Apple QuickTime, " "Quality 601 (59%)",
            "subsampling": "221111",
        }
    ],
    "1f5e87bec674bdd7dff166c2ea9ca004": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 99", "subsampling": ""}
    ],
    "1fab112b17e94f53e94a9208e9091b7b": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 51", "subsampling": ""}
    ],
    "1fb4c8af2d70cdeecab3fd9fc882e0ce": [
        {
            "description": "Apple QuickTime, " "Quality 558 (54%)",
            "subsampling": "221111",
        }
    ],
    "1ff8f5ff33353a3ee0b6dc8fbb6321a0": [
        {
            "description": "Apple QuickTime, " "Quality 665 (65%)",
            "subsampling": "221111",
        }
    ],
    "200107bc0174104bbf1d4653c4b05058": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "17 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 17",
            "subsampling": "111111",
        },
    ],
    "204b111d4aaa85b430e86273a63fd004": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 78",
            "subsampling": "111111",
        }
    ],
    "205d4a597e68f2da78137e52f39d2728": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "3",
            "subsampling": "",
        }
    ],
    "20c7942ddec30475a182cb281f12bc03": [
        {"description": "Apple QuickTime, " "Quality 473 (46%)", "subsampling": "11"}
    ],
    "20d4b3c9e3c292c68181974704fe5048": [
        {
            "description": "Apple QuickTime, " "Quality 672-673 (66%)",
            "subsampling": "11",
        }
    ],
    "20f37f34a9fd18089aa58fe77493a7b7": [
        {
            "description": "Apple QuickTime, " "Quality 225 (22%)",
            "subsampling": "221111",
        }
    ],
    "20f79a557d4edb1917d243d00a7a9ba8": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "34",
            "subsampling": "",
        }
    ],
    "20f7b70185f4b324a8451ac4657c1d66": [
        {
            "description": "Apple QuickTime, " "Quality 614 (60%)",
            "subsampling": "221111",
        }
    ],
    "2101fdf5c6f6e92943bc16ccf8aa46a8": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "56",
            "subsampling": "",
        }
    ],
    "2129ee2bff47bfa8a8bb79ea9fb67b92": [
        {"description": "Apple QuickTime, " "Quality 597 (58%)", "subsampling": "11"}
    ],
    "2183a6f77fe72f5c70726244dcabc963": [
        {
            "description": "Apple QuickTime, " "Quality 242-243 (24%)",
            "subsampling": "221111",
        }
    ],
    "21aa1a0036251eecfffd24e37d7ce3dd": [
        {"description": "ACD Systems Digital " "Imaging, Quality 93", "subsampling": ""}
    ],
    "21c9f9a0ff71d4528ef7a19d2cfd0b6c": [
        {"description": "Apple QuickTime, " "Quality 631 (62%)", "subsampling": "11"}
    ],
    "21db4122ad8183006542018e53e0c653": [
        {
            "description": "Apple QuickTime, " "Quality 394 (38%)",
            "subsampling": "221111",
        }
    ],
    "21f8a4a67742edcde0ac854522028c9f": [
        {
            "description": "Apple QuickTime, " "Quality 399 (39%)",
            "subsampling": "221111",
        }
    ],
    "2200d1873e51bf812bdcb57c10c6c14b": [
        {
            "description": "Apple QuickTime, " "Quality 195-196 (19%)",
            "subsampling": "11",
        }
    ],
    "222a8769205a592ec834b6f5fc654a21": [
        {"description": "ACD Systems Digital " "Imaging, Quality 13", "subsampling": ""}
    ],
    "2234156f0550a047700c2a08459c8242": [
        {
            "description": "Apple QuickTime, " "Quality 728 (71%)",
            "subsampling": "221111",
        }
    ],
    "226788e417078cdcc5aa989379b9e824": [
        {
            "description": "Apple QuickTime, " "Quality 404 (39%)",
            "subsampling": "221111",
        }
    ],
    "2273274a8d695da4bebff145cbcbafcc": [
        {"description": "Apple QuickTime, " "Quality 308 (30%)", "subsampling": "11"}
    ],
    "22944c3bc03d6adea8d6819f914452c3": [
        {"description": "FixFoto, Quality 15", "subsampling": ""}
    ],
    "22b5f11b635ea5484469708cd7e6e3d9": [
        {
            "description": "Apple QuickTime, " "Quality 592 (58%)",
            "subsampling": "221111",
        }
    ],
    "22c77ec6f4e8f75d48f98473abe62e59": [
        {
            "description": "Apple QuickTime, " "Quality 904-905 (88%)",
            "subsampling": "211111",
        }
    ],
    "22ccf9c976b36da34f48385a09b1951b": [
        {
            "description": "Apple QuickTime, " "Quality 1021-1023 " "(100%)",
            "subsampling": "11",
        }
    ],
    "233ed690eb7e9008c20ed16e79aa3eb5": [
        {"description": "ACD Systems Digital " "Imaging, Quality 8", "subsampling": ""}
    ],
    "234c9cf6d7fe671b52c3ec5a20046ec8": [
        {"description": "Apple QuickTime, " "Quality 507 (50%)", "subsampling": "11"}
    ],
    "234d8f310d75effc9f77beb1d3847f49": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 100",
            "subsampling": "111111",
        }
    ],
    "2358594d2a85b48dc0bd03e024dec9bd": [
        {"description": "Apple QuickTime, " "Quality 352 (34%)", "subsampling": "11"}
    ],
    "23816ed847127a41e3c7f52e04072e41": [
        {
            "description": "Apple QuickTime, " "Quality 468 (46%)",
            "subsampling": "221111",
        }
    ],
    "23822cafcc61ce2a52691f1fc963ff18": [
        {"description": "Apple QuickTime, " "Quality 497 (49%)", "subsampling": "11"}
    ],
    "23a59c4f9ec045faf9f8379b3ca302bb": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "99 (Grayscale)",
            "subsampling": "11",
        }
    ],
    "23ab27876006666358e95d9c1104bcd0": [
        {"description": "Apple QuickTime, " "Quality 381 (37%)", "subsampling": "11"}
    ],
    "23bd5edb6224e03e2f7c282e04986553": [
        {
            "description": "Apple QuickTime, " "Quality 64-80 (6-8%)",
            "subsampling": "221111",
        }
    ],
    "23f2a5970523c5f7fd2ab7fa3b09dff9": [
        {
            "description": "Pentax Optio " "550/555/M20/M30/W10/W20, " "Best",
            "subsampling": "211111",
        }
    ],
    "23f2bd2d96ec531815609503dae4a2b0": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 44",
            "subsampling": "221111",
        }
    ],
    "240fffe5f8e2d8f3345b8175f9cb0a40": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 70",
            "subsampling": "111111",
        }
    ],
    "24406aee81b89ea50881ae71f878d0ec": [
        {"description": "Apple QuickTime, " "Quality 445 (43%)", "subsampling": "11"}
    ],
    "2444e1c407a9965fb5ea2dafd269911f": [
        {
            "description": "Apple QuickTime, " "Quality 322-324 " "(31-32%)",
            "subsampling": "11",
        }
    ],
    "2457f78378c5efdac8e1ef619a4285cd": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "33",
            "subsampling": "",
        }
    ],
    "24784b5651e1790242c01de522a6e05b": [
        {"description": "Apple QuickTime, " "Quality 470 (46%)", "subsampling": "11"}
    ],
    "24ec8f0996e5e8d4dd7019d2b6063290": [
        {"description": "Apple QuickTime, " "Quality 783 (76%)", "subsampling": "11"}
    ],
    "24f95056dce30d11bad39b33ab271262": [
        {
            "description": "Apple QuickTime, " "Quality 833-834 (81%)",
            "subsampling": "211111",
        }
    ],
    "24fff8dcfdc8640225fff020ad869c18": [
        {
            "description": "Apple QuickTime, " "Quality 339 (33%)",
            "subsampling": "221111",
        }
    ],
    "2501aad23cdf94b25c6df0ab6984b6e0": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 24",
            "subsampling": "221111",
        }
    ],
    "2502314c1b957a0e4f911d17db770a01": [
        {"description": "Apple QuickTime, " "Quality 284 (28%)", "subsampling": "11"}
    ],
    "251eb2d7903f63b168348ec483ba499a": [
        {"description": "Nikon Capture NX, " "Quality 70", "subsampling": "211111"}
    ],
    "252482232ff1c8cf77db4f0c6402f858": [
        {
            "description": "Canon Digital Photo " "Professional, Quality 1",
            "subsampling": "211111",
        }
    ],
    "252ba8a31aeb601e23b3a70f9af7abc1": [
        {"description": "Apple QuickTime, " "Quality 628 (61%)", "subsampling": "11"}
    ],
    "253467dc35dfbb32cb3d619fc635d689": [
        {"description": "Pentax Optio V20/W60, " "Best", "subsampling": "211111"}
    ],
    "2535e621267a9ff2e2d09148643e3389": [
        {
            "description": "Apple QuickTime, " "Quality 102-109 " "(10-11%)",
            "subsampling": "221111",
        }
    ],
    "25497c83113bd738e89d91bd48d7086c": [
        {
            "description": "Apple QuickTime, " "Quality 638 (62%)",
            "subsampling": "221111",
        }
    ],
    "2557828257dd798ad636df350c685a26": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "88",
            "subsampling": "",
        }
    ],
    "256e617be51dade18503fcbbe87cd4a6": [
        {
            "description": "ACD Systems Digital " "Imaging, Quality 50 or " "51",
            "subsampling": "",
        }
    ],
    "259764d950c1f1e399cdb27e159c8985": [
        {
            "description": "Apple QuickTime, " "Quality 921-922 (90%)",
            "subsampling": "11",
        }
    ],
    "25b45d6c1668613a61b81c6b60fa158a": [
        {"description": "Apple QuickTime, " "Quality 841 (82%)", "subsampling": "11"}
    ],
    "25ca43baa972ad9c82128606cd383805": [
        {"description": "Apple QuickTime, " "Quality 955 (93%)", "subsampling": "11"}
    ],
    "25e399a9cf70fe7a13867b40ac2c3416": [
        {
            "description": "Apple QuickTime, " "Quality 155-157 (15%)",
            "subsampling": "221111",
        }
    ],
    "25eb3d27e65659435a89e401edfab65f": [
        {
            "description": "Apple QuickTime, " "Quality 158-161 " "(15-16%)",
            "subsampling": "221111",
        }
    ],
    "26005cdf9397dcce883660aeecb0426b": [
        {"description": "Apple QuickTime, " "Quality 902 (88%)", "subsampling": "11"}
    ],
    "261bdba7fe6d8bca5302e4e93b52c1fb": [
        {
            "description": "Apple QuickTime, " "Quality 968-970 (95%)",
            "subsampling": "211111",
        }
    ],
    "26831dfc8d0dc1d202d50d6cf7b4f4a4": [
        {
            "description": "Apple QuickTime, " "Quality 327 (32%)",
            "subsampling": "221111",
        }
    ],
    "26d087368a13e3aca9ca13a54bcc648f": [
        {
            "description": "Apple QuickTime, " "Quality 752-753 " "(73-74%)",
            "subsampling": "11",
        }
    ],
    "2706b8b0cf6686148e285b6d3e44dd72": [
        {"description": "Nikon Capture NX, " "Quality 75", "subsampling": "211111"}
    ],
    "27297008a89ee49804f0859ea6435878": [
        {"description": "Pentax Optio MX, Best", "subsampling": "211111"}
    ],
    "272b5b12f7701be4cceba51e9d5dbf13": [
        {
            "description": "Apple QuickTime, " "Quality 321 (31%)",
            "subsampling": "221111",
        }
    ],
    "2733a3cb2e0a2313b74d686437fa3ae2": [
        {"description": "Apple QuickTime, " "Quality 435 (42%)", "subsampling": "11"}
    ],
    "27472e3714251402d5509438505611c3": [
        {
            "description": "Adobe Lightroom, " "Quality 62% - 69%",
            "subsampling": "111111",
        }
    ],
    "2748fa249a86361b1b5f0662a88abdb3": [
        {
            "description": "Apple QuickTime, " "Quality 477 (47%)",
            "subsampling": "221111",
        }
    ],
    "274bbeb0ac3939f90c578ebb1f5a9eef": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "85 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 85",
            "subsampling": "111111",
        },
    ],
    "2750f3df7a97d6007d6a17f5dd27790a": [
        {"description": "Apple QuickTime, " "Quality 749 (73%)", "subsampling": "11"}
    ],
    "276da99e50e1b39134e13826789d655e": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 43",
            "subsampling": "221111",
        }
    ],
    "277982593a55786fe424c80a17224cd7": [
        {"description": "Apple QuickTime, " "Quality 335 (33%)", "subsampling": "11"}
    ],
    "27811b28d02bd417857904f0a9e1ed58": [
        {"description": "Nikon Capture NX, " "Quality 17", "subsampling": "221111"}
    ],
    "27c301566e155f700b01906a43473ffe": [
        {"description": "Nikon Capture NX, " "Quality 44", "subsampling": "221111"}
    ],
    "27e6ed2cecfebe31eb3d66128c926562": [
        {"description": "Apple QuickTime, " "Quality 515 (50%)", "subsampling": "11"}
    ],
    "280205c47c8d3706c2f36b1986e9b149": [
        {
            "description": "ACD Systems Digital " "Imaging, Quality 40 or " "41",
            "subsampling": "",
        }
    ],
    "281c39340554f672ff62c65e0bf1036b": [
        {"description": "Apple QuickTime, " "Quality 339 (33%)", "subsampling": "11"}
    ],
    "281f65a19e5de33d9ff5f3afeda06973": [
        {
            "description": "Apple QuickTime, " "Quality 236-237 (23%)",
            "subsampling": "11",
        }
    ],
    "2821aae8108df4bd98e5eaa451a351d2": [
        {"description": "Apple QuickTime, " "Quality 517 (50%)", "subsampling": "11"}
    ],
    "282914c43bab6e5c62f3caaf549f1510": [
        {
            "description": "Apple QuickTime, " "Quality 789-790 (77%)",
            "subsampling": "11",
        }
    ],
    "284efada45882694778e65969f761478": [
        {
            "description": "Apple QuickTime, " "Quality 317 (31%)",
            "subsampling": "221111",
        }
    ],
    "2851eea5e15f1b977c1496a77c884b4f": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "75",
            "subsampling": "",
        }
    ],
    "285bdd58fac87b174a22d2a93d69cd7c": [
        {
            "description": "Apple QuickTime, " "Quality 770 (75%)",
            "subsampling": "211111",
        }
    ],
    "28782f5ee24fe983fe90b9438b39ae2e": [
        {"description": "Pentax Optio S4, Best", "subsampling": "221111"}
    ],
    "28cdbc95898e02dd0ffc45ba48596ca7": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 33",
            "subsampling": "221111",
        }
    ],
    "28f718af4edb0069a1fdab00f6ea978d": [
        {"description": "Apple QuickTime, " "Quality 677 (66%)", "subsampling": "11"}
    ],
    "2916d9453b885ee4123e6e3ee94ccbc7": [
        {
            "description": "Apple QuickTime, " "Quality 669-671 " "(65-66%)",
            "subsampling": "221111",
        }
    ],
    "2926d6bf5a27174bd9057bd6198413cd": [
        {
            "description": "Apple QuickTime, " "Quality 310 (30%)",
            "subsampling": "221111",
        }
    ],
    "292b83b37765408b65f496cddd3f96ea": [
        {"description": "ACD Systems Digital " "Imaging, Quality 43", "subsampling": ""}
    ],
    "2941d12ef34511d96b659ba30d682cd1": [
        {"description": "Pentax K10D (AT)", "subsampling": "211111"}
    ],
    "29572be1991c210fabacaeb658a74844": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "44",
            "subsampling": "",
        }
    ],
    "295cb1e2772312ba5cd546966d1aa70d": [
        {
            "description": "Apple QuickTime, " "Quality 507 (50%)",
            "subsampling": "221111",
        }
    ],
    "29a9ee0cae41784d90fa74d7cd240a3e": [
        {
            "description": "Apple QuickTime, " "Quality 301 (29%)",
            "subsampling": "221111",
        }
    ],
    "29b74834ce7570b9c175d0200e75316e": [
        {
            "description": "Apple QuickTime, " "Quality 248-249 (24%)",
            "subsampling": "11",
        }
    ],
    "29b7cdc7a570b950457d20541c22c4ce": [
        {"description": "Apple QuickTime, " "Quality 610 (60%)", "subsampling": "11"}
    ],
    "29c42d951dc84d62bd134bec71bf731b": [
        {"description": "Apple QuickTime, " "Quality 958 (94%)", "subsampling": "11"}
    ],
    "29f957e2a0af0f44d271c3c4e27eec4b": [
        {"description": "ACD Systems Digital " "Imaging, Quality 14", "subsampling": ""}
    ],
    "2a1b83345108443a090cdab4c83143fb": [
        {
            "description": "Apple QuickTime, " "Quality 710 (69%)",
            "subsampling": "221111",
        }
    ],
    "2a6a136faaf1f13c2b80dcb4786d90b2": [
        {"description": "Apple QuickTime, " "Quality 487 (48%)", "subsampling": "11"}
    ],
    "2a7ec778642b15b8bce238f7b63ef537": [
        {
            "description": "Apple QuickTime, " "Quality 527 (51%)",
            "subsampling": "221111",
        }
    ],
    "2a8e27e03b6e1555335c91231c452bba": [
        {
            "description": "Apple QuickTime, " "Quality 517 (50%)",
            "subsampling": "221111",
        }
    ],
    "2a98c0b884281080eefcdf98dd33fd6b": [
        {
            "description": "Apple QuickTime, " "Quality 208-209 (20%)",
            "subsampling": "221111",
        }
    ],
    "2a9ae394dc32a418960522cbe9c6df24": [
        {"description": "Nikon Capture NX, " "Quality 63", "subsampling": "211111"}
    ],
    "2aa82b6717f1cdfe6b6d60a4486b5671": [
        {"description": "Pentax K10D (AU)", "subsampling": "211111"},
        {"description": "Pentax K10D (AV)", "subsampling": "211111"},
    ],
    "2ab2f6a116ca6fc0bbf188b19b9de967": [
        {
            "description": "ACD Systems Digital " "Imaging, Quality 0 or 1",
            "subsampling": "",
        }
    ],
    "2abebf7a61009c5c1aa9516539b9084e": [
        {"description": "Apple QuickTime, " "Quality 594 (58%)", "subsampling": "11"}
    ],
    "2ac28889e4ad4724d49f8b4c36b0cece": [
        {
            "description": "Apple QuickTime, " "Quality 242-243 (24%)",
            "subsampling": "11",
        }
    ],
    "2b1dba266c728a9f46d06e6e5c247953": [
        {"description": "Apple Aperture Quality " "5", "subsampling": "221111"}
    ],
    "2b3262e10b1563600a5f0738fec342ed": [
        {
            "description": "Apple QuickTime, " "Quality 506 (49%)",
            "subsampling": "221111",
        }
    ],
    "2b394105d4dd418e79b32e66496679d4": [
        {"description": "Apple QuickTime, " "Quality 667 (65%)", "subsampling": "11"}
    ],
    "2b7a6a83259aa9967e098d3e70f1ee09": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 59",
            "subsampling": "111111",
        }
    ],
    "2b81eecf0fecd33679adac27e79ef3f4": [
        {
            "description": "Apple QuickTime, " "Quality 640-641 (63%)",
            "subsampling": "11",
        }
    ],
    "2bafe4b75b8a105d72e981b21fe3b6cf": [
        {
            "description": "Apple QuickTime, " "Quality 540 (53%)",
            "subsampling": "221111",
        }
    ],
    "2bf57fbe54370c4d917f259631af033e": [
        {"description": "Apple QuickTime, " "Quality 574 (56%)", "subsampling": "11"}
    ],
    "2bf80ea6a878f7ecb88ea827b58c98f8": [
        {
            "description": "Apple QuickTime, " "Quality 985-987 (96%)",
            "subsampling": "211111",
        }
    ],
    "2bfe0ace876b80be6f601a1703187d94": [
        {"description": "Apple QuickTime, " "Quality 521 (51%)", "subsampling": "11"}
    ],
    "2c2726484978a15d3d756d43b0baa290": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 31", "subsampling": ""}
    ],
    "2c4a4cb841ee92aa3a2b4c93467ba7a8": [
        {
            "description": "Apple QuickTime, " "Quality 654 (64%)",
            "subsampling": "221111",
        }
    ],
    "2c6581e20fa5393b3dd4d58f0df01957": [
        {
            "description": "Apple QuickTime, " "Quality 822-824 (80%)",
            "subsampling": "11",
        }
    ],
    "2cba6ba1aede8c791ada1acaba8c162e": [
        {"description": "Apple QuickTime, " "Quality 306 (30%)", "subsampling": "11"}
    ],
    "2d2a77bf6078ab4f07261c76b637b597": [
        {
            "description": "Apple QuickTime, " "Quality 351 (34%)",
            "subsampling": "221111",
        }
    ],
    "2d387641f4e94b6986908b3770fb762e": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 84",
            "subsampling": "111111",
        }
    ],
    "2d719cb263e284fc8621bbec1fe52cd5": [
        {
            "description": "Apple QuickTime, " "Quality 447 (44%)",
            "subsampling": "221111",
        }
    ],
    "2d7eb8eb9df9f4831a843626f4fc7e19": [
        {"description": "Apple QuickTime, " "Quality 555 (54%)", "subsampling": "11"}
    ],
    "2da67fe5f0bb3c8b10403295895fb154": [
        {"description": "Apple QuickTime, " "Quality 537 (52%)", "subsampling": "11"}
    ],
    "2dffe433bbb9c81b05e569afd3d9b585": [
        {
            "description": "Apple QuickTime, " "Quality 853 (83%)",
            "subsampling": "211111",
        }
    ],
    "2e420a34dcf01dab91fd8509d4dbaab5": [
        {"description": "Apple QuickTime, " "Quality 396 (39%)", "subsampling": "11"}
    ],
    "2eae93ed601a50284ee31c20651584cb": [
        {"description": "Apple QuickTime, " "Quality 664 (65%)", "subsampling": "11"}
    ],
    "2ec2d5c10641952fce5c435b331b8872": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 63",
            "subsampling": "111111",
        }
    ],
    "2ec3d0ec37690e40f009b7a9f9b17c49": [
        {
            "description": "Apple QuickTime, " "Quality 420 (41%)",
            "subsampling": "221111",
        }
    ],
    "2edccd94198ab5a459a8396d9a0be4aa": [
        {
            "description": "Apple QuickTime, " "Quality 962 (94%)",
            "subsampling": "211111",
        }
    ],
    "2f2101a8450c617a09ccad472c275b88": [
        {
            "description": "Apple QuickTime, " "Quality 434 (42%)",
            "subsampling": "221111",
        }
    ],
    "2fbbcce5a035d6215e4851a0ae63481f": [
        {
            "description": "Apple QuickTime, " "Quality 372 (36%)",
            "subsampling": "221111",
        }
    ],
    "2fff3c6e48247992d1543d9e5c679759": [
        {"description": "Nikon Capture NX, " "Quality 54", "subsampling": "221111"}
    ],
    "301158b292e3232856a765486da26fa6": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 10",
            "subsampling": "221111",
        }
    ],
    "302ff1ad1a50d0f01a82cc88f286c649": [
        {"description": "FixFoto, Quality 3", "subsampling": ""}
    ],
    "303663905d055b77bb547fe0b0beb9c5": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "76 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 76",
            "subsampling": "111111",
        },
    ],
    "3050624718ce9acc06f85c2fa0208cc7": [
        {
            "description": "Apple QuickTime, " "Quality 294 (29%)",
            "subsampling": "221111",
        }
    ],
    "307c47179fdad179b5f962228c115db8": [
        {
            "description": "Apple QuickTime, " "Quality 554 (54%)",
            "subsampling": "221111",
        }
    ],
    "30be130aa27d0b91d6f55ed9b1cd6c84": [
        {
            "description": "Apple QuickTime, " "Quality 488 (48%)",
            "subsampling": "221111",
        }
    ],
    "30d7b6db02954dfc4ce47a089d0f40d9": [
        {"description": "Nikon Capture NX, " "Quality 73", "subsampling": "211111"}
    ],
    "310b70bc4fac884f64a07040a4b87468": [
        {"description": "Pentax Optio S, Best " "(C)", "subsampling": "221111"}
    ],
    "312e047b5d9076cd1e126f3dbce928e5": [
        {
            "description": "Apple QuickTime, " "Quality 771 (75%)",
            "subsampling": "211111",
        }
    ],
    "31365833a4d7d0ef2c1db9b90e515f7f": [
        {
            "description": "Apple QuickTime, " "Quality 959-961 (94%)",
            "subsampling": "211111",
        }
    ],
    "315e7fee22864b37b1b7670957f259fe": [
        {"description": "Apple QuickTime, " "Quality 390 (38%)", "subsampling": "11"}
    ],
    "315f4faadd967e72d730155091c4912f": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 38", "subsampling": ""}
    ],
    "31697e4b294a13e35ab8d55d3a9612ca": [
        {
            "description": "Apple QuickTime, " "Quality 1018-1020 " "(99-100%)",
            "subsampling": "211111",
        }
    ],
    "318081abf5329c90d984c2214d69f097": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "59",
            "subsampling": "",
        }
    ],
    "3184b71ca26bfe0c80811cf10423fa92": [
        {
            "description": "Apple QuickTime, " "Quality 521 (51%)",
            "subsampling": "221111",
        }
    ],
    "31852b7659883eade6e273ac61ef0262": [
        {"description": "Apple QuickTime, " "Quality 721 (70%)", "subsampling": "11"}
    ],
    "31e214243395b008048469d4bc4dc780": [
        {
            "description": "Apple QuickTime, " "Quality 778 (76%)",
            "subsampling": "211111",
        }
    ],
    "31f288945896ed839f1d936bff06fb03": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "41 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 41",
            "subsampling": "111111",
        },
    ],
    "3233b63fc39fbbaa9af364e8a33862ff": [
        {"description": "ACD Systems Digital " "Imaging, Quality 94", "subsampling": ""}
    ],
    "32386501afff88b45432b23fe41593e8": [
        {"description": "Pentax K10D (D)", "subsampling": "211111"}
    ],
    "32682ece28c3bee7754fde6fec109b47": [
        {
            "description": "Apple QuickTime, " "Quality 975-977 (95%)",
            "subsampling": "211111",
        }
    ],
    "326bd5938e2db7de9250a9fb0efc6692": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 78", "subsampling": ""}
    ],
    "326c33f64f96592487d2bfdd198738bf": [
        {
            "description": "Apple QuickTime, " "Quality 664 (65%)",
            "subsampling": "221111",
        }
    ],
    "32757023bb5e7f703acf737a5a29c9d6": [
        {
            "description": "Apple QuickTime, " "Quality 785-786 (77%)",
            "subsampling": "211111",
        }
    ],
    "327f47dd8f999b2bbb3bb25c43cf5be5": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "12 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 12",
            "subsampling": "111111",
        },
    ],
    "328ab751ea48f5a8bc7c4b8628138ce0": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 41",
            "subsampling": "221111",
        }
    ],
    "32aa33dc6de46b7c5c5948b0ae06cb0e": [
        {"description": "Apple QuickTime, " "Quality 769 (75%)", "subsampling": "11"}
    ],
    "32eb803f68d72719267a1313548e7180": [
        {
            "description": "Apple QuickTime, " "Quality 478 (47%)",
            "subsampling": "221111",
        }
    ],
    "33113dc71a90e8db06b43dadfe36b020": [
        {"description": "Apple QuickTime, " "Quality 764 (75%)", "subsampling": "11"}
    ],
    "332d9c49c5b32ae2addbb06a1e32fd49": [
        {"description": "Apple QuickTime, " "Quality 579 (57%)", "subsampling": "11"}
    ],
    "334c67d739adf957d1620201cb7a521c": [
        {
            "description": "Apple QuickTime, " "Quality 956-957 " "(93-93%)",
            "subsampling": "11",
        }
    ],
    "336eeeb78e386bf66fe6325b4a0fcfa6": [
        {"description": "Pentax Optio A40, " "Better", "subsampling": "211111"}
    ],
    "33731f743fc28e9d81e542f0ed7cdfba": [
        {"description": "Nikon Capture NX, " "Quality 3", "subsampling": "221111"}
    ],
    "338a78a7658ff3c1de33d88aa0ab7c74": [
        {"description": "Apple QuickTime, " "Quality 659 (64%)", "subsampling": "11"}
    ],
    "3396344724a1868ada2330ebaeb9448e": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "4 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 4",
            "subsampling": "111111",
        },
    ],
    "340aeb15b2b6c05968bb2c6e3d85cbed": [
        {
            "description": "Apple QuickTime, " "Quality 162-164 (16%)",
            "subsampling": "11",
        }
    ],
    "342e3bddb81140ea9df00400a46461d7": [
        {
            "description": "Apple QuickTime, " "Quality 387 (38%)",
            "subsampling": "221111",
        }
    ],
    "34457d32b9531f04696a52969e02dc1a": [
        {
            "description": "Apple QuickTime, " "Quality 188-189 (18%)",
            "subsampling": "221111",
        }
    ],
    "34466385e7bf9b2708adf19be1eb3c2d": [
        {
            "description": "Apple QuickTime, " "Quality 897-898 (88%)",
            "subsampling": "11",
        }
    ],
    "345d210b180a45bd23b0c7931c59c263": [
        {
            "description": "Apple QuickTime, " "Quality 529 (52%)",
            "subsampling": "221111",
        }
    ],
    "348f4874d57ae6aae04ef96132374913": [
        {
            "description": "Apple QuickTime, " "Quality 134-137 (13%)",
            "subsampling": "221111",
        }
    ],
    "34a599dff2b6aaed12143938b7374f2f": [
        {
            "description": "Adobe Lightroom, " "Quality 70% - 76%",
            "subsampling": "111111",
        }
    ],
    "34b25782fc089616807bbbe7f7cd8413": [
        {"description": "Nikon Capture NX, " "Quality 67", "subsampling": "211111"}
    ],
    "34bf5c46342f2a514f8ae562e520ece0": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "63",
            "subsampling": "",
        }
    ],
    "34c0043b98d09193beda0cf5d1ada274": [
        {
            "description": "Apple QuickTime, " "Quality 499 (49%)",
            "subsampling": "221111",
        }
    ],
    "34dba33043aa5ee317b7649242e702b1": [
        {
            "description": "Apple QuickTime, " "Quality 633 (62%)",
            "subsampling": "221111",
        }
    ],
    "3521d793fd9d2d9aac85dc4f0be40290": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 1",
            "subsampling": "221111",
        }
    ],
    "3527616df6f26a3ab36b80a8d885fc07": [
        {"description": "Pentax K10D (AW)", "subsampling": "211111"},
        {"description": "Pentax K10D (AX)", "subsampling": "211111"},
        {"description": "Pentax K10D (AY)", "subsampling": "211111"},
    ],
    "353bf09900feb764885329e7bebfd95e": [
        {"description": "Pentax Optio 330GS, " "Good", "subsampling": "211111"}
    ],
    "3542444d51fa859ed5af78a1f5fc4f36": [
        {"description": "Apple QuickTime, " "Quality 354 (35%)", "subsampling": "11"}
    ],
    "35686967efa5fb333fb8f4844efc33a3": [
        {
            "description": "Canon Digital Photo " "Professional, Quality 8",
            "subsampling": "211111",
        }
    ],
    "35886289b5c8921f7932f895d7f1855d": [
        {
            "description": "Apple QuickTime, " "Quality 216-217 (21%)",
            "subsampling": "221111",
        }
    ],
    "3589227bdd85f880f3337b492e895c5d": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 74",
            "subsampling": "111111",
        }
    ],
    "359038cd7c45242e96e176e91210922d": [
        {"description": "Apple QuickTime, " "Quality 629 (61%)", "subsampling": "11"}
    ],
    "35ad02c3d8237a074b67423c39d3d61c": [
        {"description": "Pentax K10D (E)", "subsampling": "211111"}
    ],
    "35af99d11406974cf2ffa6676801b10c": [
        {
            "description": "Apple QuickTime, " "Quality 168-170 " "(16-17%)",
            "subsampling": "221111",
        }
    ],
    "35b3697c265e35185e9463aac6ce9b2d": [
        {
            "description": "Apple QuickTime, " "Quality 711-712 " "(69-70%)",
            "subsampling": "11",
        }
    ],
    "36016cd5527c505ef3bbba8b3e22f9db": [
        {"description": "Nikon Capture NX, " "Quality 99", "subsampling": "111111"}
    ],
    "3601e95d6cd507065d46b3f058229d91": [
        {
            "description": "Apple QuickTime, " "Quality 489 (48%)",
            "subsampling": "221111",
        }
    ],
    "362c3e0c08f6951018cde7b412cd513f": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 72", "subsampling": ""}
    ],
    "363b54d38094e5f2e2d63c50870ae76c": [
        {
            "description": "Apple QuickTime, " "Quality 684 (67%)",
            "subsampling": "221111",
        }
    ],
    "3654bbf4a45e0c0758a82a075b3f77cc": [
        {"description": "Nikon Capture NX, " "Quality 12", "subsampling": "221111"}
    ],
    "365693ebd558aebc31a79a1abff9709d": [
        {
            "description": "Apple QuickTime, " "Quality 743-744 (73%)",
            "subsampling": "11",
        }
    ],
    "3673ce9ec4f6f916009d39282ff3a8d7": [
        {
            "description": "Apple QuickTime, " "Quality 356 (35%)",
            "subsampling": "221111",
        }
    ],
    "367b3d63cddc0cd27e58030c2b8f1aaa": [
        {"description": "Apple QuickTime, " "Quality 511 (50%)", "subsampling": "11"}
    ],
    "369e1cfc338b45a239cb7db09778037e": [
        {
            "description": "Apple QuickTime, " "Quality 302 (29%)",
            "subsampling": "221111",
        }
    ],
    "36b2371ec6df13143af12d600232c2ab": [
        {
            "description": "Apple QuickTime, " "Quality 438 (43%)",
            "subsampling": "221111",
        }
    ],
    "36d42b031eea0c9f626f15533e72162a": [
        {
            "description": "Apple QuickTime, " "Quality 934-936 (91%)",
            "subsampling": "211111",
        }
    ],
    "36da00bae6cd81d1f97e32748c07e33f": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "97 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 97",
            "subsampling": "111111",
        },
    ],
    "36e7560256c5ffd285a1ca0f6d4bf97d": [
        {"description": "Apple QuickTime, " "Quality 379 (37%)", "subsampling": "11"}
    ],
    "36e9cb02d3ef245a3e15272c5071b0ee": [
        {"description": "Apple QuickTime, " "Quality 784 (77%)", "subsampling": "11"}
    ],
    "36f1ec430bae8e5c72af6388e2a4d807": [
        {
            "description": "Apple QuickTime, " "Quality 851-852 (83%)",
            "subsampling": "11",
        }
    ],
    "37132e8ea81137fdf26ce30926ab8100": [
        {"description": "Adobe Photoshop, " "Quality 10", "subsampling": "11"}
    ],
    "3730182602996b4a1d540eb3fd970072": [
        {"description": "Apple QuickTime, " "Quality 654 (64%)", "subsampling": "11"}
    ],
    "377a7b50c2d7484255bbbf537bf9fa86": [
        {
            "description": "Apple QuickTime, " "Quality 453 (44%)",
            "subsampling": "221111",
        }
    ],
    "37802f44dab089a35e03b94a298b19da": [
        {
            "description": "Apple QuickTime, " "Quality 522 (51%)",
            "subsampling": "221111",
        }
    ],
    "37914b5d31e7f0f13066e5292c07c305": [
        {
            "description": "Apple QuickTime, " "Quality 158-161 " "(15-16%)",
            "subsampling": "11",
        }
    ],
    "379efafa6e71a90ccfcb57073d0bc5c8": [
        {
            "description": "ACD Systems Digital " "Imaging, Quality 70 or " "71",
            "subsampling": "",
        }
    ],
    "379f9f196d4190298a732ab9a7031001": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 97", "subsampling": ""}
    ],
    "37b8bbab382a228eabb0dc64c0edcb0f": [
        {"description": "Nikon Capture NX, " "Quality 68", "subsampling": "211111"}
    ],
    "37e999828e5bc43ee4a470bf29ea97b7": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "78",
            "subsampling": "",
        }
    ],
    "3803d7f6b7aed64c658c21dbb2bc0797": [
        {"description": "Pentax Optio 330, Best", "subsampling": "221111"}
    ],
    "3806bcbefd350e8791be95dfc62bab27": [
        {
            "description": "Apple QuickTime, " "Quality 608 (59%)",
            "subsampling": "221111",
        }
    ],
    "381d1ca1d61986f28cfd6da0fca348da": [
        {
            "description": "Apple QuickTime, " "Quality 994-996 (97%)",
            "subsampling": "11",
        }
    ],
    "3841f0f3be30520a1a57f41c449588ee": [
        {"description": "Apple Aperture Quality " "4", "subsampling": "221111"}
    ],
    "387354b46b9726f33da5c0c1a0c383a0": [
        {"description": "Pentax K10D/K20D (AA)", "subsampling": "211111"}
    ],
    "389e1ca056b1bd05dd29ecaecae5b4ae": [
        {
            "description": "Apple QuickTime, " "Quality 1010-1013 (99%)",
            "subsampling": "211111",
        }
    ],
    "38a1f9d86241eb3b96d5d42bc6587598": [
        {"description": "Apple QuickTime, " "Quality 368 (36%)", "subsampling": "11"}
    ],
    "38a60cdb8033a9f90027895eab0c40ba": [
        {"description": "Apple QuickTime, " "Quality 373 (36%)", "subsampling": "11"}
    ],
    "38f26622a54ba22accac05f7c0a3b307": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 18",
            "subsampling": "221111",
        }
    ],
    "38f4d508dcf9c82d9488b42a2487b191": [
        {
            "description": "Apple QuickTime, " "Quality 596 (58%)",
            "subsampling": "221111",
        }
    ],
    "395ef59782311cd2081887c78c40c4bc": [
        {
            "description": "Apple QuickTime, " "Quality 197-198 (19%)",
            "subsampling": "11",
        }
    ],
    "3974d72e6831171ec970bbb09b9cc506": [
        {
            "description": "Apple QuickTime, " "Quality 783 (76%)",
            "subsampling": "211111",
        }
    ],
    "39d929c095f37a90e7d083db40e8642d": [
        {"description": "Pentax K10D (F)", "subsampling": "211111"}
    ],
    "3a2ab96a6ad9612e1377ddc822f02ddd": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 37", "subsampling": ""}
    ],
    "3a6cefd4f43c513fdf0858f26afeab5a": [
        {"description": "Nikon Capture NX, " "Quality 7", "subsampling": "221111"}
    ],
    "3a6eac793d818f378e7b24826c9115cc": [
        {"description": "Apple QuickTime, " "Quality 488 (48%)", "subsampling": "11"}
    ],
    "3a8a34631e388e39d13616d003f05957": [
        {"description": "FinePixViewer, Basic", "subsampling": "211111"}
    ],
    "3adf9a0b85a4000243bbf833cd8e6966": [
        {"description": "Nikon Capture NX, " "Quality 95", "subsampling": "111111"}
    ],
    "3ae705fae9e895eda345d482525215e3": [
        {"description": "Apple QuickTime, " "Quality 645 (63%)", "subsampling": "11"}
    ],
    "3af16b87c33bb2e48152e249beb9147b": [
        {
            "description": "Apple QuickTime, " "Quality 767 (75%)",
            "subsampling": "221111",
        },
        {
            "description": "Apple QuickTime, " "Quality 768 (75%)",
            "subsampling": "211111",
        },
    ],
    "3af2163438180050bbcf123d4f4587d3": [
        {"description": "Apple QuickTime, " "Quality 568 (55%)", "subsampling": "11"}
    ],
    "3b0315316de45b649bd8ba5b5471ab81": [
        {"description": "Apple QuickTime, " "Quality 314 (31%)", "subsampling": "11"}
    ],
    "3b0b5975a0e1c9d732c93e1b37a6978b": [
        {"description": "Adobe Photoshop, " "Quality 0", "subsampling": "11"}
    ],
    "3b95f11bd77cb8af977c09d5851131f8": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 41", "subsampling": ""}
    ],
    "3bb09b202acd618286d26a33f688f7c7": [
        {
            "description": "Apple QuickTime, " "Quality 602 (59%)",
            "subsampling": "221111",
        }
    ],
    "3bbfcd817441d2267a49bf76b48c5f47": [
        {"description": "Apple QuickTime, " "Quality 514 (50%)", "subsampling": "11"}
    ],
    "3bc3948025869f25b143aa517b2154ac": [
        {"description": "Apple QuickTime, " "Quality 674 (66%)", "subsampling": "11"}
    ],
    "3bdb097a9791f3ce6d7bbc4d6a194aa4": [
        {"description": "Apple QuickTime, " "Quality 569 (56%)", "subsampling": "11"}
    ],
    "3c1ff7ebab192163b4578e7dfcf63ce6": [
        {"description": "Apple QuickTime, " "Quality 328 (32%)", "subsampling": "11"}
    ],
    "3c58e82299d87346d37023ea015f3e80": [
        {
            "description": "Apple QuickTime, " "Quality 496 (48%)",
            "subsampling": "221111",
        }
    ],
    "3c724d4b5d8cbe203ebbf92ea8e22808": [
        {
            "description": "Apple QuickTime, " "Quality 599 (58%)",
            "subsampling": "221111",
        }
    ],
    "3c85026793f58eb45141847a27854fe2": [
        {
            "description": "Apple QuickTime, " "Quality 532-533 (52%)",
            "subsampling": "11",
        }
    ],
    "3c9d094741c995c2c0ac9daf14c4e683": [
        {"description": "Apple QuickTime, " "Quality 548 (54%)", "subsampling": "11"}
    ],
    "3ce5057aaf0ff155ee69d66591c8290d": [
        {
            "description": "Apple QuickTime, " "Quality 406 (40%)",
            "subsampling": "221111",
        }
    ],
    "3cf112c5843f98410599ea2a197e5cf6": [
        {"description": "Apple QuickTime, " "Quality 516 (50%)", "subsampling": "11"}
    ],
    "3cf156d54120b53057f56e9f38ee2896": [
        {"description": "FixFoto, Quality 12", "subsampling": ""}
    ],
    "3cfa966dde2536c83c921aa250b978b3": [
        {"description": "Apple QuickTime, " "Quality 485 (47%)", "subsampling": "11"}
    ],
    "3d8e25b74d0d9be662f26ec5fed6fe94": [
        {"description": "ACD Systems Digital " "Imaging, Quality 67", "subsampling": ""}
    ],
    "3d8f4957eab9756993a78efe08ba3798": [
        {
            "description": "Apple QuickTime, " "Quality 937-938 (92%)",
            "subsampling": "11",
        }
    ],
    "3da1e7270e0900a17a0a4ff8d3c9a488": [
        {
            "description": "Apple QuickTime, " "Quality 597 (58%)",
            "subsampling": "221111",
        }
    ],
    "3dd79429ada0455422ff6605c1727456": [
        {
            "description": "Apple QuickTime, " "Quality 272 (27%)",
            "subsampling": "221111",
        }
    ],
    "3deffd01a1c03929873dddd86a5339f1": [
        {"description": "Apple QuickTime, " "Quality 544 (53%)", "subsampling": "11"}
    ],
    "3e37de5c00962684feba769939fce685": [
        {
            "description": "Apple QuickTime, " "Quality 280 (27%)",
            "subsampling": "221111",
        }
    ],
    "3e646bfadb62d25ae8404b179e93e74e": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "62",
            "subsampling": "",
        }
    ],
    "3eafbf05c0dd233b385856065e456c11": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "84",
            "subsampling": "",
        }
    ],
    "3ebb7aa9113b3e1628f55732de7dae7f": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "21",
            "subsampling": "",
        }
    ],
    "3eedb8a357141ff5ae765fd3be2b232f": [
        {
            "description": "Apple QuickTime, " "Quality 881-886 " "(86-87%)",
            "subsampling": "211111",
        }
    ],
    "3f01645e33791ef09fbeb6c0e63db6a9": [
        {"description": "Apple QuickTime, " "Quality 269 (26%)", "subsampling": "11"}
    ],
    "3f243aacd371617b69f1e1eacadbbe2e": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "26",
            "subsampling": "",
        }
    ],
    "3f36450b0ba074578391e77f7340cef0": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "56 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 56",
            "subsampling": "111111",
        },
    ],
    "3f48672e37b6dd2e571b222e4b7ff97d": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "33 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 33",
            "subsampling": "111111",
        },
    ],
    "3f69293a4abeb2201004e7241fe22c75": [
        {
            "description": "Apple QuickTime, " "Quality 376 (37%)",
            "subsampling": "221111",
        }
    ],
    "3f7b04c7952f96d2624813ed9896f128": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 61", "subsampling": ""}
    ],
    "3fa780a3dff1d787f7d883585a46dcfb": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 35", "subsampling": ""}
    ],
    "3fab8f2b141f95a989fc4b046ad825cb": [
        {
            "description": "Apple QuickTime, " "Quality 761 (74%)",
            "subsampling": "221111",
        }
    ],
    "3fb9c046dff30dcb4128df984532d6ba": [
        {"description": "Apple QuickTime, " "Quality 447 (44%)", "subsampling": "11"}
    ],
    "4080277d75b20871d00ebc01ffbdb848": [
        {"description": "Apple QuickTime, " "Quality 474 (46%)", "subsampling": "11"}
    ],
    "40a7c1d8f58612f4470c2531768d93b5": [
        {
            "description": "Apple QuickTime, " "Quality 1014-1016 (99%)",
            "subsampling": "11",
        }
    ],
    "40c6f2886cdca8f19a654ce321ea993e": [
        {"description": "Nikon Capture NX, " "Quality 51", "subsampling": "221111"}
    ],
    "40d08b823fa60b838dd9998d1e2b550a": [
        {"description": "ACD Systems Digital " "Imaging, Quality 38", "subsampling": ""}
    ],
    "40e59fdb430180502ceacf7b4034eff8": [
        {"description": "Apple QuickTime, " "Quality 706 (69%)", "subsampling": "11"}
    ],
    "40f66b0a209f24716320636b776dda94": [
        {"description": "Pentax Optio E30/E40, " "Best", "subsampling": "211111"}
    ],
    "41061e1cdb97926ed5bded3da11af209": [
        {
            "description": "Apple QuickTime, " "Quality 436 (43%)",
            "subsampling": "221111",
        }
    ],
    "410ed63b6e5225d8b99da6272fd6069b": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 28",
            "subsampling": "221111",
        }
    ],
    "4127433151f74654762b1ef3293781f4": [
        {"description": "Pentax K10D (G)", "subsampling": "211111"}
    ],
    "4177be1c82543b32bf6578dc3a78d49d": [
        {
            "description": "Apple QuickTime, " "Quality 180-182 (18%)",
            "subsampling": "11",
        }
    ],
    "41d873034f29b298d899b48cd321c93f": [
        {"description": "Apple QuickTime, " "Quality 482 (47%)", "subsampling": "11"}
    ],
    "41dd47887a2b87e22ad3bbacc022374e": [
        {"description": "ACD Systems Digital " "Imaging, Quality 73", "subsampling": ""}
    ],
    "41e44bae14ab49d1b0f06438d34cb316": [
        {
            "description": "Apple QuickTime, " "Quality 408 (40%)",
            "subsampling": "221111",
        }
    ],
    "4205aec34791d70be03b90ab1e54ef8c": [
        {"description": "Apple QuickTime, " "Quality 707 (69%)", "subsampling": "11"}
    ],
    "4208fca702ec702bd5d41c8231883057": [
        {"description": "ACD Systems Digital " "Imaging, Quality 29", "subsampling": ""}
    ],
    "420af34c4f718cc0a10de5285140b6e0": [
        {
            "description": "Apple QuickTime, " "Quality 531 (52%)",
            "subsampling": "221111",
        }
    ],
    "420d094d00a4a8aec94c5667254d2053": [
        {
            "description": "Apple QuickTime, " "Quality 980-984 (96%)",
            "subsampling": "11",
        }
    ],
    "4271405c840705072a102d7e18b374d9": [
        {
            "description": "Apple QuickTime, " "Quality 929 (91%)",
            "subsampling": "211111",
        }
    ],
    "427271dd1e2a3d7a7ce54af73d9e6c77": [
        {
            "description": "Apple QuickTime, " "Quality 985-987 (96%)",
            "subsampling": "11",
        }
    ],
    "428ba2c747ea4e495ff3c7ff44a988d2": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 7",
            "subsampling": "221111",
        }
    ],
    "4295c1330dec60585760cbb05b79662d": [
        {
            "description": "Apple QuickTime, " "Quality 575 (56%)",
            "subsampling": "221111",
        }
    ],
    "42bae7ef4a41562b2e98d74248f4f22e": [
        {"description": "Apple QuickTime, " "Quality 421 (41%)", "subsampling": "11"}
    ],
    "42bfe52476bf07f1ed0e6451903cc9ee": [
        {
            "description": "Adobe Lightroom, " "Quality 85% - 92%",
            "subsampling": "111111",
        }
    ],
    "42cb001aea7e24d239f6c2fcbd861862": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 8",
            "subsampling": "221111",
        }
    ],
    "42cd88e0eb3c14a705b952550ec2eacd": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 34",
            "subsampling": "221111",
        }
    ],
    "42d6f71aace3de2ccfdd8348b0198704": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 54",
            "subsampling": "111111",
        }
    ],
    "42e0c4082ec4d026c77d19a053a983f4": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 77", "subsampling": ""}
    ],
    "42e7323506b113685e82e6d42664626f": [
        {
            "description": "Apple QuickTime, " "Quality 907-908 (89%)",
            "subsampling": "211111",
        }
    ],
    "42e7cdf33b9067a7124dd27020704f9a": [
        {"description": "Nikon Capture NX, " "Quality 71", "subsampling": "211111"}
    ],
    "42fd2864197991a38b3f80374a69d4e9": [
        {"description": "Apple QuickTime, " "Quality 297 (29%)", "subsampling": "11"}
    ],
    "4379016ba81dc331ffd5f9a8ab5b6399": [
        {"description": "Apple QuickTime, " "Quality 1004 (98%)", "subsampling": "11"}
    ],
    "43887ad276efb9ca8e8110498b38d814": [
        {
            "description": "Apple QuickTime, " "Quality 293 (29%)",
            "subsampling": "221111",
        }
    ],
    "43ceb0c1a5d94d55ee20dc3a168498b2": [
        {"description": "ACD Systems Digital " "Imaging, Quality 33", "subsampling": ""}
    ],
    "43eb3b161279ccc1fb4f9cbe7b92398f": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 83",
            "subsampling": "111111",
        }
    ],
    "43f9929d00af93968662983b891364d8": [
        {
            "description": "Apple QuickTime, " "Quality 1014-1016 (99%)",
            "subsampling": "211111",
        }
    ],
    "4417e739b9244781987769c2177abc6f": [
        {
            "description": "Apple QuickTime, " "Quality 543 (53%)",
            "subsampling": "221111",
        }
    ],
    "442c2664c07af1ec15d86581f43aab0b": [
        {"description": "Apple QuickTime, " "Quality 384 (38%)", "subsampling": "11"}
    ],
    "449ed4370a849e0f736b57ee7ccab942": [
        {
            "description": "Apple QuickTime, " "Quality 925-926 (90%)",
            "subsampling": "11",
        }
    ],
    "44be972c54cd64be7524a133a7395401": [
        {"description": "Apple QuickTime, " "Quality 432 (42%)", "subsampling": "11"}
    ],
    "44c8e4d0d7678034cb206609652ffeef": [
        {"description": "Apple QuickTime, " "Quality 357 (35%)", "subsampling": "11"}
    ],
    "44ced96f11e3a410201beed353a864cf": [
        {"description": "Apple QuickTime, " "Quality 607 (59%)", "subsampling": "11"}
    ],
    "44d2a7baaf1e3f8c3d45e4e6272a39b1": [
        {
            "description": "Apple QuickTime, " "Quality 236-237 (23%)",
            "subsampling": "221111",
        }
    ],
    "44e36eb25c6f9e313ef2a8f4c520c335": [
        {
            "description": "Apple QuickTime, " "Quality 593 (58%)",
            "subsampling": "221111",
        }
    ],
    "44f583ed6b65cb8ba915ec5df051616c": [
        {
            "description": "Adobe Lightroom, " "Quality 62% - 69%",
            "subsampling": "111111",
        },
        {"description": "Adobe Photoshop, " "Quality 8", "subsampling": "111111"},
    ],
    "45148ae63b12ccaa6fb5a487ca7620e9": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 30",
            "subsampling": "221111",
        }
    ],
    "457b05fd0787a8e29bd43cd65911d6ca": [
        {"description": "Nikon D80, Basic", "subsampling": "211111"}
    ],
    "45b20f0b0d7d88d8330354212af2e087": [
        {"description": "Apple QuickTime, " "Quality 635 (62%)", "subsampling": "11"}
    ],
    "45c46a02a434d8ea759742907bfa0ee5": [
        {
            "description": "Apple QuickTime, " "Quality 668 (65%)",
            "subsampling": "221111",
        }
    ],
    "4642245b427d5dd5c1c3766c323204ac": [
        {
            "description": "Apple QuickTime, " "Quality 822-824 (80%)",
            "subsampling": "211111",
        }
    ],
    "4694896b11fb898106e30fd4ed50cded": [
        {"description": "Apple QuickTime, " "Quality 358 (35%)", "subsampling": "11"}
    ],
    "469d14cef27dbb7c1f6f49324c077852": [
        {
            "description": "Apple QuickTime, " "Quality 256-257 (25%)",
            "subsampling": "11",
        }
    ],
    "46a125048b572576eed271816b2cbad2": [
        {
            "description": "Apple QuickTime, " "Quality 110-116 (11%)",
            "subsampling": "221111",
        }
    ],
    "46dd3917c1473ed0f8fc3f1e6f08416d": [
        {"description": "Apple QuickTime, " "Quality 391 (38%)", "subsampling": "11"}
    ],
    "46f55ee294723cee9faa816549b3cfa7": [
        {"description": "Adobe Photoshop, " "Quality 11", "subsampling": "11"}
    ],
    "470c0c761e2bb5e314a7112f3d64b277": [
        {"description": "Apple QuickTime, " "Quality 611 (60%)", "subsampling": "11"}
    ],
    "476a1ebd043ed59e56d18dd6d08777d7": [
        {
            "description": "Apple QuickTime, " "Quality 326 (32%)",
            "subsampling": "221111",
        }
    ],
    "4785aafc8471873402819e423b8969a9": [
        {"description": "Nikon Capture NX, " "Quality 39", "subsampling": "221111"}
    ],
    "483b5288e4256aa8ff96d6ccb96eba43": [
        {"description": "Canon EOS 1DmkII, Fine " "(C)", "subsampling": "211111"}
    ],
    "488e5d04f779b15c53f76e67cccdb2ed": [
        {"description": "Apple QuickTime, " "Quality 736 (72%)", "subsampling": "11"}
    ],
    "48a53035374c08e6490893d8113ed6b3": [
        {"description": "Nikon Capture NX, " "Quality 15", "subsampling": "221111"}
    ],
    "48b6aa4f0258162cceb9d43e19c96043": [
        {
            "description": "Apple QuickTime, " "Quality 360 (35%)",
            "subsampling": "221111",
        }
    ],
    "48fac53d9d168eab3ce9b6edc4b9fcb1": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 64", "subsampling": ""}
    ],
    "490b035a665ef80c7b48804461d55b7f": [
        {
            "description": "Apple QuickTime, " "Quality 609 (59%)",
            "subsampling": "221111",
        }
    ],
    "49222c4a3be01e93baad695bba63b254": [
        {
            "description": "Apple QuickTime, " "Quality 589 (58%)",
            "subsampling": "221111",
        }
    ],
    "493abc7f4b392a0341bfcac091edb8f8": [
        {"description": "Panasonic DMC-FZ30, " "High (B)", "subsampling": "211111"}
    ],
    "495aeee0f43a596938c98c5364feb2ee": [
        {"description": "Apple QuickTime, " "Quality 403 (39%)", "subsampling": "11"}
    ],
    "4971237e046795a030a99a0e8d2c5acb": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 52", "subsampling": ""}
    ],
    "4974cc7044768888244b324449a238ab": [
        {
            "description": "Apple QuickTime, " "Quality 622 (61%)",
            "subsampling": "221111",
        }
    ],
    "498f446de17202060a4752434df1ed7b": [
        {"description": "Apple QuickTime, " "Quality 799 (78%)", "subsampling": "11"}
    ],
    "4998abefc838e35cf0180395309e2e33": [
        {"description": "ACD Systems Digital " "Imaging, Quality 39", "subsampling": ""}
    ],
    "49b6e472c7d5ecead593c6009768e765": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "81 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 81",
            "subsampling": "111111",
        },
    ],
    "49cd1849b501868260d8a3b1e96d8625": [
        {"description": "Apple QuickTime, " "Quality 441 (43%)", "subsampling": "11"}
    ],
    "4a14a3e37c89e5a7570f672b1970ca55": [
        {"description": "Apple QuickTime, " "Quality 608 (59%)", "subsampling": "11"}
    ],
    "4a2361c48a583f6df779d1e6088ed83c": [
        {
            "description": "Apple QuickTime, " "Quality 680 (66%)",
            "subsampling": "221111",
        }
    ],
    "4a2605b7c5b1bc99b6715342de7b6562": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "47",
            "subsampling": "",
        }
    ],
    "4a2a0e381fed49e5d5ba074998652561": [
        {
            "description": "Apple QuickTime, " "Quality 534 (52%)",
            "subsampling": "221111",
        }
    ],
    "4a39b0ae55f0eaa5672f00015cae2d40": [
        {"description": "Apple QuickTime, " "Quality 420 (41%)", "subsampling": "11"}
    ],
    "4a4a154781db3f5f500e8cf177a4b446": [
        {
            "description": "Apple QuickTime, " "Quality 366 (36%)",
            "subsampling": "221111",
        }
    ],
    "4a78c6570fc84378e3334bfcd8a5680f": [
        {"description": "Apple QuickTime, " "Quality 489 (48%)", "subsampling": "11"}
    ],
    "4aa632db3be6b6e85565c1fe66cb22d1": [
        {
            "description": "Apple QuickTime, " "Quality 1024 (lossless)",
            "subsampling": "11",
        }
    ],
    "4aa883c43840de7f0d090284120c69bc": [
        {"description": "Panasonic DMC-FZ50, " "High (D)", "subsampling": "211111"}
    ],
    "4abd7dbca7735c987eb899b0f8646ce4": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "72",
            "subsampling": "",
        }
    ],
    "4b799df6fc9476102f890343080e66f5": [
        {
            "description": "Apple QuickTime, " "Quality 855-856 " "(83-84%)",
            "subsampling": "211111",
        }
    ],
    "4b96c3457701c201f90d56af1a82d43b": [
        {
            "description": "Apple QuickTime, " "Quality 354 (35%)",
            "subsampling": "221111",
        }
    ],
    "4baf3b1df2426fbdac3d0aaa0503ee94": [
        {
            "description": "Apple QuickTime, " "Quality 750 (73%)",
            "subsampling": "221111",
        }
    ],
    "4be1504b9732d1d9f6265d0616bad21b": [
        {
            "description": "Apple QuickTime, " "Quality 273 (27%)",
            "subsampling": "221111",
        }
    ],
    "4be64c2782cbb36b757cdcadd756498a": [
        {
            "description": "Apple QuickTime, " "Quality 286 (28%)",
            "subsampling": "221111",
        }
    ],
    "4bf1b53c292dec3f7cf3c020a3a9d911": [
        {"description": "Apple QuickTime, " "Quality 520 (51%)", "subsampling": "11"}
    ],
    "4bf515768d1a06e4c529ebae3e03b4b5": [
        {
            "description": "Apple QuickTime, " "Quality 270-271 (26%)",
            "subsampling": "221111",
        }
    ],
    "4c04d6fe904a4b6ff8b25c9f0e9f0a16": [
        {
            "description": "Apple QuickTime, " "Quality 636 (62%)",
            "subsampling": "221111",
        }
    ],
    "4c30c4399ef4bb2920601d940ed404eb": [
        {
            "description": "Apple QuickTime, " "Quality 660-661 " "(64-65%)",
            "subsampling": "11",
        }
    ],
    "4c3c425b4024b68c0de03904a825bc35": [
        {
            "description": "Adobe Lightroom, " "Quality 93% - 100%",
            "subsampling": "111111",
        }
    ],
    "4c4b7fc28e54a2bbdccd90d3618f01e8": [
        {"description": "Apple QuickTime, " "Quality 316 (31%)", "subsampling": "11"}
    ],
    "4ca8ec2a0c651e0508aab3b153cfee23": [
        {"description": "Apple QuickTime, " "Quality 479 (47%)", "subsampling": "11"}
    ],
    "4cbebcb06d1003e29429e9d5c9445919": [
        {"description": "Apple QuickTime, " "Quality 500 (49%)", "subsampling": "11"}
    ],
    "4d17c873e65b9d398f27735b0020c777": [
        {"description": "Apple QuickTime, " "Quality 564 (55%)", "subsampling": "11"}
    ],
    "4d5b512d8bc173f14e6a3cf8574f670a": [
        {"description": "Nikon Capture NX, " "Quality 9", "subsampling": "221111"}
    ],
    "4d6b36e81fe30c67dd53edb4d7c05422": [
        {"description": "Canon EOS 40D, Fine " "(vertical)", "subsampling": "121111"}
    ],
    "4d8f909ee8cb53e0386eb09c1591099b": [
        {"description": "Apple QuickTime, " "Quality 348 (34%)", "subsampling": "11"}
    ],
    "4dc4b433113acbde9d77a4cbad69bb14": [
        {"description": "Apple QuickTime, " "Quality 369 (36%)", "subsampling": "11"}
    ],
    "4e3daadebe0517955b1c86fb1fbc1dc1": [
        {
            "description": "Apple QuickTime, " "Quality 138-142 " "(13-14%)",
            "subsampling": "221111",
        }
    ],
    "4e7f4e5cd15f4fc089ab25890619dc60": [
        {"description": "Pentax K10D (AB)", "subsampling": "211111"}
    ],
    "4ea4e07900e04a3bd7572d4b59aa7a74": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 98",
            "subsampling": "111111",
        }
    ],
    "4ed4751d772933938600c4e7560bf19c": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 3", "subsampling": ""}
    ],
    "4ee61c39b97558a273f310e085d0bdd2": [
        {"description": "FinePixViewer, Normal", "subsampling": "211111"}
    ],
    "4f00127e7931d668a7b472c8a669925a": [
        {
            "description": "Apple QuickTime, " "Quality 767-768 (75%)",
            "subsampling": "11",
        }
    ],
    "4f15f7e4c56e7a75c0fe5454ab7e8f72": [
        {"description": "Apple QuickTime, " "Quality 475 (46%)", "subsampling": "11"}
    ],
    "4f50903ec9314f739e460c79552a20c5": [
        {
            "description": "Apple QuickTime, " "Quality 93-101 (9-10%)",
            "subsampling": "221111",
        }
    ],
    "4f5889173779409ec604622a1894ab4a": [
        {"description": "Nikon Capture NX, " "Quality 13", "subsampling": "221111"}
    ],
    "4f72f3cdc82d433e7f749be8036d4ce0": [
        {"description": "Apple QuickTime, " "Quality 538 (53%)", "subsampling": "11"}
    ],
    "4f83a1a8338a8e6e70eaa58cd236f62a": [
        {
            "description": "Apple QuickTime, " "Quality 475 (46%)",
            "subsampling": "221111",
        }
    ],
    "4fa27c83741226576ac6359cd4f6248e": [
        {
            "description": "Apple QuickTime, " "Quality 630 (62%)",
            "subsampling": "221111",
        }
    ],
    "4fa58542b5953534072b6dc1085deadf": [
        {"description": "Apple QuickTime, " "Quality 351 (34%)", "subsampling": "11"}
    ],
    "5009778c2a1df1deeb040c85fb9d0db2": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "18",
            "subsampling": "",
        }
    ],
    "50325a7b6e0a9b7f9aea8f5a6f7f31aa": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "90",
            "subsampling": "",
        }
    ],
    "50500b1272433ef5c9c96f16069fbdf1": [
        {
            "description": "Apple QuickTime, " "Quality 512 (50%)",
            "subsampling": "221111",
        }
    ],
    "5071640a38c5898dd5d2043346fd23e1": [
        {
            "description": "Apple QuickTime, " "Quality 793-795 " "(77-78%)",
            "subsampling": "211111",
        }
    ],
    "507b49a59dce17c02dc16fcb329352eb": [
        {"description": "Apple QuickTime, " "Quality 894 (87%)", "subsampling": "11"}
    ],
    "507cc511e561916efa3b49228ffc8c9a": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 8", "subsampling": ""}
    ],
    "50a510968effffab80bed1d08c6c5ccc": [
        {
            "description": "Apple QuickTime, " "Quality 708 (69%)",
            "subsampling": "221111",
        }
    ],
    "50b309f18bcf477742aa491ea55af777": [
        {
            "description": "Apple QuickTime, " "Quality 837 (82%)",
            "subsampling": "211111",
        }
    ],
    "50f1255f2424b2de5b930751ddf24842": [
        {
            "description": "Apple QuickTime, " "Quality 535 (52%)",
            "subsampling": "221111",
        }
    ],
    "50f9224c87a32486851bdbd3e686fd5b": [
        {
            "description": "Apple QuickTime, " "Quality 134-137 (13%)",
            "subsampling": "11",
        }
    ],
    "511c5bddc18566a2544732291920caf3": [
        {"description": "Apple QuickTime, " "Quality 801 (78%)", "subsampling": "11"}
    ],
    "5134762d2d4baac8711a52e76730591c": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 67", "subsampling": ""}
    ],
    "513d9e9dabbb480eb60f7ef76b1d755e": [
        {
            "description": "Apple QuickTime, " "Quality 745 (73%)",
            "subsampling": "221111",
        }
    ],
    "5180e51bd58432c7b51a305ed0c24d1b": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 31",
            "subsampling": "221111",
        }
    ],
    "51879d6e5178d2282d5e8276ed4e2439": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 80",
            "subsampling": "111111",
        }
    ],
    "51ad55cb254f36748123ca83f43556f4": [
        {"description": "Apple QuickTime, " "Quality 652 (64%)", "subsampling": "11"}
    ],
    "52092035b4e3fd45de3298c4d641385a": [
        {"description": "Apple QuickTime, " "Quality 483 (47%)", "subsampling": "11"}
    ],
    "5229288e448311401bb284133ac7d48c": [
        {
            "description": "Apple QuickTime, " "Quality 646 (63%)",
            "subsampling": "221111",
        }
    ],
    "52318e260c0d6b3dbee85c87f9b94e63": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "87 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 87",
            "subsampling": "111111",
        },
    ],
    "524742ca0cff64ecc0c7d7413e7d4b8d": [
        {"description": "Sony Image Data Suite, " "Quality 3", "subsampling": "211111"}
    ],
    "52886ef80147c9a136e20b2bc3b76f52": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "69 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 69",
            "subsampling": "111111",
        },
    ],
    "52ab880d25db7b36137e2a3c04987c9a": [
        {
            "description": "Apple QuickTime, " "Quality 518 (51%)",
            "subsampling": "221111",
        }
    ],
    "52b20edc779f206f2aed50610971f181": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 56", "subsampling": ""}
    ],
    "52f25cf8c4d610dffcc45681def8fb49": [
        {
            "description": "Apple QuickTime, " "Quality 911-914 (89%)",
            "subsampling": "211111",
        }
    ],
    "5301c2bcae09fd4305e47ffc56b2c8a7": [
        {"description": "Nikon Capture NX, " "Quality 59", "subsampling": "221111"}
    ],
    "5319a82dc93c1ee5c8d2265e4f1fb60e": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "80",
            "subsampling": "",
        }
    ],
    "5379e0133d4439b6f7c7039fc7f7734f": [
        {
            "description": "Adobe Lightroom, " "Quality 93% - 100%",
            "subsampling": "111111",
        },
        {"description": "Adobe Photoshop, " "Quality 12", "subsampling": "111111"},
    ],
    "537f40d0aae588fbce4cde9ba148604d": [
        {
            "description": "Apple QuickTime, " "Quality 283 (28%)",
            "subsampling": "221111",
        }
    ],
    "5399adc3f21ecb30c96d6a94b38ab74c": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 82",
            "subsampling": "111111",
        }
    ],
    "53a66cb32deb83c855f36b26527f4c10": [
        {
            "description": "Apple QuickTime, " "Quality 857 (84%)",
            "subsampling": "211111",
        }
    ],
    "545e14e832fb81f032526a9efcbf2450": [
        {
            "description": "Apple QuickTime, " "Quality 471 (46%)",
            "subsampling": "221111",
        }
    ],
    "548a841c0a8c3b2beeb134c6c3b922fc": [
        {
            "description": "Apple QuickTime, " "Quality 737-738 (72%)",
            "subsampling": "11",
        }
    ],
    "54ab2e8fbd7c4ecac9eba5fb02a5ccd9": [
        {"description": "Apple QuickTime, " "Quality 773 (75%)", "subsampling": "11"}
    ],
    "54dc50b16e7cc9bc383eb9e73e85e199": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "98 (Grayscale)",
            "subsampling": "11",
        }
    ],
    "54fcb6649f5ba51c32c68970797e41ea": [
        {
            "description": "Apple QuickTime, " "Quality 806-807 (79%)",
            "subsampling": "11",
        }
    ],
    "5504a428191bc87e5c1ba4b5e9984a37": [
        {
            "description": "Apple QuickTime, " "Quality 443 (43%)",
            "subsampling": "221111",
        }
    ],
    "5519e1c07692f51d0ee421ede78fb907": [
        {"description": "Apple QuickTime, " "Quality 800 (78%)", "subsampling": "11"}
    ],
    "5522213c915e2af3ad01ee2ec27ee3ed": [
        {"description": "Nikon Capture NX, " "Quality 85", "subsampling": "111111"},
        {
            "description": "ACD Systems Digital " "Imaging, Quality 92",
            "subsampling": "",
        },
    ],
    "552bf986ae119444955ded5f485d5dc4": [
        {"description": "Apple QuickTime, " "Quality 407 (40%)", "subsampling": "11"}
    ],
    "5532e398abb0a455b528659e59c7cfd7": [
        {
            "description": "Apple QuickTime, " "Quality 262 (26%)",
            "subsampling": "221111",
        }
    ],
    "5554cfd817a2713a690b957145b088ed": [
        {
            "description": "Apple QuickTime, " "Quality 915-917 " "(89-90%)",
            "subsampling": "211111",
        }
    ],
    "555dc90fb10df448f37c67ee7ec31bc2": [
        {
            "description": "Apple QuickTime, " "Quality 346 (34%)",
            "subsampling": "221111",
        }
    ],
    "555fd108ab97e641fcfefee4bda6a306": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "23",
            "subsampling": "",
        }
    ],
    "558d017ce6d5b5282ce76727fe99b91e": [
        {"description": "Apple Aperture Quality " "10", "subsampling": "221111"}
    ],
    "55cd2cad99821382b1bd78355980b1d1": [
        {"description": "Apple QuickTime, " "Quality 835 (82%)", "subsampling": "11"}
    ],
    "55d37ee1e3c8d12a70e67206fa1c9b0c": [
        {"description": "Apple QuickTime, " "Quality 386 (38%)", "subsampling": "11"}
    ],
    "55e0cf02a898abf8e224e2e9cf6e6ca5": [
        {
            "description": "Apple QuickTime, " "Quality 765-766 (75%)",
            "subsampling": "11",
        }
    ],
    "56224ea0ac2fccb92cbe9702896f9796": [
        {
            "description": "Apple QuickTime, " "Quality 433 (42%)",
            "subsampling": "221111",
        }
    ],
    "5628aeb29bb04d9c5073bc1caf371f01": [
        {
            "description": "Apple QuickTime, " "Quality 281 (27%)",
            "subsampling": "221111",
        }
    ],
    "563f732877b2c654d571c269bbb36a40": [
        {"description": "Apple QuickTime, " "Quality 238 (23%)", "subsampling": "11"}
    ],
    "5664c6ca557bc75526f59bea6aebde51": [
        {"description": "Apple QuickTime, " "Quality 754 (74%)", "subsampling": "11"}
    ],
    "56c4efb597cc30275229486199e60f70": [
        {
            "description": "Apple QuickTime, " "Quality 992-993 (97%)",
            "subsampling": "211111",
        }
    ],
    "56caa684ce7eb0b1cf662e1c88ed1614": [
        {"description": "ACD Systems Digital " "Imaging, Quality 17", "subsampling": ""}
    ],
    "56e9a02eb25508a9f71ad1a7cb9f9f4d": [
        {
            "description": "Apple QuickTime, " "Quality 277-278 (27%)",
            "subsampling": "221111",
        }
    ],
    "5701582a0da2e9e8dcd923a5cf877494": [
        {"description": "Nikon D50, Fine", "subsampling": "211111"}
    ],
    "577ec8895d884612d064771e84cf231f": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "6",
            "subsampling": "",
        }
    ],
    "57aa47876e10c6b4f35ecb8889e55ad9": [
        {"description": "Adobe Photoshop, " "Quality 8", "subsampling": "11"}
    ],
    "57d20578d190b04c7667b10d3df241bb": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "10 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 10",
            "subsampling": "111111",
        },
    ],
    "5862c8c2b241a9760f6804d970eefd66": [
        {
            "description": "Apple QuickTime, " "Quality 606 (59%)",
            "subsampling": "221111",
        }
    ],
    "5869e4a9592a7900e740b09fe19261a1": [
        {"description": "Apple QuickTime, " "Quality 225 (22%)", "subsampling": "11"}
    ],
    "586b40c7d4b95e11309636703e81fbe9": [
        {"description": "Canon EOS 20D, Fine", "subsampling": "211111"},
        {
            "description": "Pentax K20D/K200D/Optio "
            "230, Best; Canon EOS "
            "10D/300D/350D, Fine",
            "subsampling": "211111",
        },
    ],
    "5881004f575752d77ee00e767d848e51": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 56",
            "subsampling": "111111",
        }
    ],
    "5881bb3c6e7e2ac43983b4b1e947a6c3": [
        {
            "description": "Apple QuickTime, " "Quality 500 (49%)",
            "subsampling": "221111",
        }
    ],
    "588666e111892f10ca3f17bc362d9276": [
        {"description": "Apple QuickTime, " "Quality 584 (57%)", "subsampling": "11"}
    ],
    "589b1ef8cc8bece150218e4646d9dfd6": [
        {
            "description": "Apple QuickTime, " "Quality 185-187 (18%)",
            "subsampling": "11",
        }
    ],
    "58b302794024b9842657bbe7cb667577": [
        {
            "description": "Apple QuickTime, " "Quality 285 (28%)",
            "subsampling": "221111",
        }
    ],
    "58fe81014a9ee26a7bd393c8e31f4011": [
        {
            "description": "Apple QuickTime, " "Quality 407 (40%)",
            "subsampling": "221111",
        }
    ],
    "5910b8431fdd8ab93ce258f366c4b867": [
        {"description": "Pentax K2000, Best (B)", "subsampling": "211111"}
    ],
    "591c923a44c635c33769704c9cfa6ab7": [
        {
            "description": "Apple QuickTime, " "Quality 902 (88%)",
            "subsampling": "211111",
        }
    ],
    "5975500a23ab9a547ba149bf1aaa1893": [
        {
            "description": "Apple QuickTime, " "Quality 233-234 (23%)",
            "subsampling": "221111",
        }
    ],
    "599a7794c32b9d60e80426909ed40a09": [
        {"description": "Pentax K10D (H)", "subsampling": "211111"}
    ],
    "599b6ad93f32b9d5ce67e1622338c379": [
        {
            "description": "Apple QuickTime, " "Quality 143-146 (14%)",
            "subsampling": "221111",
        }
    ],
    "59a868b3d11d9cdc87859c02757e13bb": [
        {"description": "Pentax Optio E50, Best", "subsampling": "211111"}
    ],
    "59eedef87f255db058b5ba0b1d3a4ce8": [
        {
            "description": "Apple QuickTime, " "Quality 867 (85%)",
            "subsampling": "211111",
        }
    ],
    "59faa8c6fb70d4cf42765a92c1c7afc1": [
        {"description": "Apple QuickTime, " "Quality 334 (33%)", "subsampling": "11"}
    ],
    "5a1849b49122ff09949f1d355b4f9eaa": [
        {"description": "Nikon Capture NX, " "Quality 55", "subsampling": "221111"},
        {"description": "Nikon Capture NX, " "Quality 60", "subsampling": "211111"},
    ],
    "5a19d6130b03080dfedef45b6415f4f8": [
        {
            "description": "Apple QuickTime, " "Quality 505 (49%)",
            "subsampling": "221111",
        }
    ],
    "5a1b57a2583acf5c2428cd62fe24b773": [
        {
            "description": "Apple QuickTime, " "Quality 742 (72%)",
            "subsampling": "221111",
        }
    ],
    "5a2311c438c7183f6cd1f45c10e5783a": [
        {"description": "Apple QuickTime, " "Quality 748 (73%)", "subsampling": "11"}
    ],
    "5a285190351b16fee0eb14778280d74f": [
        {
            "description": "Apple QuickTime, " "Quality 547 (53%)",
            "subsampling": "221111",
        }
    ],
    "5a54f085c1780cadb13a7dea8347c7c6": [
        {
            "description": "Apple QuickTime, " "Quality 697 (68%)",
            "subsampling": "221111",
        }
    ],
    "5a74f09fb2586fa000c42e98e3b9f2d8": [
        {"description": "Pentax Optio T10", "subsampling": "211111"}
    ],
    "5aad44c55bf4f6dc538eaca006cafac2": [
        {"description": "Apple QuickTime, " "Quality 642 (63%)", "subsampling": "11"}
    ],
    "5aedf3816a813ed63b0521b0c384a677": [
        {"description": "Apple QuickTime, " "Quality 729 (71%)", "subsampling": "11"}
    ],
    "5aee693372b77c9721dba9d3596e371c": [
        {"description": "Apple QuickTime, " "Quality 267 (26%)", "subsampling": "11"}
    ],
    "5aef4c0bc6a5c8f1baded29946a56310": [
        {"description": "ACD Systems Digital " "Imaging, Quality 53", "subsampling": ""}
    ],
    "5b35e4bc9cbbc353b8e4b73132324088": [
        {
            "description": "Apple QuickTime, " "Quality 382 (37%)",
            "subsampling": "221111",
        }
    ],
    "5b54396a8a725e49e9bd4c9883b151df": [
        {"description": "Apple QuickTime, " "Quality 280 (27%)", "subsampling": "11"}
    ],
    "5b66fa5c0c1ba746289747229193cfb0": [
        {
            "description": "Apple QuickTime, " "Quality 612 (60%)",
            "subsampling": "221111",
        }
    ],
    "5b8a79eec9b7eb7755deb7f2c189e94a": [
        {
            "description": "Apple QuickTime, " "Quality 726 (71%)",
            "subsampling": "221111",
        }
    ],
    "5bb2cf3e6721c2dd8eb3341f9bff4159": [
        {"description": "Apple QuickTime, " "Quality 498 (49%)", "subsampling": "11"}
    ],
    "5c0a83e613d3bdd9ec7e86983f75b5be": [
        {"description": "Apple QuickTime, " "Quality 708 (69%)", "subsampling": "11"}
    ],
    "5c13c8db3a0b590f4fa3ec462b8890c3": [
        {"description": "Apple QuickTime, " "Quality 434 (42%)", "subsampling": "11"}
    ],
    "5c1a40094128ac76eab0405dcb4ae3c7": [
        {"description": "Nikon Capture NX, " "Quality 74", "subsampling": "211111"}
    ],
    "5c508e529d045b6f0c800e29ba2d6ab5": [
        {
            "description": "Adobe Lightroom, " "Quality 77% - 84%",
            "subsampling": "111111",
        }
    ],
    "5c606e0f7168a78fd8d0c91646c801a3": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 29", "subsampling": ""}
    ],
    "5ca52e1ffe2c84660d7377c33c88ad53": [
        {
            "description": "ACD Systems Digital " "Imaging, Quality 90 or " "91",
            "subsampling": "",
        }
    ],
    "5caf3989a757842c716220e4e426bde2": [
        {"description": "Apple QuickTime, " "Quality 414 (40%)", "subsampling": "11"}
    ],
    "5cbeb8f83a47b6a5e8711fe0ea7c42d7": [
        {"description": "Apple QuickTime, " "Quality 244 (24%)", "subsampling": "11"}
    ],
    "5cdf1d5bbe19375ad5c7237273dddede": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "77 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 77",
            "subsampling": "111111",
        },
    ],
    "5d1b5e80f9777a636d1d5cb402fcfc32": [
        {
            "description": "Apple QuickTime, " "Quality 311 (30%)",
            "subsampling": "221111",
        }
    ],
    "5d650a1d38108fd79d4f336ba8e254c2": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "37 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 37",
            "subsampling": "111111",
        },
    ],
    "5db6302d7e68c1a274139033681b8fcc": [
        {
            "description": "Apple QuickTime, " "Quality 463 (45%)",
            "subsampling": "221111",
        }
    ],
    "5de50c687a6e885634bf16adfd75e6bc": [
        {"description": "Apple QuickTime, " "Quality 411 (40%)", "subsampling": "11"}
    ],
    "5dfcb96d9a1186f662c6adb38bb9520a": [
        {"description": "Apple QuickTime, " "Quality 637 (62%)", "subsampling": "11"}
    ],
    "5e016a2d28f8ad3e7e27e4e2981031d2": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 90",
            "subsampling": "111111",
        }
    ],
    "5e3981a937c61480451d5bdc253e5472": [
        {
            "description": "Apple QuickTime, " "Quality 720 (70%)",
            "subsampling": "221111",
        }
    ],
    "5e528bd6778792490c6cf292cf9ba8df": [
        {
            "description": "Apple QuickTime, " "Quality 523 (51%)",
            "subsampling": "221111",
        }
    ],
    "5e5530c45def7006a7f672ce5778513d": [
        {
            "description": "Apple QuickTime, " "Quality 868 (85%)",
            "subsampling": "211111",
        }
    ],
    "5e55cc3328e61e88b9f2a49af4ec2268": [
        {
            "description": "Apple QuickTime, " "Quality 212-213 (21%)",
            "subsampling": "11",
        }
    ],
    "5e75328df5dadca132bb83e0883ce522": [
        {
            "description": "Apple QuickTime, " "Quality 258 (25%)",
            "subsampling": "221111",
        }
    ],
    "5e983407295808e244f6bdece469c8be": [
        {"description": "Apple QuickTime, " "Quality 376 (37%)", "subsampling": "11"}
    ],
    "5ea9e766888399a41f3f1a3c5c15cd90": [
        {"description": "Pentax K10D (AZ)", "subsampling": "211111"}
    ],
    "5ee766b90badc8fed5a5386e78a80783": [
        {
            "description": "Pentax *istDS, Good " "(edit in camera)",
            "subsampling": "211111",
        }
    ],
    "5efe038d405e029badcea4c8ee2bfc88": [
        {"description": "Apple QuickTime, " "Quality 816 (80%)", "subsampling": "11"}
    ],
    "5f6e3a66672d6e4c41b1689996ca57d3": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 39", "subsampling": ""}
    ],
    "5f7b9af6d66eaf12874aa680e7b0d31b": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "66",
            "subsampling": "",
        }
    ],
    "5fa6bb26309d43ca6c89d6cc776a68a4": [
        {
            "description": "Apple QuickTime, " "Quality 944-946 (92%)",
            "subsampling": "211111",
        }
    ],
    "5ffdd2e918ec293efc79083703737290": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 2", "subsampling": ""}
    ],
    "60258dcc1e3a81858d176080ef774730": [
        {
            "description": "Apple QuickTime, " "Quality 484 (47%)",
            "subsampling": "221111",
        }
    ],
    "60264e35250325032bf7866ca8beaf58": [
        {"description": "Apple QuickTime, " "Quality 815 (80%)", "subsampling": "11"}
    ],
    "6042038094d7f4ad72c61c2a2e7a467f": [
        {
            "description": "Apple QuickTime, " "Quality 842 (82%)",
            "subsampling": "211111",
        }
    ],
    "606c4c78c0226646bf4d3c5a5898fb17": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "52 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 52",
            "subsampling": "111111",
        },
    ],
    "606e5652fc33c6a02328f0bd23ee9751": [
        {
            "description": "Apple QuickTime, " "Quality 171-173 (17%)",
            "subsampling": "221111",
        }
    ],
    "60880ff1f7bfe6a85cd80c2d4582395b": [
        {"description": "Apple QuickTime, " "Quality 387 (38%)", "subsampling": "11"}
    ],
    "6096eb584b99a587f5527e20473aa9d1": [
        {
            "description": "Apple QuickTime, " "Quality 787 (77%)",
            "subsampling": "211111",
        }
    ],
    "60a0ca27f3e7289d97c033ca217899cc": [
        {
            "description": "Apple QuickTime, " "Quality 796-798 (78%)",
            "subsampling": "211111",
        }
    ],
    "60b682c4d412f5255efbaa32787c46ca": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "47 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 47",
            "subsampling": "111111",
        },
    ],
    "60cb2afa0cfa7395635a9360fc690b46": [
        {"description": "Apple Aperture Quality " "0", "subsampling": "221111"}
    ],
    "60d17e041a23d47b96c5aac86180a022": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 86",
            "subsampling": "111111",
        }
    ],
    "60f75a915647ed50d1724179d50a35d2": [
        {"description": "Nikon Capture NX, " "Quality 83", "subsampling": "111111"}
    ],
    "610772f3cf75c2fd89214fafbd7617a6": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "5",
            "subsampling": "",
        }
    ],
    "6120ded86d4cc42cd7ca2131b1f51fad": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 6", "subsampling": ""}
    ],
    "6123a3685e1012af5a0d024de1ce0304": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 60",
            "subsampling": "111111",
        }
    ],
    "612941a50f2c0992938bc13106caf228": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 9", "subsampling": ""}
    ],
    "613ef896fc4af5baad36e2680968a7ba": [
        {
            "description": "Apple QuickTime, " "Quality 183-184 (18%)",
            "subsampling": "221111",
        }
    ],
    "617c4c853344ef079f4a1f1062672e8c": [
        {
            "description": "Apple QuickTime, " "Quality 551-552 (54%)",
            "subsampling": "221111",
        }
    ],
    "61814a2eca233e10b0ba26881551fb50": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "68",
            "subsampling": "",
        }
    ],
    "61884dc8b93e63c07bb487a6e29d6fb7": [
        {"description": "Apple QuickTime, " "Quality 456 (45%)", "subsampling": "11"}
    ],
    "6194167174dfcb4a769cf26f5c7a018d": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 5", "subsampling": ""}
    ],
    "619fd49197f0403ce13d86cffec46419": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "11 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 11",
            "subsampling": "111111",
        },
    ],
    "61b1d4a02498b7467f2c8e8cfebdfae9": [
        {
            "description": "Apple QuickTime, " "Quality 775-776 (76%)",
            "subsampling": "211111",
        }
    ],
    "61bb38e23040b6a8b0e8721e6d6eff66": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 63", "subsampling": ""}
    ],
    "61c8506b490d5e596151b951ffa7a14f": [
        {
            "description": "Apple QuickTime, " "Quality 509 (50%)",
            "subsampling": "221111",
        }
    ],
    "61cb5e93e3e69f6929d97653824733b0": [
        {"description": "Apple QuickTime, " "Quality 305 (30%)", "subsampling": "11"}
    ],
    "61d311bde22762ae0e88b768e835eced": [
        {"description": "Pentax Optio 33WR/M50, " "Best", "subsampling": "211111"}
    ],
    "620244f053fef313466fbcb232077aca": [
        {"description": "Apple QuickTime, " "Quality 345 (34%)", "subsampling": "11"}
    ],
    "62e6812d1f7935adddd1a69227cdf626": [
        {
            "description": "Apple QuickTime, " "Quality 502 (49%)",
            "subsampling": "221111",
        }
    ],
    "631548841b70e871ee16009737dd4b9c": [
        {
            "description": "Apple QuickTime, " "Quality 843-844 (82%)",
            "subsampling": "11",
        }
    ],
    "63190207beeb805306f7d0bcc3898cb3": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 26",
            "subsampling": "221111",
        }
    ],
    "637103ef9d8e84f8345f8218f158fc3c": [
        {
            "description": "Pentax Optio " "550/M10/T30/W30, Best",
            "subsampling": "211111",
        }
    ],
    "6385ee79b090ea430190dbe1ee93ddca": [
        {"description": "Apple QuickTime, " "Quality 364 (36%)", "subsampling": "11"}
    ],
    "63b59904874e5e427ddecb37e12f90c7": [
        {
            "description": "Apple QuickTime, " "Quality 582 (57%)",
            "subsampling": "221111",
        }
    ],
    "63ef900bf59d41003a0e0602baa60681": [
        {
            "description": "Apple QuickTime, " "Quality 459 (45%)",
            "subsampling": "221111",
        }
    ],
    "63f61a0d3c4f1ace8ebe5b6ae23e3f25": [
        {"description": "Apple QuickTime, " "Quality 540 (53%)", "subsampling": "11"}
    ],
    "63f9786c6a9b8ef87c791818ddaba058": [
        {
            "description": "Apple QuickTime, " "Quality 298 (29%)",
            "subsampling": "221111",
        }
    ],
    "641812174c82d5b62ec86c33bd852204": [
        {"description": "Pentax K10D (I)", "subsampling": "211111"}
    ],
    "643ad95753c261eacc5ea3f4c9e4d469": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "87",
            "subsampling": "",
        }
    ],
    "64677161baed1c47d2fdd6eefd779583": [
        {
            "description": "Apple QuickTime, " "Quality 805 (79%)",
            "subsampling": "211111",
        }
    ],
    "649a90949cab8f45d3ecef78068165d1": [
        {"description": "Apple QuickTime, " "Quality 494 (48%)", "subsampling": "11"}
    ],
    "64b80be38604eaecc99236b1f74a99f8": [
        {
            "description": "Apple QuickTime, " "Quality 316 (31%)",
            "subsampling": "221111",
        }
    ],
    "64d056c9e5e558d6c04d07d9d21aa7a3": [
        {
            "description": "Apple QuickTime, " "Quality 796-798 (78%)",
            "subsampling": "11",
        }
    ],
    "64ff54dc33f610e3705cae31428ce43d": [
        {
            "description": "Apple QuickTime, " "Quality 202-203 (20%)",
            "subsampling": "11",
        }
    ],
    "6502d634e5bf3f849e9d382886fc32fe": [
        {"description": "Apple QuickTime, " "Quality 657 (64%)", "subsampling": "11"}
    ],
    "6516e60b3995e21b6750ebca1ddcfee5": [
        {"description": "Apple QuickTime, " "Quality 581 (57%)", "subsampling": "11"}
    ],
    "6518270228fd20730740a08cc8a171f6": [
        {"description": "Pentax K10D (AC)", "subsampling": "211111"}
    ],
    "6528da6df208ce35fd84dccabc81d4da": [
        {
            "description": "Apple QuickTime, " "Quality 978-979 (96%)",
            "subsampling": "11",
        }
    ],
    "6537be61d21f1b6ded3253fdd84f599b": [
        {
            "description": "Apple QuickTime, " "Quality 759-760 (74%)",
            "subsampling": "11",
        }
    ],
    "6538fc6f5f1744b40c0b8b5bc7179983": [
        {"description": "Apple QuickTime, " "Quality 452 (44%)", "subsampling": "11"}
    ],
    "653c5006512bb3aaa1e6a4e77078b630": [
        {
            "description": "Apple QuickTime, " "Quality 480 (47%)",
            "subsampling": "221111",
        }
    ],
    "6547daee398d39f773742be92ef2d0d0": [
        {"description": "Apple QuickTime, " "Quality 319 (31%)", "subsampling": "11"}
    ],
    "6579941db0216f41f0a20de9b626538a": [
        {"description": "Adobe Photoshop, " "Quality 7", "subsampling": "11"}
    ],
    "659f7466f80a8034f74a00ba07b8c3fb": [
        {
            "description": "Apple QuickTime, " "Quality 802-804 " "(78-79%)",
            "subsampling": "11",
        }
    ],
    "65bf1ddc176fe4002a7a2ecaac60e58c": [
        {"description": "Apple QuickTime, " "Quality 705 (69%)", "subsampling": "11"}
    ],
    "65d20361f4ba0725cf150c7ae2033776": [
        {"description": "Apple QuickTime, " "Quality 554 (54%)", "subsampling": "11"}
    ],
    "65d7471a913f6cc87e9dc65ea594606b": [
        {"description": "Apple QuickTime, " "Quality 258 (25%)", "subsampling": "11"}
    ],
    "65edf81f975f01a7b3ad1c16a1af64cb": [
        {"description": "Apple QuickTime, " "Quality 320 (31%)", "subsampling": "11"}
    ],
    "662bd7fb9dff6426e310f9261a3703d0": [
        {"description": "Nikon D50, Fine", "subsampling": "211111"}
    ],
    "66309175abaa59d6246237a77ce9eb76": [
        {"description": "Apple QuickTime, " "Quality 436 (43%)", "subsampling": "11"}
    ],
    "6634cdad61e7a8e6fb3a4ba1a0416256": [
        {
            "description": "Apple QuickTime, " "Quality 190-191 (19%)",
            "subsampling": "221111",
        }
    ],
    "663b8a9dbd00efa78281f5028b35c503": [
        {
            "description": "Apple QuickTime, " "Quality 288 (28%)",
            "subsampling": "221111",
        }
    ],
    "6640ae3bb6f646013769b182c74931b5": [
        {"description": "Canon PowerShot, Normal", "subsampling": "211111"}
    ],
    "66529cc8ef9694e6a37e8787d0f160fd": [
        {"description": "Apple QuickTime, " "Quality 596 (58%)", "subsampling": "11"}
    ],
    "666dd95fd0e20f5c20bc44d78d528869": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "28 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 28",
            "subsampling": "111111",
        },
    ],
    "6686cddc46088f0987e7476861fbfb47": [
        {"description": "Pentax K2000, Best (A)", "subsampling": "211111"}
    ],
    "66ae78a749b520b35d4daf4531df8ae5": [
        {"description": "Nikon Capture NX, " "Quality 40", "subsampling": "221111"}
    ],
    "66aeb0f03343673eeed6462e0ce9e1aa": [
        {
            "description": "Apple QuickTime, " "Quality 147-150 " "(14-15%)",
            "subsampling": "221111",
        }
    ],
    "66e85870faf72f4f3fe25486409b286a": [
        {
            "description": "Apple QuickTime, " "Quality 958 (94%)",
            "subsampling": "211111",
        }
    ],
    "66fc410ab8f71a7fdef86fd70b742dc1": [
        {"description": "ACD Systems Digital " "Imaging, Quality 3", "subsampling": ""}
    ],
    "6700663d4ebaeb394bfd3c85597347b5": [
        {
            "description": "Apple QuickTime, " "Quality 632 (62%)",
            "subsampling": "221111",
        }
    ],
    "671a071a1b17f49a774da3893f7199c7": [
        {
            "description": "Apple QuickTime, " "Quality 250 (24%)",
            "subsampling": "221111",
        }
    ],
    "673b05962b8255cbc9bdbbc48965b4b7": [
        {"description": "Apple QuickTime, " "Quality 592 (58%)", "subsampling": "11"}
    ],
    "67515a725833d40535a54b4ef9551e05": [
        {"description": "Apple QuickTime, " "Quality 457 (45%)", "subsampling": "11"}
    ],
    "6773f3db56ae831012dbe43c1650571a": [
        {
            "description": "Apple QuickTime, " "Quality 682 (67%)",
            "subsampling": "221111",
        }
    ],
    "679dea81c8d4563e07efac4fab6b89ca": [
        {"description": "ACD Systems Digital " "Imaging, Quality 32", "subsampling": ""}
    ],
    "67a7c8896d03a030b56130e1f9c5caad": [
        {"description": "Apple QuickTime, " "Quality 519 (51%)", "subsampling": "11"}
    ],
    "67b9a678d9f669167c5b4bf12422ad50": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 50", "subsampling": ""}
    ],
    "67d5eb5f55c9a5baa0a67d42a841d77b": [
        {"description": "Nikon Capture NX, " "Quality 19", "subsampling": "221111"}
    ],
    "67db25c57803c34b065736f46f6afadb": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 59", "subsampling": ""}
    ],
    "67ed20f2fe283549dae4ba40860c3777": [
        {"description": "Apple QuickTime, " "Quality 365 (36%)", "subsampling": "11"}
    ],
    "67fbe0dce139b6db1813e30bbbceccf3": [
        {"description": "Nikon Capture NX, " "Quality 64", "subsampling": "211111"}
    ],
    "6808ca55a29fcb9c15db1925a84370c3": [
        {
            "description": "Apple QuickTime, " "Quality 864 (84%)",
            "subsampling": "211111",
        }
    ],
    "683270dbffdc5cd2d4e6cb841f17b206": [
        {
            "description": "Apple QuickTime, " "Quality 769 (75%)",
            "subsampling": "211111",
        }
    ],
    "683506a889c78d9bc230a0c7ee5f62f3": [
        {"description": "Adobe Lightroom, " "Quality 0% - 7%", "subsampling": "221111"},
        {"description": "Adobe Photoshop, " "Quality 0", "subsampling": "221111"},
    ],
    "684649f6c1590f5a912a827a6d8bfc6b": [
        {"description": "ACD Systems Digital " "Imaging, Quality 9", "subsampling": ""}
    ],
    "68783ed0a7956cf0b7a1b2787e756213": [
        {
            "description": "Apple QuickTime, " "Quality 586 (57%)",
            "subsampling": "221111",
        }
    ],
    "68799ccfa08e2f55b5be79264d3ca58a": [
        {"description": "Apple QuickTime, " "Quality 331 (32%)", "subsampling": "11"}
    ],
    "688c7dca6b12c22a21e0caf1a0336c80": [
        {
            "description": "Apple QuickTime, " "Quality 669-671 " "(65-66%)",
            "subsampling": "11",
        }
    ],
    "689a0e3511f2aea75637f46e6af9fd9f": [
        {
            "description": "Pentax Optio A40, Best " "(edit in camera)",
            "subsampling": "211111",
        }
    ],
    "68a0d6250be9df2c05556ff59988c499": [
        {"description": "Apple QuickTime, " "Quality 394 (38%)", "subsampling": "11"}
    ],
    "68a4a67af696f82bbbb7db15a16c0c46": [
        {"description": "Apple QuickTime, " "Quality 453 (44%)", "subsampling": "11"}
    ],
    "68a808b23bfa8096e04006171926b72c": [
        {
            "description": "Apple QuickTime, " "Quality 498 (49%)",
            "subsampling": "221111",
        }
    ],
    "68b07a219cda4b9fc9a8507b788d8230": [
        {"description": "Apple QuickTime, " "Quality 400 (39%)", "subsampling": "11"}
    ],
    "68d5ce8ce1a9e337ee9630dadad0650e": [
        {
            "description": "Apple QuickTime, " "Quality 827-829 (81%)",
            "subsampling": "11",
        }
    ],
    "68ff8bfc0e15c93586ef6b4cf347469c": [
        {"description": "Apple QuickTime, " "Quality 377 (37%)", "subsampling": "11"}
    ],
    "69747272d4079b78c2ee2ef0f5e63f30": [
        {
            "description": "Apple QuickTime, " "Quality 81-92 (8-9%)",
            "subsampling": "221111",
        }
    ],
    "69c6b9440342adfc0db89a6c91aba332": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "64 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 64",
            "subsampling": "111111",
        },
    ],
    "69fe5c29b9d5e4c823f8a082ab7b3285": [
        {"description": "FixFoto, Quality 13", "subsampling": ""}
    ],
    "6a092d8fd56ca0e852d74bd86cfc4f47": [
        {
            "description": "Apple QuickTime, " "Quality 956-957 (93%)",
            "subsampling": "211111",
        }
    ],
    "6a20041beb5b67d38525bb7507ffeb49": [
        {"description": "Apple QuickTime, " "Quality 573 (56%)", "subsampling": "11"}
    ],
    "6a243ac0b8575c2ed962070cd7d39e04": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 79",
            "subsampling": "111111",
        }
    ],
    "6a26a11cc28df00e01d5979e2e0fb4f7": [
        {"description": "ACD Systems Digital " "Imaging, Quality 47", "subsampling": ""}
    ],
    "6a2eb9f07f3c96365a06d91da171e673": [
        {"description": "Apple QuickTime, " "Quality 437 (43%)", "subsampling": "11"}
    ],
    "6a37c2572bb47dff514aa4b343c104b5": [
        {"description": "Apple QuickTime, " "Quality 726 (71%)", "subsampling": "11"}
    ],
    "6a87dd29703c2b3ef80f1b5d2cc8d26a": [
        {"description": "Apple QuickTime, " "Quality 697 (68%)", "subsampling": "11"}
    ],
    "6a9ead8b2339567482a172a581e86c15": [
        {
            "description": "Apple QuickTime, " "Quality 743-744 (73%)",
            "subsampling": "221111",
        }
    ],
    "6ad87d648101c268f83fa379d4c773f2": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "31 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 31",
            "subsampling": "111111",
        },
    ],
    "6ae041573525edd42e800e1b61d4313c": [
        {
            "description": "Apple QuickTime, " "Quality 247 (24%)",
            "subsampling": "221111",
        }
    ],
    "6ae7ab4e6d5e0e67006cca59c70f843c": [
        {"description": "ACD Systems Digital " "Imaging, Quality 22", "subsampling": ""}
    ],
    "6af05d547e8911fe2d1f2b4d968a477e": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 89", "subsampling": ""}
    ],
    "6af4053465275c1b1b2d5c97f4d841aa": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "48",
            "subsampling": "",
        }
    ],
    "6af868a0eececd267495f749a38b4f95": [
        {
            "description": "Apple QuickTime, " "Quality 997-998 (97%)",
            "subsampling": "211111",
        }
    ],
    "6b37d6acc52259bf972a41e84dea7754": [
        {"description": "Apple QuickTime, " "Quality 583 (57%)", "subsampling": "11"}
    ],
    "6b590185b5d6ecbc1d79c2624a0d5319": [
        {"description": "Apple QuickTime, " "Quality 259 (25%)", "subsampling": "11"}
    ],
    "6b9be09d6ec6491a20c2827dbeb678c0": [
        {"description": "Apple Aperture Quality " "1", "subsampling": "221111"}
    ],
    "6bb5ab15f80beebcb73fae0ef089fa61": [
        {"description": "Apple QuickTime, " "Quality 235 (23%)", "subsampling": "11"}
    ],
    "6bc9ebaf9f3ed62ec8818076f6f81c7f": [
        {"description": "Apple QuickTime, " "Quality 513 (50%)", "subsampling": "11"}
    ],
    "6bd350bf5df27ed1b5bf1d83fa9d021f": [
        {"description": "Sony DSLR-A700, Fine", "subsampling": "211111"}
    ],
    "6bfdcd36327406f801be86d0e8ca6b60": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 46",
            "subsampling": "221111",
        }
    ],
    "6c0476ba4b3fcc4675cfab20d3c96368": [
        {"description": "Apple QuickTime, " "Quality 263 (26%)", "subsampling": "11"}
    ],
    "6c0916ab5aa02602cc682bcdbc22369e": [
        {
            "description": "Apple QuickTime, " "Quality 537 (52%)",
            "subsampling": "221111",
        }
    ],
    "6c0ac535ec30285b609e0b8ca18e4dc0": [
        {
            "description": "Apple QuickTime, " "Quality 888-890 (87%)",
            "subsampling": "11",
        }
    ],
    "6c0e396c705a59ec610a22f11466621b": [
        {"description": "Apple QuickTime, " "Quality 778 (76%)", "subsampling": "11"}
    ],
    "6c121faf4784a5a93fbf7fff4470dea4": [
        {
            "description": "Apple QuickTime, " "Quality 464-465 (45%)",
            "subsampling": "11",
        }
    ],
    "6c23da63c864f1433ec198ae202e56f0": [
        {
            "description": "Apple QuickTime, " "Quality 567 (55%)",
            "subsampling": "221111",
        }
    ],
    "6c2bc41a4b6ad1e20655ffcc0dfd2c41": [
        {"description": "Pentax Optio 330RS, " "Fine", "subsampling": "221111"}
    ],
    "6c42d12564d1c5706653a8ddb5375192": [
        {
            "description": "Apple QuickTime, " "Quality 248-249 (24%)",
            "subsampling": "221111",
        }
    ],
    "6c6260b84a3a588614d65133430289ea": [
        {
            "description": "Apple QuickTime, " "Quality 681 (67%)",
            "subsampling": "221111",
        }
    ],
    "6c64fa9ad302624a826f04ecc80459be": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "14 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 14",
            "subsampling": "111111",
        },
    ],
    "6c947f09bc02f87b257a26f9f5c77a77": [
        {
            "description": "Apple QuickTime, " "Quality 287 (28%)",
            "subsampling": "221111",
        }
    ],
    "6ca4a27cb36f35ab84b0e2df06bb32f4": [
        {"description": "Nikon Capture NX, " "Quality 76", "subsampling": "211111"}
    ],
    "6cdd3762e346b16a59af4bddb213b07a": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 4",
            "subsampling": "221111",
        }
    ],
    "6cf4dfbe3df89d9728e0f34b7b145223": [
        {"description": "Apple QuickTime, " "Quality 417 (41%)", "subsampling": "11"}
    ],
    "6cf948e65c9d32279c757394a4f5b77e": [
        {"description": "Apple QuickTime, " "Quality 315 (31%)", "subsampling": "11"}
    ],
    "6cfe3833aadd87487afc11129d8cb2aa": [
        {"description": "Pentax Optio S, Better", "subsampling": "221111"}
    ],
    "6d79fe623c4c5320bdbe4d3026f4e71a": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 48", "subsampling": ""}
    ],
    "6dabf05ddc213b650ff08aa9a8cb9f50": [
        {
            "description": "Apple QuickTime, " "Quality 403 (39%)",
            "subsampling": "221111",
        }
    ],
    "6dc3abbdd52b2f26b790ddb33b82099a": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "43",
            "subsampling": "",
        }
    ],
    "6e0952a44c37bc2d98dbede4ec429c99": [
        {"description": "Apple QuickTime, " "Quality 472 (46%)", "subsampling": "11"}
    ],
    "6e3f6a3a5a1eae6155331d42d6f968dd": [
        {
            "description": "Adobe Lightroom, " "Quality 85% - 92%",
            "subsampling": "111111",
        },
        {"description": "Adobe Photoshop, " "Quality 11", "subsampling": "111111"},
    ],
    "6e9cfb8131373c3d1873e3f497e46b64": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 54", "subsampling": ""}
    ],
    "6eb301fb89e7d625129b77a53fe30dcc": [
        {
            "description": "Apple QuickTime, " "Quality 925-926 (90%)",
            "subsampling": "211111",
        }
    ],
    "6eeaaacec8edc933b68602b01d16204e": [
        {"description": "Apple QuickTime, " "Quality 699 (68%)", "subsampling": "11"}
    ],
    "6ef0b71a5676c4645a3166b9c34744fa": [
        {
            "description": "Apple QuickTime, " "Quality 918-920 (90%)",
            "subsampling": "211111",
        }
    ],
    "6f338385a8f2cd2dd3420a4f6138a206": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 92", "subsampling": ""}
    ],
    "6f6bfc10750e6717cc3791a9ea1d7569": [
        {
            "description": "Apple QuickTime, " "Quality 718-719 (70%)",
            "subsampling": "221111",
        }
    ],
    "6f7825365b673f9eb2ac050d27a21d1b": [
        {
            "description": "Apple QuickTime, " "Quality 206-207 (20%)",
            "subsampling": "221111",
        }
    ],
    "6f879b2b5642ee3d01faf3410a721e2d": [
        {
            "description": "Apple QuickTime, " "Quality 821 (80%)",
            "subsampling": "211111",
        }
    ],
    "6f96ed52a987d67e8d950b2627d3fbc2": [
        {
            "description": "Apple QuickTime, " "Quality 628 (61%)",
            "subsampling": "221111",
        }
    ],
    "6f9cae52d3f47f514f7c927314455a5a": [
        {"description": "Nikon Capture NX, " "Quality 77", "subsampling": "211111"},
        {"description": "Nikon Capture NX, " "Quality 81", "subsampling": "111111"},
    ],
    "6fa04ba1184e986c4da3df8141e05a42": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "81",
            "subsampling": "",
        }
    ],
    "6fc283989bb3a8c91f6c4384df2fa25d": [
        {
            "description": "Apple QuickTime, " "Quality 221-222 (22%)",
            "subsampling": "11",
        }
    ],
    "6fcbaaa11108d1712bad5410b3db5b91": [
        {
            "description": "Apple QuickTime, " "Quality 1001-1002 (98%)",
            "subsampling": "211111",
        }
    ],
    "6fd7b56ac6b58dc861e6021815fb5704": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 94",
            "subsampling": "111111",
        }
    ],
    "70073f02f04ee893510bceb09e411d53": [
        {
            "description": "Apple QuickTime, " "Quality 528 (52%)",
            "subsampling": "221111",
        }
    ],
    "701e4820f6d0b68e67b6a2b90a7baa0c": [
        {"description": "FixFoto, Quality 9", "subsampling": ""}
    ],
    "704c1868fe865f1038aa2bd0697f71a0": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "22",
            "subsampling": "",
        }
    ],
    "705064f644ac4b24884500a40ad0f7cf": [
        {
            "description": "Apple QuickTime, " "Quality 947-948 " "(92-93%)",
            "subsampling": "211111",
        }
    ],
    "705ae76b905302bd9f3b78cc8d1cb28f": [
        {"description": "Apple QuickTime, " "Quality 329 (32%)", "subsampling": "11"}
    ],
    "7079c2d71ff33e7c4e8efdece23c307b": [
        {"description": "Apple QuickTime, " "Quality 643 (63%)", "subsampling": "11"}
    ],
    "70a0b15e2e5f97e0a9333a2011afe5cd": [
        {"description": "FixFoto, Quality 19", "subsampling": ""}
    ],
    "70a311935ed066da954897fad5079377": [
        {"description": "Nikon Capture NX, " "Quality 30", "subsampling": "221111"}
    ],
    "70d843457698f46db30181ac616deb75": [
        {
            "description": "Apple QuickTime, " "Quality 275 (27%)",
            "subsampling": "221111",
        }
    ],
    "70e105a22b036f7c1ce0b5d02fa1c34e": [
        {"description": "Apple QuickTime, " "Quality 495 (48%)", "subsampling": "11"}
    ],
    "70e5babe9507bae6725e401a36903070": [
        {"description": "Apple QuickTime, " "Quality 484 (47%)", "subsampling": "11"}
    ],
    "712c145d6472a2b315b2ecfb916d1590": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "58 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 58",
            "subsampling": "111111",
        },
    ],
    "71555bee8d64c9dfca3cefa9dd332472": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "17",
            "subsampling": "",
        }
    ],
    "7163b345b90553e246296a48b46cc0b3": [
        {
            "description": "Apple QuickTime, " "Quality 909-910 (89%)",
            "subsampling": "211111",
        }
    ],
    "717cbe19ae1dc9f72c86ef518aefea16": [
        {"description": "Apple QuickTime, " "Quality 817 (80%)", "subsampling": "11"}
    ],
    "71c1a56890fff9b0a095fa5a1c96132b": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "73 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 73",
            "subsampling": "111111",
        },
    ],
    "71d0e3444a4c82cf39048ba8cf7b1d5f": [
        {
            "description": "Apple QuickTime, " "Quality 439 (43%)",
            "subsampling": "221111",
        }
    ],
    "72161116404ed3cb449674760d0e4776": [
        {"description": "Apple QuickTime, " "Quality 710 (69%)", "subsampling": "11"}
    ],
    "723c2a2de195391f2db06456e9345c5b": [
        {"description": "Apple QuickTime, " "Quality 312 (30%)", "subsampling": "11"}
    ],
    "7254c012821f2bc866d7d6dd7906c92d": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 6",
            "subsampling": "221111",
        }
    ],
    "725bcc59a6f5a1436dfa0dfd96cdcf44": [
        {
            "description": "Apple QuickTime, " "Quality 814 (79%)",
            "subsampling": "211111",
        }
    ],
    "72a91837a63fa7444416bc00a05d988b": [
        {
            "description": "Apple QuickTime, " "Quality 930 (91%)",
            "subsampling": "211111",
        }
    ],
    "72abfdc6e65b32ded2cd7ac77a04f447": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "18 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 18",
            "subsampling": "111111",
        },
    ],
    "72bce7df55635509eb6468fc6406941d": [
        {"description": "Pentax K10D (AD)", "subsampling": "211111"}
    ],
    "72cdcc91e3ddc2c3d17c20173b75c5ef": [
        {"description": "Canon EOS 1DmkII, Fine " "(B)", "subsampling": "211111"}
    ],
    "72d947637340246a35ff3ee969fd613f": [
        {"description": "Apple QuickTime, " "Quality 761 (74%)", "subsampling": "11"}
    ],
    "72df283a5c07671eba341500a3fc18f1": [
        {
            "description": "Apple QuickTime, " "Quality 723 (71%)",
            "subsampling": "221111",
        }
    ],
    "72f08842473a6c504469d341259e5cd7": [
        {
            "description": "Apple QuickTime, " "Quality 739-740 (72%)",
            "subsampling": "221111",
        }
    ],
    "731f7ffedba80407d039c1db5a785f95": [
        {
            "description": "ACD Systems Digital " "Imaging, Quality 75 or " "76",
            "subsampling": "",
        }
    ],
    "731fa7404c090db157030e40804604b6": [
        {"description": "Apple QuickTime, " "Quality 383 (37%)", "subsampling": "11"}
    ],
    "73313d816524749545292ed2284c804c": [
        {
            "description": "Apple QuickTime, " "Quality 923-924 (90%)",
            "subsampling": "11",
        }
    ],
    "734255167cbd052200fb4c474f05bcd9": [
        {
            "description": "Apple QuickTime, " "Quality 395 (39%)",
            "subsampling": "221111",
        }
    ],
    "73478bb7714d1d2342bbf22c5fdc04d6": [
        {"description": "Apple QuickTime, " "Quality 444 (43%)", "subsampling": "11"}
    ],
    "7364416ce4f2a9282efdbe052574527b": [
        {"description": "Nikon Capture NX, " "Quality 58", "subsampling": "221111"}
    ],
    "737c61e006222488645fa2e007f83f3c": [
        {
            "description": "Apple QuickTime, " "Quality 449 (44%)",
            "subsampling": "221111",
        }
    ],
    "738685b86b80ff0e8b562102d1b58f71": [
        {"description": "Nikon Capture NX, " "Quality 14", "subsampling": "221111"}
    ],
    "740d4a06f4d0f774c6aac95719673793": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "29",
            "subsampling": "",
        }
    ],
    "74523ad3424dcff6aa697c3ce433ad4e": [
        {
            "description": "Apple QuickTime, " "Quality 584 (57%)",
            "subsampling": "221111",
        }
    ],
    "7464b2361e5b5f5a9ba74a87475dda91": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "54 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 54",
            "subsampling": "111111",
        },
    ],
    "74cc07bbb7049d59aff0c4965d4d5084": [
        {
            "description": "Apple QuickTime, " "Quality 731 (71%)",
            "subsampling": "221111",
        }
    ],
    "74f0ef9476707be45f06951ca9a809ba": [
        {"description": "Canon DV/Optura/Elura, " "Superfine", "subsampling": "211111"}
    ],
    "74fddf6faaf251b28a00b4d0cd9e5621": [
        {"description": "Apple QuickTime, " "Quality 750 (73%)", "subsampling": "11"}
    ],
    "752fbc15f77a8c2149f5ae6bf49204b8": [
        {"description": "Apple QuickTime, " "Quality 626 (61%)", "subsampling": "11"}
    ],
    "757e97f3490ebc5b74fd63792fb23992": [
        {
            "description": "Apple QuickTime, " "Quality 342 (33%)",
            "subsampling": "221111",
        }
    ],
    "758d37a9d3b91c0ba383d23f5a080d8f": [
        {
            "description": "Apple QuickTime, " "Quality 185-187 (18%)",
            "subsampling": "221111",
        }
    ],
    "7590bc1a40090163a101bfd28daa3fc2": [
        {"description": "Apple QuickTime, " "Quality 522 (51%)", "subsampling": "11"}
    ],
    "759fb7011e13fa5f975bb668f5b94d8b": [
        {"description": "Pentax Optio " "550/750Z/M60/X, Best", "subsampling": "211111"}
    ],
    "75d4ffdc6c10675cb1b5bd002d4e0e41": [
        {
            "description": "Apple QuickTime, " "Quality 353 (34%)",
            "subsampling": "221111",
        }
    ],
    "75ee5a0fd61559c6bf8e6ebc920c93b0": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 85",
            "subsampling": "111111",
        }
    ],
    "75f260644b87a9779188126da8709e7f": [
        {"description": "Nikon Capture NX, " "Quality 22", "subsampling": "221111"}
    ],
    "75ff62bbf17aa1762dd15677e961ce67": [
        {"description": "ACD Systems Digital " "Imaging, Quality 87", "subsampling": ""}
    ],
    "7624f08396d811fdb6f1ead575e67e58": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 10", "subsampling": ""}
    ],
    "762f9501e83d58307d1e102ddb343207": [
        {
            "description": "Apple QuickTime, " "Quality 971 (95%)",
            "subsampling": "211111",
        }
    ],
    "767c20d7d54970b0974f205c790d7d04": [
        {"description": "Apple QuickTime, " "Quality 317 (31%)", "subsampling": "11"}
    ],
    "76806382fa57818da2e406a0dc23ce20": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "51",
            "subsampling": "",
        }
    ],
    "76aa290370382de8a3516f73389f9350": [
        {
            "description": "Apple QuickTime, " "Quality 368 (36%)",
            "subsampling": "221111",
        }
    ],
    "76af24fe94edf8f3992e38c1dd6eebce": [
        {
            "description": "Apple QuickTime, " "Quality 495 (48%)",
            "subsampling": "221111",
        }
    ],
    "76bc1d777c94b680683610218732eb11": [
        {"description": "Apple QuickTime, " "Quality 298 (29%)", "subsampling": "11"}
    ],
    "76bcc27918d8f12b343e6e5a41108781": [
        {
            "description": "Apple QuickTime, " "Quality 748 (73%)",
            "subsampling": "221111",
        }
    ],
    "76d22de881d1b95b491689b589743b7a": [
        {
            "description": "Apple QuickTime, " "Quality 647 (63%)",
            "subsampling": "221111",
        }
    ],
    "76d958276bf2cac3c36b7d9a677094a7": [
        {
            "description": "PENTAX PHOTO " "Laboratory, Highest " "compression",
            "subsampling": "211111",
        },
        {"description": "Pentax K10D (J)", "subsampling": "211111"},
    ],
    "771eeb43856b1821a271b0aa8398a243": [
        {
            "description": "Apple QuickTime, " "Quality 479 (47%)",
            "subsampling": "221111",
        }
    ],
    "7749ec06b1f1b1be30aa58dbef838d49": [
        {"description": "Apple QuickTime, " "Quality 449 (44%)", "subsampling": "11"}
    ],
    "7755ba223679105c184be0ada8c99f92": [
        {
            "description": "Apple QuickTime, " "Quality 238 (23%)",
            "subsampling": "221111",
        }
    ],
    "7770d784d852b3333f9213713e481125": [
        {"description": "Pentax Optio 450, Best", "subsampling": "211111"}
    ],
    "77f680490d08697cb0f11ff3fe76b7e8": [
        {"description": "Nikon Capture NX, " "Quality 92", "subsampling": "111111"}
    ],
    "7849ba902d96273b5ac7b6eb98f4d009": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 96", "subsampling": ""}
    ],
    "785c36a6aa2bedd207cb1fa450a5e6d4": [
        {
            "description": "Apple QuickTime, " "Quality 270-271 (26%)",
            "subsampling": "11",
        }
    ],
    "786aa4e46172ac65e10b230f3dcaadb2": [
        {"description": "Apple QuickTime, " "Quality 371 (36%)", "subsampling": "11"}
    ],
    "78787c9f0aae4ab8d15ab47eaea5035c": [
        {"description": "Apple QuickTime, " "Quality 342 (33%)", "subsampling": "11"}
    ],
    "787ed74c3d5570c03f98804bc9d0c448": [
        {
            "description": "Apple QuickTime, " "Quality 378 (37%)",
            "subsampling": "221111",
        }
    ],
    "78801638505e95827c2f7cc0c7ef78f4": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 17", "subsampling": ""}
    ],
    "789076781ff1e18154091f2460c1bab5": [
        {
            "description": "Apple QuickTime, " "Quality 937-938 (92%)",
            "subsampling": "211111",
        }
    ],
    "78a2a442aac5cca7fa2ef5a8bd96219e": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 35",
            "subsampling": "221111",
        }
    ],
    "78b0e590ea36cb11c495097049022d2e": [
        {
            "description": "Apple QuickTime, " "Quality 455 (44%)",
            "subsampling": "221111",
        }
    ],
    "78bb04e3ced3eee51c78e94b421ecc26": [
        {
            "description": "Apple QuickTime, " "Quality 267 (26%)",
            "subsampling": "221111",
        }
    ],
    "78d004490e822405acded09846135e50": [
        {
            "description": "Apple QuickTime, " "Quality 843 (82%)",
            "subsampling": "211111",
        }
    ],
    "78d19da8de8095644aa31fb409033fe7": [
        {"description": "Apple QuickTime, " "Quality 559 (55%)", "subsampling": "11"}
    ],
    "78f66ee0bc442950808e25daa02a2b02": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 12", "subsampling": ""}
    ],
    "791e3897f6ac92fb5e708b28dbd361b1": [
        {"description": "Apple QuickTime, " "Quality 731 (71%)", "subsampling": "11"}
    ],
    "792e93c41ac63451068b887b11ad0c2e": [
        {
            "description": "Apple QuickTime, " "Quality 165-167 (16%)",
            "subsampling": "221111",
        }
    ],
    "798f48b6dbe3f1cd7b40b03fae8d2611": [
        {"description": "Apple QuickTime, " "Quality 518 (51%)", "subsampling": "11"}
    ],
    "79b07131be4827795315bf42c65212f2": [
        {"description": "Pentax K10D (K)", "subsampling": "211111"}
    ],
    "79f546689b548868a904f50214928aa1": [
        {
            "description": "Apple QuickTime, " "Quality 676 (66%)",
            "subsampling": "221111",
        }
    ],
    "7a12ccd01bfdd2cf3b8ee2df498b8ae0": [
        {"description": "Apple QuickTime, " "Quality 858 (84%)", "subsampling": "11"}
    ],
    "7a318965f27e3c09d11f53cbb10a872b": [
        {
            "description": "Apple QuickTime, " "Quality 430 (42%)",
            "subsampling": "221111",
        }
    ],
    "7a52e3960831057d58e9b1ba03b87cf3": [
        {"description": "Apple QuickTime, " "Quality 702 (69%)", "subsampling": "11"}
    ],
    "7a5c04b63f9fe6af176efef387ba1f03": [
        {
            "description": "Apple QuickTime, " "Quality 338 (33%)",
            "subsampling": "221111",
        }
    ],
    "7a75abc5c5ec8cc0fa43f239ab048c08": [
        {"description": "Apple QuickTime, " "Quality 439 (43%)", "subsampling": "11"}
    ],
    "7b0242bd9aaeab4962f5d5b39b9a4027": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "93 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 93",
            "subsampling": "111111",
        },
    ],
    "7b0f02aa96271376d3f81658d98fb1df": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 87", "subsampling": ""}
    ],
    "7b17607b9954c37e525b1fbc35271553": [
        {
            "description": "Apple QuickTime, " "Quality 685 (67%)",
            "subsampling": "221111",
        }
    ],
    "7b3058792db9876a86c65ec44c0261b3": [
        {"description": "Apple QuickTime, " "Quality 375 (37%)", "subsampling": "11"}
    ],
    "7b83284f61decf47ab3f8f7361c18943": [
        {"description": "Adobe Photoshop, " "Quality 12", "subsampling": "11"}
    ],
    "7b85fffdf97680de53e49788712c50de": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "71",
            "subsampling": "",
        }
    ],
    "7be7bded72d0ade6f907e3adcf62b391": [
        {
            "description": "Apple QuickTime, " "Quality 363 (35%)",
            "subsampling": "221111",
        }
    ],
    "7bf7022a7c12b3b7ea085b46158253e6": [
        {
            "description": "Apple QuickTime, " "Quality 749 (73%)",
            "subsampling": "221111",
        }
    ],
    "7bff346b97abf46ca005af4e74b560fa": [
        {"description": "Apple QuickTime, " "Quality 663 (65%)", "subsampling": "11"}
    ],
    "7c34e6e7fe2cc760fa5c3ed812a8b74c": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 46", "subsampling": ""}
    ],
    "7c685e2916555eda34cb37a1e71adc6a": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "63 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 63",
            "subsampling": "111111",
        },
    ],
    "7c71a5eb9408b93be3ea6cf9be1d31ea": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "52",
            "subsampling": "",
        }
    ],
    "7c7d225760bce3b4e479aca8bcd2b850": [
        {"description": "Apple QuickTime, " "Quality 868 (85%)", "subsampling": "11"}
    ],
    "7c8242581553e818ef243fc680879a19": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "50 (Grayscale)",
            "subsampling": "11",
        },
        {"description": "Apple QuickTime, " "Quality 325 (32%)", "subsampling": "11"},
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 50",
            "subsampling": "111111",
        },
    ],
    "7c95c94440f652232530fe4c411be1a2": [
        {"description": "Apple QuickTime, " "Quality 355 (35%)", "subsampling": "11"}
    ],
    "7cafc25f204fc4ddf39d86e2f0f07b62": [
        {"description": "Pentax K10D (AE)", "subsampling": "211111"}
    ],
    "7cb380e582317b8387037450cc68db5e": [
        {"description": "Apple QuickTime, " "Quality 492 (48%)", "subsampling": "11"}
    ],
    "7cbd635e5fee8bbd290b0d383b03da5a": [
        {"description": "Apple QuickTime, " "Quality 646 (63%)", "subsampling": "11"}
    ],
    "7ce7d00283cada911c3ebc347680bc7d": [
        {"description": "Apple QuickTime, " "Quality 283 (28%)", "subsampling": "11"}
    ],
    "7cfd092a41a0e1c029e82467cb4c034f": [
        {"description": "ACD Systems Digital " "Imaging, Quality 77", "subsampling": ""}
    ],
    "7d1819ccce2756fcf6dfbb67565c2552": [
        {
            "description": "Apple QuickTime, " "Quality 568 (55%)",
            "subsampling": "221111",
        }
    ],
    "7d4205e3d4e0b6c7071a418c9b5840cb": [
        {
            "description": "Apple QuickTime, " "Quality 192-194 (19%)",
            "subsampling": "11",
        }
    ],
    "7d71776416a8771d10e3c2e6dc6a5f21": [
        {
            "description": "Apple QuickTime, " "Quality 694-695 (68%)",
            "subsampling": "221111",
        }
    ],
    "7d8ee11ca66d2c22ff9ed1f778b5dbac": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 76",
            "subsampling": "111111",
        }
    ],
    "7dc25cc528116e25dd1aeb590dd7cb66": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "7",
            "subsampling": "",
        }
    ],
    "7dc9316230c4f197fb5d1b36f09cd883": [
        {
            "description": "Apple QuickTime, " "Quality 197-198 (19%)",
            "subsampling": "221111",
        }
    ],
    "7dd6377a907070b1ca7e05f770ca2aab": [
        {
            "description": "Apple QuickTime, " "Quality 551-552 (54%)",
            "subsampling": "11",
        }
    ],
    "7dec6568dbad7a70622c994a326957e2": [
        {"description": "Nikon Capture NX, " "Quality 36", "subsampling": "221111"}
    ],
    "7e1453eec55a8c40166b2d8985ad6bdc": [
        {
            "description": "Apple QuickTime, " "Quality 1017 (99%)",
            "subsampling": "211111",
        }
    ],
    "7e3999424de8a8f6bb84e3cfc07628e8": [
        {"description": "Apple QuickTime, " "Quality 262 (26%)", "subsampling": "11"}
    ],
    "7e4b44f2900a405e7b85090af7d40298": [
        {
            "description": "Apple QuickTime, " "Quality 367 (36%)",
            "subsampling": "221111",
        }
    ],
    "7e6246d9be5273b979beb680b284e7b8": [
        {"description": "Apple QuickTime, " "Quality 0-63 (0-6%)", "subsampling": "11"}
    ],
    "7eafb9874384d391836e64911e912295": [
        {"description": "Panasonic DMC-FZ50, " "High (E)", "subsampling": "211111"}
    ],
    "7eb9fe0338a7b802860a60e0088418fd": [
        {"description": "Apple QuickTime, " "Quality 614 (60%)", "subsampling": "11"}
    ],
    "7ed52852c280b97fd44def8434d84051": [
        {
            "description": "Apple QuickTime, " "Quality 228-229 (22%)",
            "subsampling": "11",
        }
    ],
    "7ed560efea0b44168d910a73fab9204c": [
        {"description": "ACD Systems Digital " "Imaging, Quality 82", "subsampling": ""}
    ],
    "7ef06dbde538346b8b01c6b538ca70c6": [
        {
            "description": "Adobe Lightroom, " "Quality 39% - 46%",
            "subsampling": "221111",
        },
        {"description": "Adobe Photoshop, " "Quality 5", "subsampling": "221111"},
    ],
    "7ef2cd2b66d51fe80d94d5db427ee9ef": [
        {"description": "FixFoto, Quality 17", "subsampling": ""}
    ],
    "7f3d110973a4d7d5824724c4e577b407": [
        {
            "description": "Apple QuickTime, " "Quality 384 (38%)",
            "subsampling": "221111",
        }
    ],
    "7f51ebf21174bcd3b027ae3cc77c4459": [
        {
            "description": "Apple QuickTime, " "Quality 1004 (98%)",
            "subsampling": "211111",
        }
    ],
    "7f712aecf513621f635a007aadda61af": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 17",
            "subsampling": "221111",
        }
    ],
    "7f8b33a26e7f35a6eaf2e95df81e1cca": [
        {
            "description": "Apple QuickTime, " "Quality 1024 (Lossless)",
            "subsampling": "111111",
        }
    ],
    "7fac641c5b795e68ca8cfae4466a19c7": [
        {"description": "Apple QuickTime, " "Quality 845 (83%)", "subsampling": "11"}
    ],
    "7fca22065811c0efe6599a15ca38f05e": [
        {
            "description": "Apple QuickTime, " "Quality 457 (45%)",
            "subsampling": "221111",
        }
    ],
    "7fe7b339c6ffc62b984eeab4b0df9168": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "84 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 84",
            "subsampling": "111111",
        },
    ],
    "8015ad9fa22d6565ca61ce9979f3663f": [
        {"description": "Apple QuickTime, " "Quality 428 (42%)", "subsampling": "11"}
    ],
    "80175a9dbb871d045c738fdeb6fcbdc7": [
        {"description": "Apple QuickTime, " "Quality 293 (29%)", "subsampling": "11"}
    ],
    "80409b38f84336548b62e337a850e9cb": [
        {
            "description": "Apple QuickTime, " "Quality 941-943 (92%)",
            "subsampling": "211111",
        }
    ],
    "804bd63907214e005f01fb65a2bb00e6": [
        {"description": "Pentax Optio S4i, Best", "subsampling": "221111"}
    ],
    "80bdd75a2fc87b5288bc77763481df83": [
        {"description": "Apple QuickTime, " "Quality 398 (39%)", "subsampling": "11"}
    ],
    "80ccbe5645cc62ebd4ae7b2128b42d91": [
        {
            "description": "Apple QuickTime, " "Quality 409 (40%)",
            "subsampling": "221111",
        }
    ],
    "80db52b1671d32d8bd3126bf1d7db8ec": [
        {"description": "Apple QuickTime, " "Quality 530 (52%)", "subsampling": "11"}
    ],
    "80ef22ca4475af1bbb8963ac511144d7": [
        {"description": "Apple QuickTime, " "Quality 808 (79%)", "subsampling": "11"}
    ],
    "80f2c05e2ad3524f18dd55bac10ee2e3": [
        {
            "description": "Apple QuickTime, " "Quality 536 (52%)",
            "subsampling": "221111",
        }
    ],
    "811e5b0229f0e8baf4b40cd2d8777550": [
        {"description": "Pentax K10D (AF)", "subsampling": "211111"}
    ],
    "81339d89e8294729c69fc096f1a448f3": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "19",
            "subsampling": "",
        }
    ],
    "8134ff0c4713cc1ef4a25ff60b49ac54": [
        {
            "description": "Apple QuickTime, " "Quality 643 (63%)",
            "subsampling": "221111",
        }
    ],
    "813b89236cfe429fe534361f28ace015": [
        {
            "description": "Apple QuickTime, " "Quality 683 (67%)",
            "subsampling": "221111",
        }
    ],
    "81597eb992e32e186d2b5565bbe4ae3a": [
        {"description": "Nikon Capture NX, " "Quality 57", "subsampling": "221111"}
    ],
    "8190e844832ee8ea97492b509c728de4": [
        {
            "description": "Apple QuickTime, " "Quality 333 (33%)",
            "subsampling": "221111",
        }
    ],
    "81a936d8371a7d59da428fcfc349850f": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "4",
            "subsampling": "",
        }
    ],
    "81ac42cc63416f7c66cd2a51a8801cbd": [
        {
            "description": "Apple QuickTime, " "Quality 210-211 (21%)",
            "subsampling": "11",
        }
    ],
    "81c1ce1c7d15394d95eaf2d6bd1495e3": [
        {"description": "Apple QuickTime, " "Quality 318 (31%)", "subsampling": "11"}
    ],
    "81d620f1b470fd535b26544b4ea20643": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "38 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 38",
            "subsampling": "111111",
        },
    ],
    "81f039d6a0ded8227dc51273d153b295": [
        {
            "description": "Apple QuickTime, " "Quality 703-704 (69%)",
            "subsampling": "221111",
        }
    ],
    "82028a770d9e45d64d6aa26faee97e72": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "20",
            "subsampling": "",
        }
    ],
    "820db98d1ee91bb648e7a05498a340b0": [
        {"description": "Apple QuickTime, " "Quality 928 (91%)", "subsampling": "11"}
    ],
    "821d7e59bcf756171b7644ec5736266e": [
        {
            "description": "Apple QuickTime, " "Quality 634 (62%)",
            "subsampling": "221111",
        }
    ],
    "824a9788f50aad6ca26ada301cae5c72": [
        {
            "description": "Apple QuickTime, " "Quality 174-176 (17%)",
            "subsampling": "11",
        }
    ],
    "825fb58744c6c2432d232f5fb83a9597": [
        {
            "description": "Apple QuickTime, " "Quality 330 (32%)",
            "subsampling": "221111",
        }
    ],
    "8278e4f14c7bf6efd2a847ef40f392e3": [
        {"description": "Apple QuickTime, " "Quality 777 (76%)", "subsampling": "11"}
    ],
    "82a9cce34fb9c7c3c0ab908533a9a9bf": [
        {
            "description": "Apple QuickTime, " "Quality 855-856 " "(83-84%)",
            "subsampling": "11",
        }
    ],
    "82b4bc7c4a832b620e810311a33c9771": [
        {"description": "Apple QuickTime, " "Quality 656 (64%)", "subsampling": "11"}
    ],
    "82b56237e4eccde035edff4a5abdba44": [
        {"description": "Panasonic DMC-FZ50, " "High (F)", "subsampling": "211111"}
    ],
    "82d40afcb23ac10dba01bbab101da176": [
        {"description": "Apple QuickTime, " "Quality 340 (33%)", "subsampling": "11"}
    ],
    "82e672854d7e00d47a988855b95d2f7f": [
        {
            "description": "Apple QuickTime, " "Quality 374 (37%)",
            "subsampling": "221111",
        }
    ],
    "82f45d11d651d93a67995965b94aa649": [
        {
            "description": "Apple QuickTime, " "Quality 550 (54%)",
            "subsampling": "221111",
        }
    ],
    "8319dfe3caedea6988e5024b0196d317": [
        {"description": "Apple QuickTime, " "Quality 404 (39%)", "subsampling": "11"}
    ],
    "8335023e5a1ee8df80d52327b0556c44": [
        {"description": "Panasonic DMC-FZ30, " "High (C)", "subsampling": "211111"}
    ],
    "8361a9dbb5d93ad098a0ce2091b0bdf5": [
        {"description": "Apple QuickTime, " "Quality 356 (35%)", "subsampling": "11"}
    ],
    "836448ef538366adb50202927b53808a": [
        {"description": "Pentax K10D (L)", "subsampling": "211111"}
    ],
    "8392742f8f5971ed08c7520d0e9c81f3": [
        {"description": "Apple QuickTime, " "Quality 1017 (99%)", "subsampling": "11"}
    ],
    "83c8ceab43dedde06d8068e5b8ccdc2b": [
        {"description": "Apple QuickTime, " "Quality 266 (26%)", "subsampling": "11"}
    ],
    "83d6d7dd7ace56feeeb65b88accae1bc": [
        {"description": "Canon PowerShot, Normal " "Small", "subsampling": "211111"}
    ],
    "83e206dafb515f20a4b9a0c16f770940": [
        {
            "description": "Apple QuickTime, " "Quality 305 (30%)",
            "subsampling": "221111",
        }
    ],
    "83f3452abc7906930b228c29a4320089": [
        {"description": "Apple QuickTime, " "Quality 1003 (98%)", "subsampling": "11"}
    ],
    "83ff61ebceff5f888b9615b250aa7b76": [
        {"description": "Apple QuickTime, " "Quality 690 (67%)", "subsampling": "11"}
    ],
    "840be626ed18db6cdef3c5c357e24d34": [
        {"description": "ACD Systems Digital " "Imaging, Quality 23", "subsampling": ""}
    ],
    "84285f5b3248884488e5142b8c7210e2": [
        {"description": "Pentax Optio S6, Good", "subsampling": "211111"}
    ],
    "8431e86434062b325c519fd836353cd0": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 85", "subsampling": ""}
    ],
    "8453391d3adf377c46a1a0cee08c35c3": [
        {
            "description": "Adobe Lightroom, " "Quality 24% - 30%",
            "subsampling": "221111",
        }
    ],
    "84788c494352a07ab54f360f4a2a3d34": [
        {"description": "Apple QuickTime, " "Quality 272 (27%)", "subsampling": "11"}
    ],
    "849bce1254b14d44e24a6b419c385597": [
        {
            "description": "Apple QuickTime, " "Quality 424 (41%)",
            "subsampling": "221111",
        }
    ],
    "84a69c0b43505dd0cbc25d640873b5b9": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 5",
            "subsampling": "221111",
        }
    ],
    "84c2067991afbb6851204f21f5d132ea": [
        {
            "description": "Apple QuickTime, " "Quality 350 (34%)",
            "subsampling": "221111",
        }
    ],
    "84c8e142e6d27734b126f76653b9199d": [
        {
            "description": "Apple QuickTime, " "Quality 639 (62%)",
            "subsampling": "221111",
        }
    ],
    "84d5f059ce3e1b78d91355e1e86e2d1a": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 55",
            "subsampling": "111111",
        }
    ],
    "84dbe33962674aab86e03681ac3bd35f": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 82", "subsampling": ""}
    ],
    "84de345dcf710f937a39a0b631b87fc4": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 51",
            "subsampling": "111111",
        }
    ],
    "850f2b2aaa99ad390bc9443be1b587dc": [
        {"description": "Apple QuickTime, " "Quality 250 (24%)", "subsampling": "11"}
    ],
    "8534b67f8115ddc0296623a1ed3fc8ec": [
        {"description": "ACD Systems Digital " "Imaging, Quality 42", "subsampling": ""}
    ],
    "853946ede6a624136546ec5b68ecdc49": [
        {"description": "Apple QuickTime, " "Quality 461 (45%)", "subsampling": "11"}
    ],
    "854d2e536bc92a9e2e3db3ff2c18e138": [
        {
            "description": "Apple QuickTime, " "Quality 359 (35%)",
            "subsampling": "221111",
        }
    ],
    "8558c6d41f03db192198dceefbd1e89b": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 27", "subsampling": ""}
    ],
    "85adcc8c52c25334a9e7ea9d79433f8d": [
        {"description": "Apple QuickTime, " "Quality 713 (70%)", "subsampling": "11"}
    ],
    "85fc5daf51e6cbb04352016c817e5714": [
        {"description": "Apple QuickTime, " "Quality 388 (38%)", "subsampling": "11"}
    ],
    "866b8adb1ce7c9dc0e58b7c1e013280f": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 16",
            "subsampling": "221111",
        }
    ],
    "866dd04cb0fe2e00cda7395162480117": [
        {"description": "FixFoto, Quality 0 or 1", "subsampling": ""}
    ],
    "866fcb1296d7da02b4ad31afb242f25f": [
        {"description": "Nikon Capture NX, " "Quality 4", "subsampling": "221111"}
    ],
    "86ab18d6c1359a424f303fcfd0930df2": [
        {
            "description": "Apple QuickTime, " "Quality 615 (60%)",
            "subsampling": "221111",
        }
    ],
    "86cfac24ca9f4ab254f882ad399ea758": [
        {"description": "Apple QuickTime, " "Quality 524 (51%)", "subsampling": "11"}
    ],
    "86e707c017682fe08213216d064b1b51": [
        {"description": "Apple QuickTime, " "Quality 653 (64%)", "subsampling": "11"}
    ],
    "86e7666b05bd1fc130fbf4b48f854288": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 88", "subsampling": ""}
    ],
    "8711d6e1c56049c0e643bc6cf19a735c": [
        {
            "description": "Apple QuickTime, " "Quality 838-839 (82%)",
            "subsampling": "11",
        }
    ],
    "876ec039f82e49b925b232843b4703d4": [
        {"description": "Apple QuickTime, " "Quality 591 (58%)", "subsampling": "11"}
    ],
    "877d03a5abf5b6c4ad03c39afd97f4a2": [
        {"description": "FixFoto, Quality 10", "subsampling": ""}
    ],
    "879b320cfd6e27b2e283b573483bda81": [
        {
            "description": "Apple QuickTime, " "Quality 476 (46%)",
            "subsampling": "221111",
        }
    ],
    "87d40f2e4dad34fa435c62af6817dc18": [
        {
            "description": "Apple QuickTime, " "Quality 652 (64%)",
            "subsampling": "221111",
        }
    ],
    "87eac5c1375cca9aa16eba0704616a7b": [
        {
            "description": "Apple QuickTime, " "Quality 648-649 (63%)",
            "subsampling": "11",
        }
    ],
    "87fb3c7402ba4edcda34b71696d2b0e3": [
        {
            "description": "Apple QuickTime, " "Quality 801 (78%)",
            "subsampling": "211111",
        }
    ],
    "88558d6e9a513ff713945bd60ed19cc7": [
        {"description": "Apple QuickTime, " "Quality 840 (82%)", "subsampling": "11"}
    ],
    "886374ceebcfd4dfed200b0b34b4baca": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "27 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 27",
            "subsampling": "111111",
        },
    ],
    "8887b718c97e0d80ed8d9a198387e2eb": [
        {"description": "ACD Systems Digital " "Imaging, Quality 68", "subsampling": ""}
    ],
    "88a2772be7b74a5a9b7ebbea28ddde47": [
        {
            "description": "Apple QuickTime, " "Quality 304 (30%)",
            "subsampling": "221111",
        }
    ],
    "88b1726a20759f29eecfa2b129773127": [
        {"description": "Nikon Capture NX, " "Quality 29", "subsampling": "221111"}
    ],
    "88b94edfd7a6c7aadac520905e6cfa0a": [
        {
            "description": "Apple QuickTime, " "Quality 183-184 (18%)",
            "subsampling": "11",
        }
    ],
    "891a53bb6a5261a2c076cf8931c3660e": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "31",
            "subsampling": "",
        }
    ],
    "892788bdf8cbef5c6fbd7019a079bf8e": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "39 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 39",
            "subsampling": "111111",
        },
    ],
    "8a202c89c57e77f50e1df27a3be7d5b7": [
        {"description": "Apple QuickTime, " "Quality 613 (60%)", "subsampling": "11"}
    ],
    "8a2ae82991917070de49cc48d104446f": [
        {"description": "Apple QuickTime, " "Quality 675 (66%)", "subsampling": "11"}
    ],
    "8a4ff70dce3efc9312ff7239e79b6bc9": [
        {
            "description": "Apple QuickTime, " "Quality 764 (75%)",
            "subsampling": "221111",
        }
    ],
    "8a5df2b5337bf8251c3f66f6adbb5262": [
        {"description": "Apple Aperture Quality " "3", "subsampling": "221111"}
    ],
    "8a6ba56597670b7adb70901eca278049": [
        {
            "description": "Apple QuickTime, " "Quality 655 (64%)",
            "subsampling": "221111",
        }
    ],
    "8a8603650fa5ae5fdcf4b2eaf0b23638": [
        {
            "description": "Adobe Lightroom, " "Quality 54% - 61%",
            "subsampling": "111111",
        },
        {"description": "Adobe Photoshop, " "Quality 7", "subsampling": "111111"},
    ],
    "8a91452f2df82874183be50601242106": [
        {
            "description": "Apple QuickTime, " "Quality 425 (42%)",
            "subsampling": "221111",
        }
    ],
    "8a983844f9b0aec26fc8ac75a258e3ac": [
        {"description": "Apple QuickTime, " "Quality 606 (59%)", "subsampling": "11"}
    ],
    "8ab1119f4ed4941736cb8ec1796f5674": [
        {
            "description": "Canon Digital Photo " "Professional, Quality 4",
            "subsampling": "211111",
        }
    ],
    "8ab83dc2e7ca8b9db1f3b0ab500f3aca": [
        {"description": "Apple QuickTime, " "Quality 630 (62%)", "subsampling": "11"}
    ],
    "8ae7d2b569c437904a20a10bbd21fe89": [
        {"description": "Apple QuickTime, " "Quality 588 (57%)", "subsampling": "11"}
    ],
    "8b1138e2d88033d42698a386a2e8605b": [
        {
            "description": "Apple QuickTime, " "Quality 686 (67%)",
            "subsampling": "221111",
        }
    ],
    "8b1d11d31bc9445278cf9af55b0c156b": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 32", "subsampling": ""}
    ],
    "8b8dc34912d8b18742a7670be4b1c867": [
        {
            "description": "Apple QuickTime, " "Quality 400 (39%)",
            "subsampling": "221111",
        }
    ],
    "8b9e19fe69d7c7e1989018aca76c0aea": [
        {"description": "Apple QuickTime, " "Quality 299 (29%)", "subsampling": "11"}
    ],
    "8baa876790518bf509dd09093759331d": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 90", "subsampling": ""}
    ],
    "8bc267b04a54c02fdee1f4fdf0bcce83": [
        {
            "description": "Canon EOS " "1DmkIII/5DmkII/40D/1000D, " "Fine",
            "subsampling": "211111",
        }
    ],
    "8bc4e4bec8e9b193c11ad90c7f8bfaf3": [
        {
            "description": "Apple QuickTime, " "Quality 826 (81%)",
            "subsampling": "211111",
        }
    ],
    "8bc7e3b8f24507e284075ebeb272c3f4": [
        {
            "description": "Apple QuickTime, " "Quality 143-146 (14%)",
            "subsampling": "11",
        }
    ],
    "8bd486eb557ae8f39948775aba222731": [
        {
            "description": "Apple QuickTime, " "Quality 825 (81%)",
            "subsampling": "211111",
        }
    ],
    "8bda9fb1ed75249ac5b2feaad7b51d2f": [
        {
            "description": "Apple QuickTime, " "Quality 485 (47%)",
            "subsampling": "221111",
        }
    ],
    "8c0c36696a99fd889e0f0c7d64824f3c": [
        {"description": "Apple Aperture Quality " "8", "subsampling": "221111"}
    ],
    "8c0e1d4cd6138817963af6ca149cb5d5": [
        {"description": "Apple QuickTime, " "Quality 549 (54%)", "subsampling": "11"}
    ],
    "8c0ea132cfacf212c518ad297229be34": [
        {"description": "Apple QuickTime, " "Quality 422 (41%)", "subsampling": "11"}
    ],
    "8c105b3669931607853fa5ba4fffb839": [
        {"description": "Panasonic DMC-FZ30, " "High (D)", "subsampling": "211111"}
    ],
    "8c1fead15819016583650eff5a4f5bda": [
        {"description": "Apple QuickTime, " "Quality 570 (56%)", "subsampling": "11"}
    ],
    "8c372e99fa96d2598e431f8137e47da6": [
        {"description": "Apple QuickTime, " "Quality 426 (42%)", "subsampling": "11"}
    ],
    "8c389c29eca238b3b331f65f7e124a27": [
        {"description": "Nikon Capture NX, " "Quality 80", "subsampling": "111111"}
    ],
    "8c482fe6aef2a59a94cb779e6795e512": [
        {
            "description": "Apple QuickTime, " "Quality 836 (82%)",
            "subsampling": "211111",
        }
    ],
    "8c5c788bd53945222fc98f1a6155004c": [
        {"description": "Apple QuickTime, " "Quality 762 (74%)", "subsampling": "11"}
    ],
    "8c85462b5a01db09bcbf304d7be1d543": [
        {
            "description": "Apple QuickTime, " "Quality 657 (64%)",
            "subsampling": "221111",
        }
    ],
    "8c85e0e8f41257e2cd739a5b158ec218": [
        {
            "description": "ACD Systems Digital " "Imaging, Quality 20 or " "21",
            "subsampling": "",
        }
    ],
    "8c89043f00678bb5c68ee90390c1b43b": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 80", "subsampling": ""}
    ],
    "8cb101a5ae986e45cc31a9e19a35535d": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 65", "subsampling": ""}
    ],
    "8cb1bb16c6fa524199dad5513386d225": [
        {
            "description": "Apple QuickTime, " "Quality 461 (45%)",
            "subsampling": "221111",
        }
    ],
    "8cbf6cda8ae0249fb91c1ff5ab788a04": [
        {"description": "Apple QuickTime, " "Quality 686 (67%)", "subsampling": "11"}
    ],
    "8cc04e05813c028683e3cb8e6eab79eb": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "83",
            "subsampling": "",
        }
    ],
    "8cdb9100cfbb246d440d469e72ce37a6": [
        {"description": "ACD Systems Digital " "Imaging, Quality 69", "subsampling": ""}
    ],
    "8d0663f8149a308365e18bdeb8c867e8": [
        {"description": "Apple QuickTime, " "Quality 350 (34%)", "subsampling": "11"}
    ],
    "8d0fed09156984328f90f9f19fb5a079": [
        {
            "description": "Apple QuickTime, " "Quality 706 (69%)",
            "subsampling": "221111",
        }
    ],
    "8d14598ae9cc1b7f5357424a19d05a71": [
        {"description": "Pentax Optio A30/A40, " "Good", "subsampling": "211111"}
    ],
    "8d2f02a07bad6b5cec48466036fef319": [
        {"description": "Pentax Optio 550, " "Better", "subsampling": "121111"}
    ],
    "8d3b678651ec71f27e3727718123f354": [
        {
            "description": "Apple QuickTime, " "Quality 932-933 (91%)",
            "subsampling": "211111",
        }
    ],
    "8d4b2a14a176d63e509684aa4246dabb": [
        {
            "description": "Apple QuickTime, " "Quality 1010-1013 (99%)",
            "subsampling": "11",
        }
    ],
    "8d4f697b3a2baaecc8765f31f54a76ae": [
        {
            "description": "Apple QuickTime, " "Quality 219-220 (21%)",
            "subsampling": "11",
        }
    ],
    "8d8fab3b6b7386a4e81f10c15a7abaa5": [
        {
            "description": "Apple QuickTime, " "Quality 373 (36%)",
            "subsampling": "221111",
        }
    ],
    "8d9edea9287aa919e433b620f61468dc": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 11",
            "subsampling": "221111",
        }
    ],
    "8daf4a87b28106876529a549cf1040b8": [
        {"description": "Apple QuickTime, " "Quality 582 (57%)", "subsampling": "11"}
    ],
    "8dc4cff27c3c5196b4bc8905ef32f119": [
        {"description": "Apple QuickTime, " "Quality 241 (24%)", "subsampling": "11"}
    ],
    "8dc8361e94137f5466c8dd1f9aa06781": [
        {"description": "Apple QuickTime, " "Quality 463 (45%)", "subsampling": "11"}
    ],
    "8e1ceace8fafe31282393d8677e76994": [
        {"description": "Nikon Capture NX, " "Quality 82", "subsampling": "111111"}
    ],
    "8e2a66454fb149552d4538d53ec033aa": [
        {
            "description": "Apple QuickTime, " "Quality 588 (57%)",
            "subsampling": "221111",
        }
    ],
    "8e3cfc2fc9cfbba0f6aed9850504ebb6": [
        {
            "description": "Apple QuickTime, " "Quality 556 (54%)",
            "subsampling": "221111",
        }
    ],
    "8e4f695afcf2a06254561e5e22b7a80b": [
        {
            "description": "Apple QuickTime, " "Quality 662 (65%)",
            "subsampling": "221111",
        }
    ],
    "8e5290b1d12832ad259de92a53e1ef4e": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 87",
            "subsampling": "111111",
        }
    ],
    "8e54abf2320cca661b6dd67b7658c9f3": [
        {
            "description": "Apple QuickTime, " "Quality 422 (41%)",
            "subsampling": "221111",
        }
    ],
    "8e763b5b9255df1f4cb7b9732e99c210": [
        {"description": "ACD Systems Digital " "Imaging, Quality 4", "subsampling": ""}
    ],
    "8ecfb959bc76e5d6703f3f3bba2c5529": [
        {"description": "Panasonic DMC-FZ30, " "High (E)", "subsampling": "211111"}
    ],
    "8edf0677ca6be750511593fad835bbb5": [
        {
            "description": "Apple QuickTime, " "Quality 102-109 " "(10-11%)",
            "subsampling": "11",
        }
    ],
    "8ef467e72e5006d1b48209e7b5d94541": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "11",
            "subsampling": "",
        }
    ],
    "8efda55d6186d9867189c5cb572c5413": [
        {
            "description": "Apple QuickTime, " "Quality 637 (62%)",
            "subsampling": "221111",
        }
    ],
    "8f0f54955cf19689f38df36715908b76": [
        {
            "description": "Apple QuickTime, " "Quality 448 (44%)",
            "subsampling": "221111",
        }
    ],
    "8f2f9e8433104cedb50c3e54577fcd00": [
        {
            "description": "Apple QuickTime, " "Quality 349 (34%)",
            "subsampling": "221111",
        }
    ],
    "8f699e4439175f5f0cf0f903040fb3c5": [
        {
            "description": "Apple QuickTime, " "Quality 128-133 (13%)",
            "subsampling": "11",
        }
    ],
    "8f70e4a31ad4584043ddc655eca17e89": [
        {"description": "Pentax K10D (M)", "subsampling": "211111"}
    ],
    "8f72f67948f264bdbd33107c33b1e0a0": [
        {"description": "Apple QuickTime, " "Quality 714 (70%)", "subsampling": "11"}
    ],
    "8f96a0f2af7f1f1b0b2d4895bced1326": [
        {"description": "Apple QuickTime, " "Quality 295 (29%)", "subsampling": "11"}
    ],
    "8fb05e3c3b0a7404ff6ca54f952d2a5e": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 40",
            "subsampling": "221111",
        }
    ],
    "8fb281fcf4d481e59e1c15ed51ef8f19": [
        {"description": "Apple QuickTime, " "Quality 864 (84%)", "subsampling": "11"}
    ],
    "8fbb8cc5368224625689df80bf4d2a04": [
        {"description": "FixFoto, Quality 5", "subsampling": ""}
    ],
    "8fc0325d05c9199bc1e2dec417c3a55e": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 65",
            "subsampling": "111111",
        }
    ],
    "8fe3845bafb06ee4de1a6f75c2a42e9b": [
        {
            "description": "Apple QuickTime, " "Quality 931 (91%)",
            "subsampling": "211111",
        }
    ],
    "8ff6f2d4369155b0474417b00c3c4ac9": [
        {
            "description": "Apple QuickTime, " "Quality 677 (66%)",
            "subsampling": "221111",
        }
    ],
    "900fee18a5f6d1dc3fd856d3d92f5414": [
        {
            "description": "Apple QuickTime, " "Quality 598 (58%)",
            "subsampling": "221111",
        }
    ],
    "904f231c98f390400ba7ae17c252813f": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 24", "subsampling": ""}
    ],
    "905a0b1688644902f6a65d872d68a9db": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "49",
            "subsampling": "",
        }
    ],
    "9060906039e9ff37171ba48d908f6ad5": [
        {
            "description": "Apple QuickTime, " "Quality 923-924 (90%)",
            "subsampling": "211111",
        }
    ],
    "907e599e3c462b498e936dfc35b20bb9": [
        {
            "description": "Apple QuickTime, " "Quality 703-704 (69%)",
            "subsampling": "11",
        }
    ],
    "90d39fd222f9114f613a315a894283ca": [
        {
            "description": "Apple QuickTime, " "Quality 774 (76%)",
            "subsampling": "211111",
        }
    ],
    "90d3c964eaf6e4bd12cf5ca791a7d753": [
        {"description": "Pentax K10D (N)", "subsampling": "211111"}
    ],
    "90d96923be1883e6ee15a9d0d32a114c": [
        {
            "description": "Apple QuickTime, " "Quality 553 (54%)",
            "subsampling": "221111",
        }
    ],
    "90ece7123e8d614d9aab55eaba6dd7da": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 47", "subsampling": ""}
    ],
    "910416483a49503202cbe3ecee33afc9": [
        {"description": "Apple QuickTime, " "Quality 678 (66%)", "subsampling": "11"}
    ],
    "911e66f21fe242cc74e0a5738b0330bd": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 14",
            "subsampling": "221111",
        }
    ],
    "912779b5b7c935f2b533af0f400402f3": [
        {
            "description": "Apple QuickTime, " "Quality 369 (36%)",
            "subsampling": "221111",
        }
    ],
    "9127f8ddd20e583523bc848e99061126": [
        {
            "description": "Apple QuickTime, " "Quality 490 (48%)",
            "subsampling": "221111",
        }
    ],
    "912804912a3914f0b470b29495810d8c": [
        {
            "description": "Apple QuickTime, " "Quality 756-758 (74%)",
            "subsampling": "11",
        }
    ],
    "9146c5df73615b0f2a470521bab7e4c4": [
        {"description": "Apple QuickTime, " "Quality 866 (85%)", "subsampling": "11"}
    ],
    "9155c8acf8322e8af898272c694fa1d6": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 55", "subsampling": ""}
    ],
    "9160a8eeb898a05dcb02206603a45a65": [
        {
            "description": "Apple QuickTime, " "Quality 873-877 " "(85-86%)",
            "subsampling": "11",
        }
    ],
    "916225049ab8d411a5e0138ea9087e37": [
        {"description": "Apple QuickTime, " "Quality 313 (31%)", "subsampling": "11"}
    ],
    "916b16f020b2b21e4c8114da8c05d584": [
        {"description": "Apple QuickTime, " "Quality 501 (49%)", "subsampling": "11"}
    ],
    "917fe67f6ded5decac1820642239622c": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 71", "subsampling": ""}
    ],
    "91885755c780ebe16b1278a0359eda83": [
        {"description": "Apple QuickTime, " "Quality 621 (61%)", "subsampling": "11"}
    ],
    "919a38ebb9fc0bcba388643a9b3ef27c": [
        {"description": "Apple QuickTime, " "Quality 680 (66%)", "subsampling": "11"}
    ],
    "91a7f0747ed633f481918a83b1a7c77c": [
        {
            "description": "Apple QuickTime, " "Quality 909-914 (89%)",
            "subsampling": "11",
        }
    ],
    "91bd468ca96fe548a7df9646b51880d1": [
        {
            "description": "Apple QuickTime, " "Quality 314 (31%)",
            "subsampling": "221111",
        }
    ],
    "91c1b36d4411306ba3afaea0658f1ad8": [
        {"description": "Apple QuickTime, " "Quality 346 (34%)", "subsampling": "11"}
    ],
    "91c7f694fbf07321037a838c3a4d6e7d": [
        {
            "description": "Apple QuickTime, " "Quality 370 (36%)",
            "subsampling": "221111",
        }
    ],
    "91c9d96e11d96e10b328a5f18960247b": [
        {"description": "Apple QuickTime, " "Quality 698 (68%)", "subsampling": "11"}
    ],
    "91d7b4300c98c726aff7b19cbe098a3e": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 67",
            "subsampling": "111111",
        }
    ],
    "91dfacd928ce717cb135c6da03afd907": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 49",
            "subsampling": "221111",
        }
    ],
    "92044affd220e31ee953aff021144b29": [
        {
            "description": "Apple QuickTime, " "Quality 539 (53%)",
            "subsampling": "221111",
        }
    ],
    "9205cc28769d94d6d00c25804ac70a88": [
        {
            "description": "Apple QuickTime, " "Quality 576 (56%)",
            "subsampling": "221111",
        }
    ],
    "925b6581f0ae2f288530b00168152b80": [
        {"description": "Apple QuickTime, " "Quality 825 (81%)", "subsampling": "11"}
    ],
    "92658d4c879d6e48bfda1a6e9f49ef8d": [
        {"description": "Apple QuickTime, " "Quality 543 (53%)", "subsampling": "11"}
    ],
    "9282a1cec6bbd1232b3673091164d43d": [
        {"description": "Pentax K10D (AG)", "subsampling": "211111"}
    ],
    "92a9e0d027a1b2e5f7e49f7ffd96277e": [
        {
            "description": "Apple QuickTime, " "Quality 838-839 (82%)",
            "subsampling": "211111",
        }
    ],
    "92c1557deaa14f1cdaf92cf0531487f1": [
        {"description": "Canon EOS 1D/1DS, Fine", "subsampling": "121111"}
    ],
    "93173762094b6b506aa495e022ced65f": [
        {"description": "Apple QuickTime, " "Quality 338 (33%)", "subsampling": "11"}
    ],
    "9366dde6c37f4cac36a8e8cea4d5f51c": [
        {
            "description": "Apple QuickTime, " "Quality 405 (40%)",
            "subsampling": "221111",
        }
    ],
    "93818f3a0e6d491500cb62e1f683da22": [
        {"description": "Apple Aperture Quality " "7", "subsampling": "221111"}
    ],
    "939b804eefc95158a934bb48e3f3b545": [
        {"description": "Nikon Capture NX, " "Quality 46", "subsampling": "221111"}
    ],
    "93b4929d4a3b955f4996ab7e3b6fbe53": [
        {"description": "ACD Systems Digital " "Imaging, Quality 62", "subsampling": ""}
    ],
    "93c1ba0af1f50d889cb5e2364be3a056": [
        {"description": "Apple QuickTime, " "Quality 929 (91%)", "subsampling": "11"}
    ],
    "93d7ac97a931be74c7fe849edc482ea1": [
        {
            "description": "Apple QuickTime, " "Quality 782 (76%)",
            "subsampling": "211111",
        }
    ],
    "93e725418f46b2a70723523bef0979fe": [
        {
            "description": "Apple QuickTime, " "Quality 611 (60%)",
            "subsampling": "221111",
        }
    ],
    "93ef48999d5659763a33c45a2a0fa784": [
        {
            "description": "Apple QuickTime, " "Quality 177-179 (17%)",
            "subsampling": "221111",
        }
    ],
    "9438633929a283aac168f415d8ca44d6": [
        {"description": "Apple QuickTime, " "Quality 330 (32%)", "subsampling": "11"}
    ],
    "9440b11ee5eb970a3ea6de9353099761": [
        {"description": "Apple QuickTime, " "Quality 788 (77%)", "subsampling": "11"}
    ],
    "946d9f9346a0c65eec478945ad3d6143": [
        {"description": "Nikon Capture NX, " "Quality 41", "subsampling": "221111"}
    ],
    "94f6dbd754fb4ba3c92698d5f08084f9": [
        {
            "description": "Apple QuickTime, " "Quality 503 (49%)",
            "subsampling": "221111",
        }
    ],
    "9503a86793e86d1fca3d8797548fa243": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 40", "subsampling": ""}
    ],
    "9530dfffc5574606841a597212ec25b4": [
        {"description": "Nikon Capture NX, " "Quality 96", "subsampling": "111111"}
    ],
    "95348adff2bf5a88f3967e9237fc571e": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "60; Pentax Better",
            "subsampling": "",
        }
    ],
    "9570584f017ed2c4f0fb91782b51faa9": [
        {"description": "Pentax Optio M40/Z10, " "Best", "subsampling": "211111"}
    ],
    "958185c48000065b5b8d03b0f975d95b": [
        {
            "description": "Apple QuickTime, " "Quality 446 (44%)",
            "subsampling": "221111",
        }
    ],
    "95b6a316836182441b12039279872ec3": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "98",
            "subsampling": "",
        }
    ],
    "96076425ecc546ec028d0eab48332756": [
        {
            "description": "Apple QuickTime, " "Quality 735 (72%)",
            "subsampling": "221111",
        }
    ],
    "960caf85ef273541ac2e76c9554dc860": [
        {
            "description": "Apple QuickTime, " "Quality 903 (88%)",
            "subsampling": "211111",
        }
    ],
    "967aeb5bc4d75a0d5c0998bbfb282982": [
        {"description": "Apple QuickTime, " "Quality 571 (56%)", "subsampling": "11"}
    ],
    "967fc5c3ece2b69662257c76397416c9": [
        {
            "description": "Apple QuickTime, " "Quality 644 (63%)",
            "subsampling": "221111",
        }
    ],
    "96a267e050b6d8a13439f8a9bb89722c": [
        {"description": "Nikon Capture NX, " "Quality 43", "subsampling": "221111"}
    ],
    "96bce854134a2fccfcb68dca6687cd51": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 36",
            "subsampling": "221111",
        }
    ],
    "96c9e3cd827097ec03edc458fc1053e4": [
        {
            "description": "Apple QuickTime, " "Quality 320 (31%)",
            "subsampling": "221111",
        }
    ],
    "96eda111b2153648b3f27d6c1a9ec48f": [
        {"description": "Panasonic DMC-FZ50/TZ3, " "High (B)", "subsampling": "211111"}
    ],
    "9717c5a17cbffdfaa2e5d3769b87fbc5": [
        {
            "description": "Apple QuickTime, " "Quality 603 (59%)",
            "subsampling": "221111",
        }
    ],
    "97346edee67c3afea7823c72e57cb6c5": [
        {
            "description": "Apple QuickTime, " "Quality 381 (37%)",
            "subsampling": "221111",
        }
    ],
    "98201e1185b7069f1247ac3cdc56c824": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 64",
            "subsampling": "111111",
        }
    ],
    "982fc46fd167df238fbf23494a1ce761": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 93",
            "subsampling": "111111",
        }
    ],
    "984c0f34636e6197b508265f17cbd6c9": [
        {
            "description": "Apple QuickTime, " "Quality 456 (45%)",
            "subsampling": "221111",
        }
    ],
    "984c359b9fbcc4d6f805946aa23ae708": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 19", "subsampling": ""}
    ],
    "984d291debac8a0caeaccccea5fbfbdf": [
        {"description": "Apple QuickTime, " "Quality 230 (22%)", "subsampling": "11"}
    ],
    "9866add6e1d251e1d4c40793f4300dce": [
        {
            "description": "Apple QuickTime, " "Quality 571 (56%)",
            "subsampling": "221111",
        }
    ],
    "987ebcbd20b633b40241fcd30266e986": [
        {
            "description": "Apple QuickTime, " "Quality 777 (76%)",
            "subsampling": "211111",
        }
    ],
    "98abef3366c7f451e44f5c2799e2be6d": [
        {"description": "Apple QuickTime, " "Quality 502 (49%)", "subsampling": "11"}
    ],
    "98af13526b7e4bbf73a9fb11a8fa789d": [
        {
            "description": "Canon EOS 1DSmkII, Fine " "(vertical)",
            "subsampling": "121111",
        }
    ],
    "98b684f30055c84ba5734e29f7b98b5f": [
        {"description": "Apple QuickTime, " "Quality 218 (21%)", "subsampling": "11"}
    ],
    "98ddda3b0ada32ce919b9af9df4054dd": [
        {
            "description": "Apple QuickTime, " "Quality 559 (55%)",
            "subsampling": "221111",
        }
    ],
    "98dec36fe95ed7c1772d9ed67a67e260": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "85",
            "subsampling": "",
        }
    ],
    "98fddd9e5862e06385b46a016597c02f": [
        {
            "description": "Apple QuickTime, " "Quality 992-993 (97%)",
            "subsampling": "11",
        }
    ],
    "99458d7a01a39fe126592d9afb1402ce": [
        {
            "description": "Apple QuickTime, " "Quality 772 (75%)",
            "subsampling": "211111",
        }
    ],
    "994a9f2060976d95719ca7064be3a99c": [
        {"description": "Pentax K10D (0)", "subsampling": "211111"},
        {"description": "Pentax K10D/K20D (P)", "subsampling": "211111"},
    ],
    "99589fb7d66a29f15d9ff0f37235e7a2": [
        {
            "description": "Apple QuickTime, " "Quality 988-991 " "(96-97%)",
            "subsampling": "11",
        }
    ],
    "9971f02a466c47d640e8f20a2e4b55b9": [
        {"description": "Pentax K10D (Q)", "subsampling": "211111"}
    ],
    "99bf8158a4060d354b521f3d6f5648ac": [
        {
            "description": "Apple QuickTime, " "Quality 319 (31%)",
            "subsampling": "221111",
        }
    ],
    "99d933a8a9ece6f2ee65757aa81ef5bd": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "15",
            "subsampling": "",
        }
    ],
    "99f76923cfbd774febea883b603b8103": [
        {"description": "Panasonic DMC-FZ30, " "High (F)", "subsampling": "211111"}
    ],
    "9a26194b114b7db253601ff80b03da9a": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 34", "subsampling": ""}
    ],
    "9a43fc0aa6223673c32a49fb76d6525c": [
        {
            "description": "Apple QuickTime, " "Quality 473 (46%)",
            "subsampling": "221111",
        }
    ],
    "9a7ebf265afce16abaa6ca2fbb550b63": [
        {
            "description": "Apple QuickTime, " "Quality 705 (69%)",
            "subsampling": "221111",
        }
    ],
    "9a8a54328e297faa0a546c46145c9aa8": [
        {"description": "ACD Systems Digital " "Imaging, Quality 49", "subsampling": ""}
    ],
    "9aa9359126240c0712610121371f870c": [
        {
            "description": "Apple QuickTime, " "Quality 231-232 (23%)",
            "subsampling": "221111",
        }
    ],
    "9ab0afefad0e6bb7c3c1a8bca0c3f987": [
        {"description": "Apple QuickTime, " "Quality 289 (28%)", "subsampling": "11"}
    ],
    "9ac881c536e509675e5cf3795a85d9de": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 0",
            "subsampling": "221111",
        }
    ],
    "9ad6008e7b4f8478043bfa54e1d9e48e": [
        {"description": "Apple QuickTime, " "Quality 634 (62%)", "subsampling": "11"}
    ],
    "9ae3a57ce98290176c4700baaff5661f": [
        {"description": "ACD Systems Digital " "Imaging, Quality 84", "subsampling": ""}
    ],
    "9b1e6d379d3030dfa313bcaedc1ef3c7": [
        {"description": "Nikon Capture NX, " "Quality 10", "subsampling": "221111"}
    ],
    "9b2247e0f55b4485e7c55a04ee6a801c": [
        {
            "description": "Apple QuickTime, " "Quality 231-232 (23%)",
            "subsampling": "11",
        }
    ],
    "9b3475b865b9d31e433538460b75a588": [
        {"description": "Panasonic DMC-FZ10, " "High", "subsampling": "211111"}
    ],
    "9b62a9e4544cbc1033c67732ea0bbb08": [
        {
            "description": "Apple QuickTime, " "Quality 174-176 (17%)",
            "subsampling": "221111",
        }
    ],
    "9bade640c3fcb807ed1322479f9e7f1c": [
        {"description": "Apple QuickTime, " "Quality 427 (42%)", "subsampling": "11"}
    ],
    "9bda57f21c56ea0dc971164b8dc56394": [
        {"description": "Apple QuickTime, " "Quality 332 (32%)", "subsampling": "11"}
    ],
    "9be2446f168941ff42d9fc7441f2429b": [
        {"description": "Nikon Capture NX, " "Quality 61", "subsampling": "211111"}
    ],
    "9beb1b7c55129a34c850c359d7263457": [
        {"description": "Apple QuickTime, " "Quality 526 (51%)", "subsampling": "11"}
    ],
    "9bf86a5ec6e5382f214e07364a62b1b3": [
        {"description": "Apple QuickTime, " "Quality 481 (47%)", "subsampling": "11"}
    ],
    "9bfe788e7ae4bc9cbe76d36f9a2b1b5e": [
        {
            "description": "Apple QuickTime, " "Quality 591 (58%)",
            "subsampling": "221111",
        }
    ],
    "9c1865e7fdc0289dc5fe8f4c1f65577e": [
        {
            "description": "Apple QuickTime, " "Quality 393 (38%)",
            "subsampling": "221111",
        }
    ],
    "9c34d3dedfe47d95edabdcbc5568a2a8": [
        {"description": "Apple QuickTime, " "Quality 627 (61%)", "subsampling": "11"}
    ],
    "9c62dbc848be82ef91219ba9843998be": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "70 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 70",
            "subsampling": "111111",
        },
    ],
    "9c6f5faa1009cafe8bc3060fe18d4b60": [
        {"description": "Apple QuickTime, " "Quality 468 (46%)", "subsampling": "11"}
    ],
    "9cb9a256b6deb481cf13e5230fe87dbb": [
        {
            "description": "Apple QuickTime, " "Quality 618-619 (60%)",
            "subsampling": "221111",
        }
    ],
    "9cd85933ddb1101d9b859a19e9a30334": [
        {"description": "ACD Systems Digital " "Imaging, Quality 12", "subsampling": ""}
    ],
    "9ce50f6e0b00d2e601f2fcc151abc4d8": [
        {"description": "Apple QuickTime, " "Quality 529 (52%)", "subsampling": "11"}
    ],
    "9d125046484461bbc155d8eff6d4e8f0": [
        {
            "description": "Canon PowerShot, " "Superfine (A430/A460)",
            "subsampling": "211111",
        }
    ],
    "9d321ab2bdda6f3cb76d2d88838aa8c3": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "30 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 30",
            "subsampling": "111111",
        },
    ],
    "9d398f1b1f40b7aaec1bd9cdb6922530": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 69", "subsampling": ""}
    ],
    "9d4a8c44917390e56bca2352a8a4b1be": [
        {"description": "Apple QuickTime, " "Quality 378 (37%)", "subsampling": "11"}
    ],
    "9d765f3947408b2c6f26163d7b072895": [
        {"description": "Apple QuickTime, " "Quality 820 (80%)", "subsampling": "11"}
    ],
    "9d91481900305fb9ad09339f0924f690": [
        {
            "description": "Apple QuickTime, " "Quality 128-133 (13%)",
            "subsampling": "221111",
        }
    ],
    "9da4a7e310cb44578b009e78458d3b19": [
        {"description": "Apple QuickTime, " "Quality 869 (85%)", "subsampling": "11"}
    ],
    "9dbb8223620e7f25ca3292849f7aa025": [
        {
            "description": "Apple QuickTime, " "Quality 791-792 (77%)",
            "subsampling": "211111",
        }
    ],
    "9dd5c9717d0fd45486af4d26e59ebb35": [
        {
            "description": "Apple QuickTime, " "Quality 212-213 (21%)",
            "subsampling": "221111",
        }
    ],
    "9ddc6134fe65ea64048fdfd27c82bed7": [
        {"description": "Apple QuickTime, " "Quality 359 (35%)", "subsampling": "11"}
    ],
    "9df94f927ffc1f3345923232691fab3b": [
        {
            "description": "Apple QuickTime, " "Quality 918-920 (90%)",
            "subsampling": "11",
        }
    ],
    "9dfcc9ae3baee4bb4ad63abf2f740275": [
        {"description": "Apple QuickTime, " "Quality 508 (50%)", "subsampling": "11"}
    ],
    "9e048c787b12b9ab47d6166e81bc8bda": [
        {
            "description": "Apple QuickTime, " "Quality 809 (79%)",
            "subsampling": "211111",
        }
    ],
    "9e201a496a3700a77d9102c0dd0f8dbf": [
        {"description": "Nikon D300, Basic", "subsampling": "211111"}
    ],
    "9e334af92d75ab7d4ea1a9816840ea73": [
        {
            "description": "Apple QuickTime, " "Quality 486 (47%)",
            "subsampling": "221111",
        }
    ],
    "9e6abfb26d3b95b8cd2f710e78def947": [
        {"description": "Canon EOS 300D, Fine " "(vertical)", "subsampling": "121111"}
    ],
    "9e992f35767c4aa023b8afd243b247bf": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 22",
            "subsampling": "221111",
        }
    ],
    "9e9e3e22af4e41ea4ec1b8f656f28f42": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "96",
            "subsampling": "",
        }
    ],
    "9eb7cdfd07099c1bb8e2c6c04b20b8ba": [
        {"description": "Panasonic DMC-FZ30, " "High (G)", "subsampling": "211111"}
    ],
    "9ebd96ea70c2bcf4f377a175c71baf2c": [
        {"description": "Apple QuickTime, " "Quality 836 (82%)", "subsampling": "11"}
    ],
    "9ec2859c370f557783903608748e7fb1": [
        {"description": "Apple QuickTime, " "Quality 585 (57%)", "subsampling": "11"}
    ],
    "9ec82f50503769a9bb17e876594833b6": [
        {"description": "Apple QuickTime, " "Quality 419 (41%)", "subsampling": "11"}
    ],
    "9ed53fb5bc8e397daf9409251c0a0a6c": [
        {
            "description": "Apple QuickTime, " "Quality 651 (64%)",
            "subsampling": "221111",
        }
    ],
    "9f3289994c790a10ecb2d93021677840": [
        {"description": "Apple QuickTime, " "Quality 546 (53%)", "subsampling": "11"}
    ],
    "9f48e71f610caa47b94d3e474608cb3d": [
        {
            "description": "Apple QuickTime, " "Quality 440 (43%)",
            "subsampling": "221111",
        }
    ],
    "9f490145dcc00db3e57014d41d2f99f2": [
        {"description": "Apple QuickTime, " "Quality 818 (80%)", "subsampling": "11"}
    ],
    "9fa9c3d1041911322544aef0298695ba": [
        {"description": "Apple QuickTime, " "Quality 763 (75%)", "subsampling": "11"}
    ],
    "9fc030294fa5c4044dbb0cb461b0cf93": [
        {"description": "Panasonic DMC-TZ5, High " "(A)", "subsampling": "211111"}
    ],
    "9fee7fc42e670d6e30a5e9fcf696241d": [
        {"description": "Apple QuickTime, " "Quality 728 (71%)", "subsampling": "11"}
    ],
    "9ffb80389e2eed2301e6b07860c2fbd7": [
        {
            "description": "Apple QuickTime, " "Quality 841 (82%)",
            "subsampling": "211111",
        }
    ],
    "9fffe6b2fbbce23598c19e6cd177adb0": [
        {
            "description": "Apple QuickTime, " "Quality 375 (37%)",
            "subsampling": "221111",
        }
    ],
    "a01d3a7766c7c593a79ff6c63433860a": [
        {
            "description": "Apple QuickTime, " "Quality 377 (37%)",
            "subsampling": "221111",
        }
    ],
    "a02b6b8286cf6d036961911e98bd8f89": [
        {
            "description": "Apple QuickTime, " "Quality 718-719 (70%)",
            "subsampling": "11",
        }
    ],
    "a06d250213e349005897bd6fa5bebca8": [
        {"description": "ACD Systems Digital " "Imaging, Quality 37", "subsampling": ""}
    ],
    "a0772e73dec2bdc4057c27da47bff376": [
        {
            "description": "Adobe Lightroom, " "Quality 31% - 38%",
            "subsampling": "221111",
        },
        {"description": "Adobe Photoshop, " "Quality 4", "subsampling": "221111"},
    ],
    "a08a6b6535f292518b5ff6d0d05ae187": [
        {
            "description": "Apple QuickTime, " "Quality 891-893 (87%)",
            "subsampling": "211111",
        }
    ],
    "a09ca4c4391e0221396a08f229a65f9d": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "61 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 61",
            "subsampling": "111111",
        },
    ],
    "a09fe2e60a7ff12e1e5ca00afa9719ef": [
        {"description": "Apple QuickTime, " "Quality 683 (67%)", "subsampling": "11"}
    ],
    "a0a30c816d5d47a91c66e5645eb5fdb8": [
        {"description": "ACD Systems Digital " "Imaging, Quality 74", "subsampling": ""}
    ],
    "a0a7061bc100f051a3c5470559661138": [
        {
            "description": "Apple QuickTime, " "Quality 501 (49%)",
            "subsampling": "221111",
        }
    ],
    "a0c4d0114c04c89c879d9dc03463b347": [
        {"description": "Apple QuickTime, " "Quality 779 (76%)", "subsampling": "11"}
    ],
    "a1085c167f1cd610258fe38c8a84a8b9": [
        {
            "description": "Canon Digital Photo " "Professional, Quality 3",
            "subsampling": "211111",
        }
    ],
    "a10e87fa030f8177a4f59f8d16a20afd": [
        {"description": "Apple QuickTime, " "Quality 658 (64%)", "subsampling": "11"}
    ],
    "a15a74418a924874c5f3d2ca20e7af90": [
        {
            "description": "Apple QuickTime, " "Quality 846-849 (83%)",
            "subsampling": "11",
        }
    ],
    "a16371762ce48953d42dfb5b77d1bfc6": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 77",
            "subsampling": "111111",
        }
    ],
    "a16626c285e5a2290d331f99f4eec774": [
        {"description": "Pentax K10D (R)", "subsampling": "211111"}
    ],
    "a1664b510ce4c6aa3588cdbc327a6f57": [
        {"description": "Apple QuickTime, " "Quality 343 (33%)", "subsampling": "11"}
    ],
    "a16e53aa41aa66124557c0b976d73734": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "55",
            "subsampling": "",
        }
    ],
    "a1a8f92dc00c42877eb9a1d7462f8408": [
        {"description": "Apple QuickTime, " "Quality 311 (30%)", "subsampling": "11"}
    ],
    "a1ee06d19dcb62c7467768d1ba73cf12": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "86",
            "subsampling": "",
        }
    ],
    "a295b7163305f327a5a45ae177a0a19c": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "23 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 23",
            "subsampling": "111111",
        },
    ],
    "a2b6067d9e5731be8029e17c00d7e043": [
        {"description": "Apple QuickTime, " "Quality 770 (75%)", "subsampling": "11"}
    ],
    "a2d1de53a0882047287a954f86bc783d": [
        {"description": "Apple QuickTime, " "Quality 691 (67%)", "subsampling": "11"}
    ],
    "a2e3baa02454492ef811619ac18c65da": [
        {
            "description": "Apple QuickTime, " "Quality 123-127 (12%)",
            "subsampling": "11",
        }
    ],
    "a2e7b219d18177294378485759215f72": [
        {
            "description": "Apple QuickTime, " "Quality 282 (28%)",
            "subsampling": "221111",
        }
    ],
    "a2f2a404cd1c2278ef65f2a27c0365e0": [
        {
            "description": "Apple QuickTime, " "Quality 347 (34%)",
            "subsampling": "221111",
        }
    ],
    "a2f4b6ac52f87791380bdfe38ae333e1": [
        {
            "description": "Canon Digital Photo " "Professional, Quality 6",
            "subsampling": "211111",
        }
    ],
    "a333be9f2b13b53bfdf64bf5665f8e55": [
        {
            "description": "Apple QuickTime, " "Quality 221-222 (22%)",
            "subsampling": "221111",
        }
    ],
    "a36199f5a090de94b10a32fbe05f2916": [
        {
            "description": "Apple QuickTime, " "Quality 688-689 (67%)",
            "subsampling": "221111",
        }
    ],
    "a3698813ce90772a30b6eb9a7deb3f4a": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 9",
            "subsampling": "221111",
        }
    ],
    "a371d1ffc8d85d502854a356f3b0ea74": [
        {"description": "FixFoto, Quality 6", "subsampling": ""}
    ],
    "a3a96add050fc51a2b3ce59a9a491034": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "92 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 92",
            "subsampling": "111111",
        },
    ],
    "a3ba20f325ff36f874d633919185f92d": [
        {
            "description": "Apple QuickTime, " "Quality 789 (77%)",
            "subsampling": "211111",
        }
    ],
    "a3bb9728b3dfa7002364659db0c420fc": [
        {
            "description": "Apple QuickTime, " "Quality 915-917 " "(89-90%)",
            "subsampling": "11",
        }
    ],
    "a3c40b635e584c8f49d6b6b110846fee": [
        {
            "description": "Apple QuickTime, " "Quality 291-292 " "(28-29%)",
            "subsampling": "11",
        }
    ],
    "a3e2cc4ea95cda49501bc73c494e9420": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 79", "subsampling": ""}
    ],
    "a431976a61e281e7b9d808f094b74d2e": [
        {
            "description": "Apple QuickTime, " "Quality 587 (57%)",
            "subsampling": "221111",
        }
    ],
    "a439b365c2d0cf1fbaad2e42d331d759": [
        {
            "description": "Apple QuickTime, " "Quality 894 (87%)",
            "subsampling": "211111",
        }
    ],
    "a43b370edaaee853bb16e46ee4a002e8": [
        {
            "description": "Apple QuickTime, " "Quality 383 (37%)",
            "subsampling": "221111",
        }
    ],
    "a451c79ccddcd543a80e1ce0449dcb0d": [
        {"description": "Apple QuickTime, " "Quality 536 (52%)", "subsampling": "11"}
    ],
    "a455a3149812ba6951a016ee6114f9da": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 76", "subsampling": ""}
    ],
    "a4680e71907e5c6f7b18e20e46286412": [
        {
            "description": "Apple QuickTime, " "Quality 421 (41%)",
            "subsampling": "221111",
        }
    ],
    "a4683813bdf6e2bd429c4c5676128384": [
        {
            "description": "Apple QuickTime, " "Quality 555 (54%)",
            "subsampling": "221111",
        }
    ],
    "a4b8b3408ae302ae81f125e972901131": [
        {"description": "Nikon Capture NX, " "Quality 6", "subsampling": "221111"}
    ],
    "a4bfd80e0c8b9ae7a1114d79a7b63ad6": [
        {
            "description": "Apple QuickTime, " "Quality 525 (51%)",
            "subsampling": "221111",
        }
    ],
    "a4cb8a3a000484b37c4373cde1170091": [
        {
            "description": "Pentax Optio " "A30/A40/S10/S12, Best",
            "subsampling": "211111",
        }
    ],
    "a4ecd6b77f06671530942783c3595aca": [
        {"description": "Pentax Optio A20, Best", "subsampling": "211111"}
    ],
    "a50ff29c6c2a7e73f742ca94678956ba": [
        {
            "description": "Apple QuickTime, " "Quality 151-154 (15%)",
            "subsampling": "11",
        }
    ],
    "a53a7d4cc86d01f4c1b867270c9c078f": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "34 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 34",
            "subsampling": "111111",
        },
    ],
    "a56edeb9e571dc790a429c26ebc59976": [
        {
            "description": "Apple QuickTime, " "Quality 355 (35%)",
            "subsampling": "221111",
        }
    ],
    "a582968bb1890620ffbae916ebafcb64": [
        {"description": "Nikon Capture NX, " "Quality 56", "subsampling": "221111"}
    ],
    "a5894172d7ec5f0c1550934c9e9385c9": [
        {
            "description": "Canon Digital Photo " "Professional, Quality 9",
            "subsampling": "211111",
        }
    ],
    "a589d880de576ed888c57814ccea47a0": [
        {
            "description": "Apple QuickTime, " "Quality 844 (82%)",
            "subsampling": "211111",
        }
    ],
    "a595c40b5dbd45557c3c8d23ebee5e24": [
        {"description": "Apple QuickTime, " "Quality 577 (56%)", "subsampling": "11"}
    ],
    "a5b4bbf018828a3d00e54ab72a175fdc": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "89",
            "subsampling": "",
        }
    ],
    "a5bcbd80472fdf697db770ac78d6a4e3": [
        {"description": "Apple QuickTime, " "Quality 603 (59%)", "subsampling": "11"}
    ],
    "a5cd2d8592e1c45b67cfb3009d07fb49": [
        {
            "description": "Apple QuickTime, " "Quality 492 (48%)",
            "subsampling": "221111",
        }
    ],
    "a5da49ac5bfe27aafda44bae107ae1c5": [
        {
            "description": "Apple QuickTime, " "Quality 230 (22%)",
            "subsampling": "221111",
        }
    ],
    "a5e5355ae60c569dec306eb971a49276": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "46",
            "subsampling": "",
        }
    ],
    "a5f724e9d7148f1a84ee597f45c33141": [
        {"description": "Apple QuickTime, " "Quality 644 (63%)", "subsampling": "11"}
    ],
    "a60bbd6538af00192c411020d7494a1d": [
        {
            "description": "Apple QuickTime, " "Quality 897-898 (88%)",
            "subsampling": "211111",
        }
    ],
    "a62fb887c209e0fab99fcb7ac81137a2": [
        {"description": "Apple QuickTime, " "Quality 632 (62%)", "subsampling": "11"}
    ],
    "a64569d6387a118992e44e41aaeac27e": [
        {"description": "Pentax K10D (S)", "subsampling": "211111"}
    ],
    "a65113fd3b66ef137f9b1144367f731b": [
        {
            "description": "Apple QuickTime, " "Quality 299 (29%)",
            "subsampling": "221111",
        }
    ],
    "a670182cd48f37dd16652db878791a7a": [
        {
            "description": "Apple QuickTime, " "Quality 426 (42%)",
            "subsampling": "221111",
        }
    ],
    "a6841b35e9ffefa5d83a0445dddd2621": [
        {
            "description": "Adobe Lightroom, " "Quality 77% - 84%",
            "subsampling": "111111",
        },
        {"description": "Adobe Photoshop, " "Quality 10", "subsampling": "111111"},
    ],
    "a68893776502a591548c7b5bece13e1b": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "25 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 25",
            "subsampling": "111111",
        },
    ],
    "a6a49ea0300157ecb401ce45d7f1f850": [
        {"description": "Apple QuickTime, " "Quality 303 (30%)", "subsampling": "11"}
    ],
    "a6c15a75ab70e28c78e6084f909523bf": [
        {
            "description": "Apple QuickTime, " "Quality 188-189 (18%)",
            "subsampling": "11",
        }
    ],
    "a6c4a173169d168e003839e51f035661": [
        {
            "description": "Apple QuickTime, " "Quality 722 (71%)",
            "subsampling": "221111",
        }
    ],
    "a6df2748a4972d4323f0386820ce35a4": [
        {
            "description": "Apple QuickTime, " "Quality 840 (82%)",
            "subsampling": "211111",
        }
    ],
    "a748fdfe8d6dc9493253908410e517eb": [
        {
            "description": "Apple QuickTime, " "Quality 415 (41%)",
            "subsampling": "221111",
        }
    ],
    "a78fd0f1183b268b2fdfa23308c3ad44": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "67",
            "subsampling": "",
        }
    ],
    "a79e66299883be78b02ceaaf9159c320": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "41",
            "subsampling": "",
        }
    ],
    "a7e85552c3e5e40288891d225f308590": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 49", "subsampling": ""}
    ],
    "a8055a53fda7f9a0e387026c81960aa4": [
        {"description": "Pentax K10D (T)", "subsampling": "211111"}
    ],
    "a873e49b871c32bcaf8e3c6622744e70": [
        {
            "description": "Apple QuickTime, " "Quality 690 (67%)",
            "subsampling": "221111",
        }
    ],
    "a8779af4cb8afa2def1d346a9b16e81a": [
        {"description": "Panasonic DMC-TZ5, High " "(B)", "subsampling": "211111"}
    ],
    "a8780d0f85eef638c6a448e57b157378": [
        {
            "description": "Apple QuickTime, " "Quality 978-979 (96%)",
            "subsampling": "211111",
        }
    ],
    "a88bad671d80cf6a70bd6e37be9c95c9": [
        {"description": "Apple QuickTime, " "Quality 380 (37%)", "subsampling": "11"}
    ],
    "a8b52e666bd3d81404c0f8915ac18b43": [
        {
            "description": "Apple QuickTime, " "Quality 573 (56%)",
            "subsampling": "221111",
        }
    ],
    "a8be3b3791e958d092b3e37286802e0c": [
        {
            "description": "Apple QuickTime, " "Quality 811-813 (79%)",
            "subsampling": "11",
        }
    ],
    "a8ecf55a88fd0e1b29646207aff8c36f": [
        {"description": "Apple QuickTime, " "Quality 301 (29%)", "subsampling": "11"}
    ],
    "a8f8928c72b69049e1da7639e977c9c7": [
        {
            "description": "Apple QuickTime, " "Quality 557 (54%)",
            "subsampling": "221111",
        }
    ],
    "a91f5f8e8d743e52169d965992c5021e": [
        {"description": "Apple QuickTime, " "Quality 746 (73%)", "subsampling": "11"}
    ],
    "a92912eb3c81e5c873d49433264af842": [
        {
            "description": "Canon EOS " "30D/40D/50D/300D, " "Normal",
            "subsampling": "211111",
        }
    ],
    "a946498fd1902c9de87a1f5182966742": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "36 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 36",
            "subsampling": "111111",
        },
    ],
    "a97591462e9b2339efd4f88ca97bb471": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "100",
            "subsampling": "",
        }
    ],
    "a99810db58e835fe4b213d707dc0b754": [
        {"description": "Apple QuickTime, " "Quality 734 (72%)", "subsampling": "11"}
    ],
    "a99e2826c10d0922ce8942c5437f53a6": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "6 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 6",
            "subsampling": "111111",
        },
    ],
    "a9a0a5000cd6fb322960a4c45cf1d032": [
        {"description": "FixFoto, Quality 7", "subsampling": ""}
    ],
    "a9b2875fc3c21e7b998969c57f74fa7a": [
        {
            "description": "Apple QuickTime, " "Quality 296 (29%)",
            "subsampling": "221111",
        }
    ],
    "a9c018e06868989776a81650300bcfce": [
        {"description": "Apple QuickTime, " "Quality 821 (80%)", "subsampling": "11"}
    ],
    "a9cc8a19ae25bc024c3d92d84c13c7a5": [
        {"description": "ACD Systems Digital " "Imaging, Quality 34", "subsampling": ""}
    ],
    "a9f461d3bca42dfab57c834fa5f34419": [
        {"description": "Apple QuickTime, " "Quality 666 (65%)", "subsampling": "11"}
    ],
    "aa049fdc1387851a664143df0408f55c": [
        {"description": "Nikon Capture NX, " "Quality 34", "subsampling": "221111"}
    ],
    "aa05fbe795d86a1063c55865e8613536": [
        {"description": "Pentax Optio S, Best " "(D)", "subsampling": "221111"}
    ],
    "aa2d374bbab2a30e00c1863264588a42": [
        {"description": "Nikon Capture NX, " "Quality 31", "subsampling": "221111"}
    ],
    "aa4a5528ae18ecd36ec052014b91f651": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 33", "subsampling": ""}
    ],
    "aa5a427657696f05da789e1516b8c2ff": [
        {
            "description": "Apple QuickTime, " "Quality 206-207 (20%)",
            "subsampling": "11",
        }
    ],
    "aa5e05f96c53f6bc498f5016b1113651": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "28",
            "subsampling": "",
        }
    ],
    "aa6072a632f7bae361c8d371aa022c57": [
        {
            "description": "Apple QuickTime, " "Quality 343 (33%)",
            "subsampling": "221111",
        }
    ],
    "aa83fd556c569ddcd81e0cc1ba866373": [
        {"description": "Apple QuickTime, " "Quality 650 (63%)", "subsampling": "11"}
    ],
    "aa8940194463b7adc14f20dbee9c6a75": [
        {
            "description": "Apple QuickTime, " "Quality 497 (49%)",
            "subsampling": "221111",
        }
    ],
    "aaa2026d750590e466d9198f20b888e4": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "57",
            "subsampling": "",
        }
    ],
    "aaac84043224d33e1d3a1723b653b0cd": [
        {"description": "FixFoto, Quality 8", "subsampling": ""}
    ],
    "aac2510e3cd617eb2cd60e7dc6f5d252": [
        {
            "description": "Apple QuickTime, " "Quality 818 (80%)",
            "subsampling": "211111",
        }
    ],
    "aad0e2cd42c5adaec41080a05be4ffdc": [
        {
            "description": "Apple QuickTime, " "Quality 548 (54%)",
            "subsampling": "221111",
        }
    ],
    "aad1109d9c49b8170feac125148b2a50": [
        {"description": "Nikon Capture NX, " "Quality 25", "subsampling": "221111"}
    ],
    "aaf1ebc6949569327f95cf7da78ee7bc": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "39",
            "subsampling": "",
        }
    ],
    "ab2b6d0624f294bf4e53e34208caeaa6": [
        {"description": "Apple QuickTime, " "Quality 971 (95%)", "subsampling": "11"}
    ],
    "ab2f8513823067af242f7e3c04a88a9c": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "46 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 46",
            "subsampling": "111111",
        },
    ],
    "ab50a9f53a44ffecc54efe1cb7c6620a": [
        {"description": "Pentax K10D (U)", "subsampling": "211111"}
    ],
    "ab7cfb73667875854893982a8cfcfab9": [
        {"description": "Apple QuickTime, " "Quality 662 (65%)", "subsampling": "11"}
    ],
    "ab8fe796c87f9f61cedbfa64af9f5dec": [
        {
            "description": "Apple QuickTime, " "Quality 590 (58%)",
            "subsampling": "221111",
        }
    ],
    "ab975404bdb713bb6a58ac560330aaf1": [
        {
            "description": "Apple QuickTime, " "Quality 391 (38%)",
            "subsampling": "221111",
        }
    ],
    "abb56efe234d4b8fdf50016a19c63684": [
        {
            "description": "Apple QuickTime, " "Quality 411 (40%)",
            "subsampling": "221111",
        }
    ],
    "abdf532dc2005805db7d8d0214227146": [
        {
            "description": "Apple QuickTime, " "Quality 526 (51%)",
            "subsampling": "221111",
        }
    ],
    "ac015afc1d80314edd832aebfb495d25": [
        {
            "description": "Apple QuickTime, " "Quality 621 (61%)",
            "subsampling": "221111",
        }
    ],
    "ac25112c596d62f95518af109457975c": [
        {"description": "Apple QuickTime, " "Quality 615 (60%)", "subsampling": "11"}
    ],
    "ac2d99dd3ff609760c207419312e7b30": [
        {"description": "Apple QuickTime, " "Quality 867 (85%)", "subsampling": "11"}
    ],
    "ac2f66ab2559019fcf021b9a32b049ab": [
        {"description": "ACD Systems Digital " "Imaging, Quality 28", "subsampling": ""}
    ],
    "ac47d493602dddace7844a9bc962e5ed": [
        {"description": "Apple QuickTime, " "Quality 469 (46%)", "subsampling": "11"}
    ],
    "ac76c6ebb64c843736fc765a03674d94": [
        {"description": "Apple QuickTime, " "Quality 372 (36%)", "subsampling": "11"}
    ],
    "acc5e596cc4eb156b83eb89190b289a7": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "54",
            "subsampling": "",
        }
    ],
    "acd1d5ec1787c9d346d87c281a7b6da0": [
        {
            "description": "Apple QuickTime, " "Quality 464-465 (45%)",
            "subsampling": "221111",
        }
    ],
    "ad2221ee8bb94a3558ed16766efaec4f": [
        {
            "description": "Apple QuickTime, " "Quality 763 (75%)",
            "subsampling": "221111",
        }
    ],
    "ad3aad027e3829959ebeb6288bfab268": [
        {
            "description": "Apple QuickTime, " "Quality 727 (71%)",
            "subsampling": "221111",
        }
    ],
    "ad5399708089baad5891319303ba92df": [
        {
            "description": "Apple QuickTime, " "Quality 927 (91%)",
            "subsampling": "211111",
        }
    ],
    "ad801813f822ef9774801ab4d9145a61": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 57", "subsampling": ""}
    ],
    "ad8bbd6b23b87950d1b76278fbb7de87": [
        {
            "description": "Apple QuickTime, " "Quality 388 (38%)",
            "subsampling": "221111",
        }
    ],
    "adbb56f1f0e0392392f9c7a38351a9ec": [
        {"description": "Apple QuickTime, " "Quality 471 (46%)", "subsampling": "11"}
    ],
    "add779ad00786bd2ccb9dcc226386b1a": [
        {
            "description": "Apple QuickTime, " "Quality 988-991 " "(96-97%)",
            "subsampling": "211111",
        }
    ],
    "adf507352f9ce218a4605700459d597f": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "95",
            "subsampling": "",
        }
    ],
    "ae15629cecc940fef9f24ad9f207fa10": [
        {
            "description": "Apple QuickTime, " "Quality 510 (50%)",
            "subsampling": "221111",
        }
    ],
    "ae2efaf1a96a4fdcfa9003b9aa963ae4": [
        {"description": "Pentax Optio 330, Best " "(vertical)", "subsampling": "221111"}
    ],
    "ae39c8775a10e34accdf2bba3bffc483": [
        {
            "description": "Apple QuickTime, " "Quality 312 (30%)",
            "subsampling": "221111",
        }
    ],
    "ae3dd4568cc71c47d068cf831c66b59d": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "59 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 59",
            "subsampling": "111111",
        },
    ],
    "ae5c6eab0d57249acbcb8b1990b2602f": [
        {
            "description": "Apple QuickTime, " "Quality 737-738 (72%)",
            "subsampling": "221111",
        }
    ],
    "ae6c2112dd560530b7bacc8bfa9fb7f6": [
        {"description": "Apple QuickTime, " "Quality 623 (61%)", "subsampling": "11"}
    ],
    "ae9202355f603776794d3e62c43578d6": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "96 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 96",
            "subsampling": "111111",
        },
    ],
    "ae9de0a8343d730e2e6a358849c29a4e": [
        {
            "description": "Apple QuickTime, " "Quality 413 (40%)",
            "subsampling": "221111",
        }
    ],
    "aeaa2ca48eabb3088ebb713b3c4e1a67": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "55 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 55",
            "subsampling": "111111",
        },
    ],
    "aeb34eb083acc888770d65e691497bcf": [
        {
            "description": "Adobe Photoshop " "Express, Original Size",
            "subsampling": "111111",
        },
        {"description": "Canon ZoomBrowser, High", "subsampling": "211111"},
        {"description": "Sony Image Data Suite, " "Quality 2", "subsampling": "211111"},
        {"description": "Pentax K10D (V)", "subsampling": "211111"},
    ],
    "aee867276d6dc4ed4b682a454815acd1": [
        {
            "description": "Apple QuickTime, " "Quality 348 (34%)",
            "subsampling": "221111",
        }
    ],
    "af10133169e143a2b3634c48dede9440": [
        {
            "description": "Apple QuickTime, " "Quality 790 (77%)",
            "subsampling": "211111",
        }
    ],
    "af2a112c30fa29213a402dbd3c2b2d3a": [
        {"description": "Pentax K10D (W)", "subsampling": "211111"}
    ],
    "af683de3118ab595c41b5796b57a9540": [
        {"description": "Apple QuickTime, " "Quality 286 (28%)", "subsampling": "11"}
    ],
    "af6a08d0742aa8ed6bae2f1c374e7931": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "12",
            "subsampling": "",
        }
    ],
    "afb31cfed194d4e125bde8fd4755bb8a": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 20",
            "subsampling": "221111",
        }
    ],
    "afd16e145464c7c5a3cd703017b4ef7a": [
        {
            "description": "Apple QuickTime, " "Quality 928 (91%)",
            "subsampling": "211111",
        }
    ],
    "b008cd63591f8fd366f77d2b224b9c9c": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "80 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 80",
            "subsampling": "111111",
        },
    ],
    "b013b5c9b7bafc9dcad9a1e87fc629ff": [
        {"description": "Apple QuickTime, " "Quality 491 (48%)", "subsampling": "11"}
    ],
    "b0144b1d2671d145d29812ebcebd863d": [
        {"description": "Apple QuickTime, " "Quality 486 (47%)", "subsampling": "11"}
    ],
    "b015ada43293b8d5bd2a8f288f8fb928": [
        {
            "description": "Apple QuickTime, " "Quality 642 (63%)",
            "subsampling": "221111",
        }
    ],
    "b023f424f81c8cbbab20119c06163dce": [
        {"description": "Nikon Capture NX, " "Quality 91", "subsampling": "111111"}
    ],
    "b04cbc1812939770d59461982cd9d32d": [
        {
            "description": "Apple QuickTime, " "Quality 259 (25%)",
            "subsampling": "221111",
        }
    ],
    "b08313a6919d308e50b806f138a8a2a1": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 45", "subsampling": ""}
    ],
    "b08af3cffd1904e8a8cfbbba71077069": [
        {
            "description": "Apple QuickTime, " "Quality 410 (40%)",
            "subsampling": "221111",
        }
    ],
    "b095631a0665a515d9aa290639f6672b": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "76",
            "subsampling": "",
        }
    ],
    "b09abfa40fc6607dc26d8b5df48c72fc": [
        {
            "description": "Apple QuickTime, " "Quality 869 (85%)",
            "subsampling": "211111",
        }
    ],
    "b0a00ffee2e55457cd999bba2d07f63e": [
        {"description": "Apple QuickTime, " "Quality 636 (62%)", "subsampling": "11"}
    ],
    "b0a0fd1ec2dd366ad00d3e83d6dedec2": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 93", "subsampling": ""}
    ],
    "b0a501129cb83e54f97006610ec9ed64": [
        {
            "description": "Apple QuickTime, " "Quality 431 (42%)",
            "subsampling": "221111",
        }
    ],
    "b0c2c3f76d848ee2e8f47a9a90131a21": [
        {"description": "Apple QuickTime, " "Quality 625 (61%)", "subsampling": "11"}
    ],
    "b157c4aabba2816f391c8f76ca3d4072": [
        {"description": "Apple QuickTime, " "Quality 604 (59%)", "subsampling": "11"}
    ],
    "b163f35baed567d70aa2536695558724": [
        {"description": "Nikon Capture NX, " "Quality 69", "subsampling": "211111"}
    ],
    "b1b1a08ebaf13142b731c95771d97226": [
        {
            "description": "Apple QuickTime, " "Quality 308 (30%)",
            "subsampling": "221111",
        }
    ],
    "b1dc98f6a2f8828f8432872da43e7d94": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "21 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 21",
            "subsampling": "111111",
        },
    ],
    "b1f1b6519991ac7696b233dd9b9de6b5": [
        {"description": "Apple QuickTime, " "Quality 509 (50%)", "subsampling": "11"}
    ],
    "b2118dc8e8b1762cc634e135a2a1893c": [
        {
            "description": "Apple QuickTime, " "Quality 274 (27%)",
            "subsampling": "221111",
        }
    ],
    "b26a53dce1477ac3970335df110bb240": [
        {
            "description": "Apple QuickTime, " "Quality 219-220 (21%)",
            "subsampling": "221111",
        }
    ],
    "b2762ffa5c0a1799fb2e9ad6dfd2171a": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 58",
            "subsampling": "111111",
        }
    ],
    "b290e52c21a435fede4586636ef5e287": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "60 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 60",
            "subsampling": "111111",
        },
    ],
    "b2f7b5e3007387aa22df74e82e916195": [
        {"description": "Apple QuickTime, " "Quality 433 (42%)", "subsampling": "11"}
    ],
    "b2f95d6a0eec4de39e0964a3b7303e9f": [
        {"description": "Apple QuickTime, " "Quality 842 (82%)", "subsampling": "11"}
    ],
    "b309a0dc90b16ac01f0798a04c3127e8": [
        {
            "description": "Apple QuickTime, " "Quality 254 (25%)",
            "subsampling": "221111",
        }
    ],
    "b35f3358027aa4d2cca0c64425aa8f1b": [
        {
            "description": "Apple QuickTime, " "Quality 358 (35%)",
            "subsampling": "221111",
        }
    ],
    "b39cafdb459a42749be3f6459a596677": [
        {"description": "Adobe Photoshop, " "Quality 3", "subsampling": "11"}
    ],
    "b3d9bdc2090200537fb42f4d69631150": [
        {"description": "FixFoto, Quality 11", "subsampling": ""}
    ],
    "b3ebdf0376c9c48cca51ea8b550f6c51": [
        {"description": "Apple QuickTime, " "Quality 709 (69%)", "subsampling": "11"}
    ],
    "b3f215deea48e982e205619af279205f": [
        {"description": "Adobe Photoshop, " "Quality 4", "subsampling": "11"}
    ],
    "b40f3f3c46d70a560e2033fadd8c7bb5": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 29",
            "subsampling": "221111",
        }
    ],
    "b41b3d226ba21244b8070ba719ec721a": [
        {"description": "ACD Systems Digital " "Imaging, Quality 48", "subsampling": ""}
    ],
    "b41ccbe66e41a05de5e68832c07969a7": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "2 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 2",
            "subsampling": "111111",
        },
    ],
    "b43ab5c404469c416e853e52497b3f0d": [
        {
            "description": "Apple QuickTime, " "Quality 560 (55%)",
            "subsampling": "221111",
        }
    ],
    "b44cb1ca15fc9e3a27420df2ddae5879": [
        {"description": "Apple QuickTime, " "Quality 622 (61%)", "subsampling": "11"}
    ],
    "b4633256b0e0d5e2a5021f01ebabc105": [
        {
            "description": "Apple QuickTime, " "Quality 773 (75%)",
            "subsampling": "211111",
        }
    ],
    "b4ef810b14dee9c6d6d8cace98f799a6": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "68 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 68",
            "subsampling": "111111",
        },
    ],
    "b5424d9dce37dd5c9e0e38bcc775f48e": [
        {"description": "Apple QuickTime, " "Quality 676 (66%)", "subsampling": "11"}
    ],
    "b558f097ed59f547d2b370a73145caf9": [
        {"description": "Apple QuickTime, " "Quality 853 (83%)", "subsampling": "11"}
    ],
    "b55f27c368f119f25957c8e0036b27f8": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "65",
            "subsampling": "",
        }
    ],
    "b5648f13228d20fd7ae81965394f7515": [
        {
            "description": "Apple QuickTime, " "Quality 577 (56%)",
            "subsampling": "221111",
        }
    ],
    "b5c213a3785c4c62b25d8f8c30758593": [
        {"description": "Konica/Minolta DYNAX " "7D, Fine", "subsampling": "211111"}
    ],
    "b63e97c56859f2476ed3f15f40775fb5": [
        {
            "description": "Apple QuickTime, " "Quality 817 (80%)",
            "subsampling": "211111",
        }
    ],
    "b64cc19a0f81a506ed5bcfb9c131c8fe": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "88 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 88",
            "subsampling": "111111",
        },
    ],
    "b6640d3879f9922708d23e6adb3d61c9": [
        {"description": "Pentax Optio V10, Best", "subsampling": "211111"}
    ],
    "b6900aafebce0e59136abb701eacb1e5": [
        {"description": "Apple QuickTime, " "Quality 290 (28%)", "subsampling": "11"}
    ],
    "b69090d1ab951e6355ab193b1f20bf48": [
        {"description": "Apple QuickTime, " "Quality 282 (28%)", "subsampling": "11"}
    ],
    "b691578c1d6b16687fe2df12843d0642": [
        {
            "description": "Apple QuickTime, " "Quality 785-786 (77%)",
            "subsampling": "11",
        }
    ],
    "b697448eec21ef07f3111b62d592c423": [
        {
            "description": "Apple QuickTime, " "Quality 888-890 (87%)",
            "subsampling": "211111",
        }
    ],
    "b69dcb672088f296323d891219464ad8": [
        {"description": "Nikon Capture NX, " "Quality 89", "subsampling": "111111"}
    ],
    "b6a2598792fd87b7eb0c094cbd52862f": [
        {"description": "FinePixViewer, Fine", "subsampling": "211111"}
    ],
    "b6b80a78472dca05c9135702e96fdad9": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 83", "subsampling": ""}
    ],
    "b6bd9f956309a20e3a56294077536391": [
        {"description": "Pentax Optio A10/S7, " "Best", "subsampling": "211111"}
    ],
    "b6d1c6efb27ea721577888b5f981ad7b": [
        {"description": "Nikon Capture NX, " "Quality 90", "subsampling": "111111"}
    ],
    "b6ea2f838fa1942a21e41f6bba417782": [
        {
            "description": "Apple QuickTime, " "Quality 972-973 (95%)",
            "subsampling": "11",
        }
    ],
    "b6ff9215f87e4b053aaee36381f59005": [
        {"description": "Apple QuickTime, " "Quality 741 (72%)", "subsampling": "11"}
    ],
    "b7257ba67e4b38b7ccdca2a65d60c970": [
        {
            "description": "Apple QuickTime, " "Quality 504 (49%)",
            "subsampling": "221111",
        }
    ],
    "b7279ade733ff1c88073971cebe6edd8": [
        {
            "description": "Apple QuickTime, " "Quality 357 (35%)",
            "subsampling": "221111",
        }
    ],
    "b73481179da895f3b9ecea1737054a9c": [
        {"description": "Pentax K20D, Best (B)", "subsampling": "211111"}
    ],
    "b749b90354443bf17da7a67a5ad53397": [
        {"description": "Apple QuickTime, " "Quality 562 (55%)", "subsampling": "11"}
    ],
    "b783df92ec8a787b1eae4e05888b184b": [
        {
            "description": "Apple QuickTime, " "Quality 833-834 (81%)",
            "subsampling": "11",
        }
    ],
    "b79ff1a16807a48a31d457ad7e0b94f2": [
        {
            "description": "Apple QuickTime, " "Quality 980-984 (96%)",
            "subsampling": "211111",
        }
    ],
    "b80e56d3ed0c4a8e1c6bb0c5a1d45ca9": [
        {
            "description": "Apple QuickTime, " "Quality 226-227 (22%)",
            "subsampling": "221111",
        }
    ],
    "b83146f54d17b2c8e242f7f36dc36f19": [
        {
            "description": "Apple QuickTime, " "Quality 414 (40%)",
            "subsampling": "221111",
        }
    ],
    "b8548a302585d78a0c269b54bff86541": [
        {"description": "Canon PowerShot, Fine " "Small", "subsampling": "211111"}
    ],
    "b87750acf49940bf1f01f6a134a600b1": [
        {"description": "Apple QuickTime, " "Quality 382 (37%)", "subsampling": "11"}
    ],
    "b8d1fcda3a19d00788c2be73fd4c2c8e": [
        {
            "description": "Apple QuickTime, " "Quality 765-766 (75%)",
            "subsampling": "221111",
        }
    ],
    "b8ef26dabc2d81a8ba13b1f49ea711d3": [
        {"description": "Apple QuickTime, " "Quality 605 (59%)", "subsampling": "11"}
    ],
    "b8fca611f92cbc459fe21e11f0214328": [
        {
            "description": "Apple QuickTime, " "Quality 672-673 (66%)",
            "subsampling": "221111",
        }
    ],
    "b8fce00f93108e7db57a012c51fad341": [
        {"description": "Pentax K20D, Best (C)", "subsampling": "211111"}
    ],
    "b900f91ee8697255d5daebce858caaeb": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "45 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 45",
            "subsampling": "111111",
        },
    ],
    "b9594c8100236f288cdc01e6488cbc41": [
        {"description": "Apple QuickTime, " "Quality 353 (34%)", "subsampling": "11"}
    ],
    "b98b8adb8f1f78b65800efe6c329ceab": [
        {"description": "FixFoto, Quality 22", "subsampling": ""}
    ],
    "b99bdcd0145833d52b916e71f2c20a04": [
        {
            "description": "Apple QuickTime, " "Quality 746 (73%)",
            "subsampling": "221111",
        }
    ],
    "b9b1ce23552e2f82b95b48de20065ed3": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "99",
            "subsampling": "",
        }
    ],
    "b9be740b8a374a52808ad5ef6db2bfe7": [
        {
            "description": "Apple QuickTime, " "Quality 297 (29%)",
            "subsampling": "221111",
        }
    ],
    "b9d16f36087d4cca70eef1512c4be569": [
        {
            "description": "Apple QuickTime, " "Quality 691 (67%)",
            "subsampling": "221111",
        }
    ],
    "b9d66564ab9c4bb0910eb228aa9a48e1": [
        {
            "description": "Apple QuickTime, " "Quality 861-863 (84%)",
            "subsampling": "211111",
        }
    ],
    "b9eb63b89c80c71f4eac8c6e27d272f1": [
        {
            "description": "ACD Systems Digital " "Imaging, Quality 25 or " "26",
            "subsampling": "",
        }
    ],
    "b9f5c003ef62cbd8fc93be6679c1c3bc": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "97",
            "subsampling": "",
        }
    ],
    "b9fd15fd52408af5ea2a5045227233d8": [
        {
            "description": "Adobe Lightroom, " "Quality 54% - 61%",
            "subsampling": "111111",
        }
    ],
    "ba12dbfbd652c9cde69822996bdb2139": [
        {"description": "ACD Systems Digital " "Imaging, Quality 79", "subsampling": ""}
    ],
    "ba18a8f4175bdedfea7af9bf5fe8dd9c": [
        {
            "description": "Apple QuickTime, " "Quality 972-973 (95%)",
            "subsampling": "211111",
        }
    ],
    "ba1a32697c0ae4e76a78f4b5624a8ce0": [
        {"description": "Apple QuickTime, " "Quality 393 (38%)", "subsampling": "11"}
    ],
    "ba36e1298ce7fed908ee3e02b83ae7c3": [
        {
            "description": "Apple QuickTime, " "Quality 290 (28%)",
            "subsampling": "221111",
        }
    ],
    "ba3c103d00719e795b093ac7a75e6fac": [
        {"description": "Apple QuickTime, " "Quality 296 (29%)", "subsampling": "11"}
    ],
    "ba49b0656894f3c76d852223721b3b1f": [
        {
            "description": "Apple QuickTime, " "Quality 736 (72%)",
            "subsampling": "221111",
        }
    ],
    "ba4af3bb30dda0a7be4c04ff1ebbd9ef": [
        {
            "description": "Apple QuickTime, " "Quality 878-880 (86%)",
            "subsampling": "211111",
        }
    ],
    "ba60a642bfb1a184c11e5561581d7115": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 71",
            "subsampling": "111111",
        }
    ],
    "bad6fdd8761fb9d0921384013acf783f": [
        {
            "description": "Apple QuickTime, " "Quality 835 (82%)",
            "subsampling": "211111",
        }
    ],
    "bafe2a89809f23bc7367e9a819570728": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 45",
            "subsampling": "221111",
        }
    ],
    "bb0180b9eda074c3f913c8ada3d4c1ad": [
        {
            "description": "Apple QuickTime, " "Quality 751 (73%)",
            "subsampling": "221111",
        }
    ],
    "bb313d5398065376c7765092fc8ea0f0": [
        {"description": "Nikon Capture NX, " "Quality 33", "subsampling": "221111"}
    ],
    "bb342113b57cf66ce0cf3a09fae5fd16": [
        {
            "description": "Apple QuickTime, " "Quality 450 (44%)",
            "subsampling": "221111",
        }
    ],
    "bb4475a9e14464eb4682fd81cceb1f91": [
        {"description": "Pentax K10D (X)", "subsampling": "211111"}
    ],
    "bbad0e19b252268530df19c563aa9176": [
        {
            "description": "Apple QuickTime, " "Quality 520 (51%)",
            "subsampling": "221111",
        }
    ],
    "bbba80e58afae43278e287021d4f1499": [
        {"description": "Nikon Capture NX, " "Quality 62", "subsampling": "211111"}
    ],
    "bbbae155e558e9d37686ec34bd065a53": [
        {"description": "Apple QuickTime, " "Quality 480 (47%)", "subsampling": "11"}
    ],
    "bbd2dbcfe20b59e981e9a42cd1eb6ece": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "100 (Grayscale)",
            "subsampling": "11",
        }
    ],
    "bc066ff3fbea8a290c6f9882687945e0": [
        {"description": "Pentax Optio 430RS, " "Fine", "subsampling": "221111"}
    ],
    "bc156b933365b88e5ba9f1bd4b2fee4e": [
        {
            "description": "Apple QuickTime, " "Quality 147-150 " "(14-15%)",
            "subsampling": "11",
        }
    ],
    "bc2afe0a9c7c68b8d84bd231209be3e2": [
        {
            "description": "Apple QuickTime, " "Quality 859-860 (84%)",
            "subsampling": "211111",
        }
    ],
    "bc4541f5bc4d58b99b53d24f3f520b32": [
        {
            "description": "Apple QuickTime, " "Quality 623 (61%)",
            "subsampling": "221111",
        }
    ],
    "bc490651af6592cd1dbbbc4fa2cfa1fb": [
        {
            "description": "Adobe Lightroom, " "Quality 8% - 15%",
            "subsampling": "221111",
        },
        {"description": "Adobe Photoshop, " "Quality 1", "subsampling": "221111"},
    ],
    "bc4abc4600f2efc0bdead1e4be78801b": [
        {
            "description": "Apple QuickTime, " "Quality 291-292 " "(28-29%)",
            "subsampling": "221111",
        }
    ],
    "bc6d3a9f349a97c5cde3f8fa4e1b5beb": [
        {
            "description": "Apple QuickTime, " "Quality 313 (31%)",
            "subsampling": "221111",
        }
    ],
    "bc93228921ec863e90850325cfd90dd2": [
        {
            "description": "Apple QuickTime, " "Quality 165-167 (16%)",
            "subsampling": "11",
        }
    ],
    "bcc29022955cc7532b08640ab118259c": [
        {"description": "Apple QuickTime, " "Quality 696 (68%)", "subsampling": "11"}
    ],
    "bcd4d36a9db91a51d1a571f71f8230d4": [
        {"description": "ACD Systems Digital " "Imaging, Quality 27", "subsampling": ""}
    ],
    "bce6fa61623ad4f65ff3fec1528cb026": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "82 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 82",
            "subsampling": "111111",
        },
    ],
    "bceaee6c1a150006b3643de6942ccfa3": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 22", "subsampling": ""}
    ],
    "bd1f81bd50cf9859eb0ae6d2dbf75d09": [
        {"description": "Apple QuickTime, " "Quality 927 (91%)", "subsampling": "11"}
    ],
    "bd6943a8c92a14e74d2b24052a19400a": [
        {
            "description": "Apple QuickTime, " "Quality 610 (60%)",
            "subsampling": "221111",
        }
    ],
    "bdaf13038b56b5701f60300528f8a89c": [
        {
            "description": "Apple QuickTime, " "Quality 640-641 (63%)",
            "subsampling": "221111",
        }
    ],
    "bdaf3e68c2925cbaad3864359fdbbb77": [
        {
            "description": "Apple QuickTime, " "Quality 474 (46%)",
            "subsampling": "221111",
        }
    ],
    "bdcc7abca09941326c079bb3bc30de4d": [
        {
            "description": "Apple QuickTime, " "Quality 93-101 (9-10%)",
            "subsampling": "11",
        }
    ],
    "bdd6043e7f5a5f1512b99b2394a075e2": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 52",
            "subsampling": "111111",
        }
    ],
    "bdebcafc7b5f6b7fea114943e042df5e": [
        {
            "description": "Apple QuickTime, " "Quality 345 (34%)",
            "subsampling": "221111",
        }
    ],
    "be010732a7783ee345548a1eb95d024a": [
        {
            "description": "Apple QuickTime, " "Quality 631 (62%)",
            "subsampling": "221111",
        }
    ],
    "be232444027e83db6f8d8b79d078442e": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "57 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 57",
            "subsampling": "111111",
        },
    ],
    "be63c4e967eff819bd8a052a561a4576": [
        {
            "description": "Apple QuickTime, " "Quality 562 (55%)",
            "subsampling": "221111",
        }
    ],
    "be7c72e09c46622b0d2b93e170a03e17": [
        {
            "description": "Apple QuickTime, " "Quality 707 (69%)",
            "subsampling": "221111",
        }
    ],
    "be7e7114f08e1775ca9676d2feeeccca": [
        {"description": "Apple QuickTime, " "Quality 431 (42%)", "subsampling": "11"}
    ],
    "bebd334aca511e2a2b6c60f43f9e6cf1": [
        {"description": "Panasonic DMC-FZ30, " "High (H)", "subsampling": "211111"}
    ],
    "beee113eea5950b8211cdc49e5a04099": [
        {
            "description": "Apple QuickTime, " "Quality 845 (83%)",
            "subsampling": "211111",
        }
    ],
    "bf010771f909049fc5fceedcaa0f917c": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 75", "subsampling": ""}
    ],
    "bf0c20b20af6473b7c4a338ba57d1a96": [
        {
            "description": "Apple QuickTime, " "Quality 895 (87%)",
            "subsampling": "211111",
        }
    ],
    "bf2904a3e3870a2b4d060e0863530d92": [
        {"description": "Apple QuickTime, " "Quality 409 (40%)", "subsampling": "11"}
    ],
    "bf29abfdf0086437452e2ca220e69cae": [
        {"description": "Apple QuickTime, " "Quality 273 (27%)", "subsampling": "11"}
    ],
    "bf68d1866b75cea8f99cf2fc46f9d686": [
        {"description": "FixFoto, Quality 21", "subsampling": ""}
    ],
    "bf72e4d4aacbdaeb86fd3f67c8df2667": [
        {"description": "Canon ZoomBrowser, " "Medium", "subsampling": "211111"},
        {
            "description": "PENTAX PHOTO " "Laboratory, High " "compression",
            "subsampling": "211111",
        },
        {
            "description": "HTC Touch Diamond " "P3700, Quality Unknown",
            "subsampling": "221111",
        },
        {"description": "Pentax K10D (Y)", "subsampling": "211111"},
    ],
    "bfe8c1c73eea84b85673487a82f67627": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "71 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 71",
            "subsampling": "111111",
        },
    ],
    "c00374dece11c3cab5f2c3bf9621d365": [
        {
            "description": "Apple QuickTime, " "Quality 117-122 " "(11-12%)",
            "subsampling": "11",
        }
    ],
    "c0204862b8aafa2c286c7b58d755c31f": [
        {"description": "Nikon Capture NX, " "Quality 78", "subsampling": "211111"}
    ],
    "c029b8a48e3c93f7c0367f2a149491c7": [
        {
            "description": "Apple QuickTime, " "Quality 687 (67%)",
            "subsampling": "221111",
        }
    ],
    "c063344185079018af9fcf161a3fdf98": [
        {"description": "FixFoto, Quality 23", "subsampling": ""}
    ],
    "c07a6430e56ef16a0526673398e87ac6": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 7", "subsampling": ""}
    ],
    "c0a54e87a2ef1c163311bcc1abf85214": [
        {"description": "Apple QuickTime, " "Quality 450 (44%)", "subsampling": "11"}
    ],
    "c0cecb47363aff00a2764a915f95cd35": [
        {
            "description": "Apple QuickTime, " "Quality 580 (57%)",
            "subsampling": "221111",
        }
    ],
    "c0cf6b0c508a35a13acd8c912548a269": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "91",
            "subsampling": "",
        }
    ],
    "c0f2265630bdf5f29e8c95df25c89edb": [
        {"description": "Apple QuickTime, " "Quality 601 (59%)", "subsampling": "11"}
    ],
    "c10fca5e6f66238ab09f7e8105f54e39": [
        {
            "description": "Apple QuickTime, " "Quality 730 (71%)",
            "subsampling": "221111",
        }
    ],
    "c1278992838bdd62e71bf41c20126a5f": [
        {"description": "Apple QuickTime, " "Quality 730 (71%)", "subsampling": "11"}
    ],
    "c1557f789acc622c8858be4dfbc53c31": [
        {
            "description": "Apple QuickTime, " "Quality 696 (68%)",
            "subsampling": "221111",
        }
    ],
    "c181c79bc41cf5fe11e6f253242ce2c4": [
        {
            "description": "Apple QuickTime, " "Quality 949-951 (93%)",
            "subsampling": "211111",
        }
    ],
    "c18239304e22bd19e3c8a21f9875ba39": [
        {
            "description": "Apple QuickTime, " "Quality 775-776 (76%)",
            "subsampling": "11",
        }
    ],
    "c192d5847d1146a31db621263a9ce2f5": [
        {
            "description": "Apple QuickTime, " "Quality 679 (66%)",
            "subsampling": "221111",
        }
    ],
    "c1978a445de1173b5039b0cf8d8a91fe": [
        {
            "description": "ACD Systems Digital " "Imaging, Quality 65 or " "66",
            "subsampling": "",
        }
    ],
    "c1af7f1a3716bef087124306b068605c": [
        {"description": "Apple QuickTime, " "Quality 423 (41%)", "subsampling": "11"}
    ],
    "c1bcc3db9f417dc52595f2bb224e30d7": [
        {"description": "Apple QuickTime, " "Quality 307 (30%)", "subsampling": "11"}
    ],
    "c1e0554d8a6ed003eb98e068429b56b9": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 12",
            "subsampling": "221111",
        }
    ],
    "c20f4841a1ff7e393af8f6ea4124403c": [
        {"description": "ACD Systems Digital " "Imaging, Quality 54", "subsampling": ""}
    ],
    "c23b08c94d7537c9447691d54ae1080c": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "16 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 16",
            "subsampling": "111111",
        },
    ],
    "c244f94d84a016840c6ef06250c58ade": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 73",
            "subsampling": "111111",
        }
    ],
    "c24c44a4dadd77c15e0b4c741a2d4bd5": [
        {"description": "Nikon Capture NX, " "Quality 98", "subsampling": "111111"}
    ],
    "c25ed5069735a3f9677ee494108a52bc": [
        {"description": "Apple QuickTime, " "Quality 715 (70%)", "subsampling": "11"}
    ],
    "c28ab3fd6480c92028327957228c0a11": [
        {"description": "Apple QuickTime, " "Quality 512 (50%)", "subsampling": "11"}
    ],
    "c2a8a67d050b22a0673ee9ad6685a540": [
        {"description": "Apple QuickTime, " "Quality 336 (33%)", "subsampling": "11"}
    ],
    "c2afe9aca67de0276a6fb507861c3e80": [
        {
            "description": "Apple QuickTime, " "Quality 427 (42%)",
            "subsampling": "221111",
        }
    ],
    "c2b037bf9f5e5baba804d7bbbb2dc73b": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "83 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 83",
            "subsampling": "111111",
        },
    ],
    "c2b23a91d377ce2d99ac4109f2740069": [
        {
            "description": "Apple QuickTime, " "Quality 579 (57%)",
            "subsampling": "221111",
        }
    ],
    "c2d5e2e93ec191015d8181c9e25387d8": [
        {"description": "Apple QuickTime, " "Quality 553 (54%)", "subsampling": "11"}
    ],
    "c2df556e8ede9fb199b9a16e01279c6b": [
        {
            "description": "Apple QuickTime, " "Quality 994-996 (97%)",
            "subsampling": "211111",
        }
    ],
    "c31cb63954b137b62c5fe35379235e2e": [
        {
            "description": "Apple QuickTime, " "Quality 952-954 (93%)",
            "subsampling": "11",
        }
    ],
    "c31f71de437dc301d34f847d95267d9e": [
        {
            "description": "Apple QuickTime, " "Quality 755 (74%)",
            "subsampling": "221111",
        }
    ],
    "c33573208ef877f1bc9a64f595e00c4d": [
        {
            "description": "Apple QuickTime, " "Quality 975-977 (95%)",
            "subsampling": "11",
        }
    ],
    "c33a667bff7f590655d196010c5e39f3": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "20 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 20",
            "subsampling": "111111",
        },
    ],
    "c3b80241282d06ac5114f2750089589a": [
        {
            "description": "Apple QuickTime, " "Quality 123-127 (12%)",
            "subsampling": "221111",
        }
    ],
    "c3bb3c557e70b56a890b07236348518b": [
        {
            "description": "Apple QuickTime, " "Quality 162-164 (16%)",
            "subsampling": "221111",
        }
    ],
    "c3d1601f84ec3adfbc8ca17883ef6378": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 98", "subsampling": ""}
    ],
    "c3f615274e58eb887a2aa75acad436ff": [
        {"description": "Apple QuickTime, " "Quality 865 (84%)", "subsampling": "11"}
    ],
    "c3fbc85c803ddc81c8882c03330b5b15": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 89",
            "subsampling": "111111",
        }
    ],
    "c40848be9d1d1018747630cdac2d7294": [
        {
            "description": "Apple QuickTime, " "Quality 968-970 (95%)",
            "subsampling": "11",
        }
    ],
    "c40a38c96832a6042c6ddfc9754c1d6d": [
        {
            "description": "Apple QuickTime, " "Quality 487 (48%)",
            "subsampling": "221111",
        }
    ],
    "c44701e8185306f5e6d09be16a2b0fbd": [
        {
            "description": "Apple QuickTime, " "Quality 325 (32%)",
            "subsampling": "221111",
        },
        {"description": "Nikon Capture NX, " "Quality 23", "subsampling": "221111"},
        {
            "description": "Sony Image Data Suite, " "Quality 4 (high " "compression)",
            "subsampling": "211111",
        },
    ],
    "c448e6817efa9acdad225e60ed0013f9": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 23", "subsampling": ""}
    ],
    "c46c764191f9c3db2bfe8d134512bcd8": [
        {
            "description": "ACD Systems Digital " "Imaging, Quality 15 or " "16",
            "subsampling": "",
        }
    ],
    "c4fb82f47a7b002d5cab421592ae4972": [
        {
            "description": "Apple QuickTime, " "Quality 721 (70%)",
            "subsampling": "221111",
        }
    ],
    "c53438ece0552cedb1ec0d50ad2d5dbe": [
        {
            "description": "Apple QuickTime, " "Quality 462 (45%)",
            "subsampling": "221111",
        }
    ],
    "c558f3407dc549c902efad68c54920de": [
        {"description": "Apple QuickTime, " "Quality 440 (43%)", "subsampling": "11"}
    ],
    "c5774ffb4573926fd03d4175818c0e5d": [
        {
            "description": "Apple QuickTime, " "Quality 714 (70%)",
            "subsampling": "221111",
        }
    ],
    "c58a47c2e3dc737b9591420812b9cc27": [
        {
            "description": "Apple QuickTime, " "Quality 397 (39%)",
            "subsampling": "221111",
        }
    ],
    "c59a4cf0beedbfd1b102dc3d3c8e73ac": [
        {"description": "Pentax K10D (AH)", "subsampling": "211111"}
    ],
    "c5bb48d86e26ac496bb4b4bc888cc06a": [
        {"description": "Apple QuickTime, " "Quality 576 (56%)", "subsampling": "11"}
    ],
    "c5c102ba5f004d49656f424d89e9773c": [
        {
            "description": "Apple QuickTime, " "Quality 481 (47%)",
            "subsampling": "221111",
        }
    ],
    "c5c472d899462bbe31da9aa8c072c0bc": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 32",
            "subsampling": "221111",
        }
    ],
    "c5fcb1748f616ac97794d34b1b93616e": [
        {
            "description": "Apple QuickTime, " "Quality 752-753 " "(73-74%)",
            "subsampling": "221111",
        }
    ],
    "c60dbbefd4f215b9359dd004f4fb0fd3": [
        {
            "description": "Apple QuickTime, " "Quality 678 (66%)",
            "subsampling": "221111",
        }
    ],
    "c60f75f7e09f0454db9cc48392a7eeed": [
        {"description": "Apple QuickTime, " "Quality 360 (35%)", "subsampling": "11"}
    ],
    "c638d9151dc650993b56f4effc0fe19c": [
        {"description": "Apple QuickTime, " "Quality 700 (68%)", "subsampling": "11"}
    ],
    "c65677d79e37baf57767e10d7b7f1ce8": [
        {"description": "Apple QuickTime, " "Quality 668 (65%)", "subsampling": "11"}
    ],
    "c67d246229fcc0dd1b974f7df556d247": [
        {"description": "Apple QuickTime, " "Quality 701 (68%)", "subsampling": "11"}
    ],
    "c6d134475eb85bd454f2ee5153366c51": [
        {
            "description": "Apple QuickTime, " "Quality 788 (77%)",
            "subsampling": "211111",
        }
    ],
    "c6d9120293c8435cf6b40574b45756bb": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 95",
            "subsampling": "111111",
        }
    ],
    "c70a1df73760a88deb890003cdab3bfe": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "27",
            "subsampling": "",
        }
    ],
    "c71131cb485b59faf920d11982f7d454": [
        {"description": "Apple QuickTime, " "Quality 774 (76%)", "subsampling": "11"}
    ],
    "c71aa81fb12b378dd31a1ca128942f76": [
        {
            "description": "Apple QuickTime, " "Quality 594 (58%)",
            "subsampling": "221111",
        }
    ],
    "c722656df4bb0651821cd90880953a20": [
        {"description": "Apple QuickTime, " "Quality 563 (55%)", "subsampling": "11"}
    ],
    "c7294290fe26155147072f9041705cfb": [
        {"description": "Nikon Capture NX, " "Quality 97", "subsampling": "111111"}
    ],
    "c740804ef8493bb467744e1cdb8882c1": [
        {
            "description": "Apple QuickTime, " "Quality 390 (38%)",
            "subsampling": "221111",
        }
    ],
    "c741c1b134cf81ab69acc81f15a67137": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "24 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 24",
            "subsampling": "111111",
        },
    ],
    "c7498fc4b3802b290a452631dd1e1b63": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 60", "subsampling": ""}
    ],
    "c7614d3d384a02630721be335062ef75": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 53",
            "subsampling": "111111",
        }
    ],
    "c78717ac2705274888912f349eeb2c8e": [
        {"description": "Apple QuickTime, " "Quality 692 (68%)", "subsampling": "11"}
    ],
    "c79231716eff96853fe03a26c1c38120": [
        {"description": "Apple QuickTime, " "Quality 294 (29%)", "subsampling": "11"}
    ],
    "c7d0f7dee5631d01bc55b7c598805d98": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "16",
            "subsampling": "",
        }
    ],
    "c7da2e951711b8b1314a7c531e09cbdc": [
        {"description": "Apple QuickTime, " "Quality 274 (27%)", "subsampling": "11"}
    ],
    "c7e68d88bee5c2ee4b61a11bc2e68c80": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 70", "subsampling": ""}
    ],
    "c804929d3963c7427fa143e0d1e8c94e": [
        {
            "description": "Apple QuickTime, " "Quality 780-781 (76%)",
            "subsampling": "11",
        }
    ],
    "c81b03b0291d2277461a551ed6861252": [
        {
            "description": "Apple QuickTime, " "Quality 648-649 (63%)",
            "subsampling": "221111",
        }
    ],
    "c84313bc621c6d05999510fa57c56d05": [
        {"description": "Apple QuickTime, " "Quality 542 (53%)", "subsampling": "11"}
    ],
    "c871ce0851d4647f226b2dcfd49fe9a9": [
        {"description": "Panasonic DMC-L1, Very " "High", "subsampling": "211111"}
    ],
    "c8bfcc60aeec937300405f59373be4ef": [
        {"description": "Pentax K2000, Best (C)", "subsampling": "211111"}
    ],
    "c8ef3c50ca99c44ea13f1692ac1190dc": [
        {
            "description": "Apple QuickTime, " "Quality 511 (50%)",
            "subsampling": "221111",
        }
    ],
    "c8f02bf550c40daa39b28911a4ef5a69": [
        {
            "description": "Apple QuickTime, " "Quality 578 (56%)",
            "subsampling": "221111",
        }
    ],
    "c8f917220d6285cda6428a2cf6a9a1b3": [
        {
            "description": "Apple QuickTime, " "Quality 688-689 (67%)",
            "subsampling": "11",
        }
    ],
    "c901580e589f58d309f8b50590cfe214": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 72",
            "subsampling": "111111",
        }
    ],
    "c910bcb7b9e8967b87cfa08229d9ca34": [
        {
            "description": "Apple QuickTime, " "Quality 508 (50%)",
            "subsampling": "221111",
        }
    ],
    "c92c755320e7ce8f46f644b90b7907e8": [
        {
            "description": "Apple QuickTime, " "Quality 999-1000 (98%)",
            "subsampling": "211111",
        }
    ],
    "c9309ab058680151be5f97e6c54dc687": [
        {"description": "Nikon Capture NX, " "Quality 100", "subsampling": "111111"},
        {
            "description": "ACD Systems Digital " "Imaging, Quality 98",
            "subsampling": "",
        },
    ],
    "c94e09eec2df4a41b2806c23d9939cb6": [
        {"description": "Apple QuickTime, " "Quality 826 (81%)", "subsampling": "11"}
    ],
    "c97965ce5392623f668a386b30e41cee": [
        {"description": "Nikon Capture NX, " "Quality 26", "subsampling": "221111"}
    ],
    "c9a4b04bc8e580608014b6f3111322d7": [
        {"description": "Apple QuickTime, " "Quality 448 (44%)", "subsampling": "11"}
    ],
    "c9ce3dc3d0567f631e463cc3ff1b2e30": [
        {
            "description": "Apple QuickTime, " "Quality 252-253 (25%)",
            "subsampling": "221111",
        }
    ],
    "c9f10fb6d352cc8a8967e7e96a64862c": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "42",
            "subsampling": "",
        }
    ],
    "c9f953acdfc1f5afdbb9e9f74692d23e": [
        {
            "description": "Apple QuickTime, " "Quality 741 (72%)",
            "subsampling": "221111",
        }
    ],
    "ca0bf66c467278f9d5ca5301840e7a7f": [
        {
            "description": "Apple QuickTime, " "Quality 963-967 (94%)",
            "subsampling": "211111",
        }
    ],
    "ca0e84028714f19cf20cb868d1cd346c": [
        {
            "description": "Apple QuickTime, " "Quality 541 (53%)",
            "subsampling": "221111",
        }
    ],
    "ca21386b17f3866a235fca4b6e72b124": [
        {"description": "Apple QuickTime, " "Quality 940 (92%)", "subsampling": "11"}
    ],
    "ca39dde8e9b4ccd6261b28e089181639": [
        {
            "description": "Apple QuickTime, " "Quality 806-807 (79%)",
            "subsampling": "211111",
        }
    ],
    "ca683ab6caaa3132bf661a0ebf32ef4e": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 81",
            "subsampling": "111111",
        }
    ],
    "caabe462a50217592c74902def037c07": [
        {
            "description": "Apple QuickTime, " "Quality 341 (33%)",
            "subsampling": "221111",
        }
    ],
    "cae0c8eb9a11a1f6eb7eca9651d8dbc0": [
        {"description": "ACD Systems Digital " "Imaging, Quality 44", "subsampling": ""}
    ],
    "cae6fd91a423ff181d50bb9c26a0d392": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 75",
            "subsampling": "111111",
        }
    ],
    "caf33ddc94762bf60a8c5e5024550b21": [
        {"description": "Apple QuickTime, " "Quality 64-80 (6-8%)", "subsampling": "11"}
    ],
    "cb207af75faf8ee1ef0ca3caa593bb69": [
        {
            "description": "Apple QuickTime, " "Quality 429 (42%)",
            "subsampling": "221111",
        }
    ],
    "cb34e1a0e18a4dd7ffe823f9c92b3622": [
        {
            "description": "Apple QuickTime, " "Quality 620 (61%)",
            "subsampling": "221111",
        }
    ],
    "cb5fc7927d88ac99f556b2dd7985eaf9": [
        {"description": "Apple QuickTime, " "Quality 505 (49%)", "subsampling": "11"}
    ],
    "cb6bc96131c4a5f762b5e5f79e7c4b66": [
        {"description": "Apple QuickTime, " "Quality 771 (75%)", "subsampling": "11"}
    ],
    "cb99b9bd30ae36929755fee9208ab36b": [
        {
            "description": "ACD Systems Digital " "Imaging, Quality 85 or " "86",
            "subsampling": "",
        }
    ],
    "cbde745c78fd546d6e83dd7512ebe863": [
        {"description": "Nikon Capture NX, " "Quality 2", "subsampling": "221111"}
    ],
    "cbdec670ec6d9105277434b304226920": [
        {
            "description": "Apple QuickTime, " "Quality 585 (57%)",
            "subsampling": "221111",
        }
    ],
    "cbfbfef12aead8841585ef605c789b9f": [
        {
            "description": "Adobe Lightroom, " "Quality 24% - 30%",
            "subsampling": "221111",
        },
        {"description": "Adobe Photoshop, " "Quality 3", "subsampling": "221111"},
    ],
    "cc3936c39c298ef67d9196d0254b0c19": [
        {
            "description": "Apple QuickTime, " "Quality 515 (50%)",
            "subsampling": "221111",
        }
    ],
    "cc3e4dc4e190d00a12bd03199efdcc6d": [
        {
            "description": "Apple QuickTime, " "Quality 437 (43%)",
            "subsampling": "221111",
        }
    ],
    "cc6bb734b742b0631ab6562a329e1603": [
        {"description": "Apple QuickTime, " "Quality 458 (45%)", "subsampling": "11"}
    ],
    "cc96e1c8906353c4023bc7e6b72bb684": [
        {"description": "Apple QuickTime, " "Quality 930 (91%)", "subsampling": "11"}
    ],
    "ccb55ec1549a51212859495e104c626b": [
        {"description": "Apple QuickTime, " "Quality 598 (58%)", "subsampling": "11"}
    ],
    "cccd5f36920fbe8ad77da2214f8ab6ed": [
        {
            "description": "Apple QuickTime, " "Quality 138-142 " "(13-14%)",
            "subsampling": "11",
        }
    ],
    "ccd6708ca1dbd66a23d40cee635a0f76": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 25", "subsampling": ""}
    ],
    "ccdf1a403ec068ad21ee78686a86dd10": [
        {"description": "Apple QuickTime, " "Quality 809 (79%)", "subsampling": "11"}
    ],
    "ccf3f63196092667f97c2ff723481a21": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "53",
            "subsampling": "",
        }
    ],
    "cd091eeb9d27d9dc7cdb5bff73572679": [
        {
            "description": "Apple QuickTime, " "Quality 762 (74%)",
            "subsampling": "221111",
        }
    ],
    "cd15038a76bd8752c3afd14669816c2e": [
        {
            "description": "Apple QuickTime, " "Quality 255 (25%)",
            "subsampling": "221111",
        }
    ],
    "cd2c6c01d8eb8d985086b54e2269278a": [
        {"description": "Nikon Capture NX, " "Quality 66", "subsampling": "211111"}
    ],
    "cd3ed5b396580d8e9f0cb7b78baed8b8": [
        {
            "description": "Apple QuickTime, " "Quality 451 (44%)",
            "subsampling": "221111",
        }
    ],
    "cd993be55bad60bb539df0cc2d7f9f6f": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "94",
            "subsampling": "",
        }
    ],
    "cdd7bd689f14d5f7c3ea790f6f09ae64": [
        {"description": "Apple QuickTime, " "Quality 572 (56%)", "subsampling": "11"}
    ],
    "cdf8e921300f27a4af7661a2de16e91a": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "32 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 32",
            "subsampling": "111111",
        },
    ],
    "ce05e4b45c53a6e321d9cf1061c62128": [
        {
            "description": "Apple QuickTime, " "Quality 117-122 " "(11-12%)",
            "subsampling": "221111",
        }
    ],
    "ce0e14187fec73f57242becd633a89a3": [
        {"description": "Apple QuickTime, " "Quality 556 (54%)", "subsampling": "11"}
    ],
    "ce0f36a3d870b24f9816634000ea2d2e": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "69",
            "subsampling": "",
        }
    ],
    "ce2335cc1f8289deda620877f50fd90d": [
        {
            "description": "Apple QuickTime, " "Quality 519 (51%)",
            "subsampling": "221111",
        }
    ],
    "ce378a14d52ee5752ded23b5a444f75e": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "25",
            "subsampling": "",
        }
    ],
    "ce4286d9f07999524c3c7472b065c5ab": [
        {
            "description": "Adobe Lightroom, " "Quality 16% - 23%",
            "subsampling": "221111",
        },
        {"description": "Adobe Photoshop, " "Quality 2", "subsampling": "221111"},
    ],
    "ce48f7fb2ba9edee46c3f4839b40ef60": [
        {"description": "Apple QuickTime, " "Quality 374 (37%)", "subsampling": "11"}
    ],
    "ce6bcb98c5f9358594f5934e64b4ecc3": [
        {"description": "Nikon Capture NX, " "Quality 38", "subsampling": "221111"}
    ],
    "ce9ad8466ffd84b91039326e8688c44a": [
        {
            "description": "Apple QuickTime, " "Quality 732-733 " "(71-72%)",
            "subsampling": "221111",
        }
    ],
    "cea44b5645cd1dbf469c8ae5600e4ff5": [
        {"description": "Apple QuickTime, " "Quality 413 (40%)", "subsampling": "11"}
    ],
    "ced483058f2abf19df0f7935dafd217a": [
        {"description": "Apple QuickTime, " "Quality 612 (60%)", "subsampling": "11"}
    ],
    "cedc5208c6e1cbffd8be0e47bfd76698": [
        {"description": "ACD Systems Digital " "Imaging, Quality 18", "subsampling": ""}
    ],
    "ceecacb651d0e01e9b1c78cde2d7835a": [
        {"description": "Apple QuickTime, " "Quality 854 (83%)", "subsampling": "11"}
    ],
    "cef5a49e1834c316a4a9e7dca8d69157": [
        {"description": "Apple QuickTime, " "Quality 939 (92%)", "subsampling": "11"}
    ],
    "ceff136f6dd88242500bfd639cb0c003": [
        {"description": "Nikon Capture NX, " "Quality 45", "subsampling": "221111"}
    ],
    "cf0a070dc9b4a8983b50f8e3f105b857": [
        {
            "description": "Apple QuickTime, " "Quality 442 (43%)",
            "subsampling": "221111",
        }
    ],
    "cf3929fd4c1e5c28b7f137f982178ad1": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "40 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 40",
            "subsampling": "111111",
        },
    ],
    "cf8573af40ced1793dcbc2346f969240": [
        {"description": "FixFoto, Quality 14", "subsampling": ""}
    ],
    "cf8fce0d4bde00a2feb680bb52667c8f": [
        {
            "description": "Apple QuickTime, " "Quality 208-209 (20%)",
            "subsampling": "11",
        }
    ],
    "cfbe44397240092d3a67241a23342528": [
        {"description": "Nikon Capture NX, " "Quality 5", "subsampling": "221111"}
    ],
    "cfc78404529f2b81b16d3f25fc96e8f4": [
        {
            "description": "Apple QuickTime, " "Quality 870 (85%)",
            "subsampling": "211111",
        }
    ],
    "cfe3144d4f8048a0507269a9d8a85993": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 43", "subsampling": ""}
    ],
    "cfe4549eb2dd81684920aa32b598260c": [
        {
            "description": "Apple QuickTime, " "Quality 739-740 (72%)",
            "subsampling": "11",
        }
    ],
    "d00103d50108e8be370a78d47f51aba0": [
        {
            "description": "Apple QuickTime, " "Quality 815 (80%)",
            "subsampling": "211111",
        }
    ],
    "d018c811df2390446b43cc702888864c": [
        {
            "description": "Apple QuickTime, " "Quality 171-173 (17%)",
            "subsampling": "11",
        }
    ],
    "d01a38e0f568d2a7b6b71f8fa63b8bcc": [
        {
            "description": "Apple QuickTime, " "Quality 645 (63%)",
            "subsampling": "221111",
        }
    ],
    "d03a4790dd96a862113b1a2408103ad6": [
        {
            "description": "Apple QuickTime, " "Quality 235 (23%)",
            "subsampling": "221111",
        }
    ],
    "d052e48078f986c715e68f502d371ccc": [
        {
            "description": "Apple QuickTime, " "Quality 190-191 (19%)",
            "subsampling": "11",
        }
    ],
    "d053fd2c67ce96b0ecf9ffc4b7f7775d": [
        {
            "description": "Apple QuickTime, " "Quality 663 (65%)",
            "subsampling": "221111",
        }
    ],
    "d08c8435de33f2c186aa2dd9cba3e874": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 61",
            "subsampling": "111111",
        }
    ],
    "d09f78b68290ff6b470720ead4d79b15": [
        {"description": "Apple QuickTime, " "Quality 279 (27%)", "subsampling": "11"}
    ],
    "d0a67359275cf9e2e8f35de79d2e28ae": [
        {
            "description": "Apple QuickTime, " "Quality 155-157 (15%)",
            "subsampling": "11",
        }
    ],
    "d0a8f50ff547da69a57eeb892e194cff": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 95", "subsampling": ""}
    ],
    "d0cbe6c7372724a802d0183c6de66f8b": [
        {"description": "Apple QuickTime, " "Quality 367 (36%)", "subsampling": "11"}
    ],
    "d0d6f781130c0fecd985df78c15c5c16": [
        {
            "description": "Apple QuickTime, " "Quality 859-860 (84%)",
            "subsampling": "11",
        }
    ],
    "d0eaa368737f17f6037757d393a22599": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "75 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "Apple QuickTime, " "Quality 466-467 (46%)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 75",
            "subsampling": "111111",
        },
    ],
    "d14411ab659ac68209ee8c75b941cb48": [
        {
            "description": "Apple QuickTime, " "Quality 228-229 (22%)",
            "subsampling": "221111",
        }
    ],
    "d1a8052e7152e0c35d167e9e56418eb7": [
        {
            "description": "Apple QuickTime, " "Quality 974 (95%)",
            "subsampling": "211111",
        }
    ],
    "d1c8c1e1fc2bfb776d2ee1aace3fc6f9": [
        {"description": "Apple QuickTime, " "Quality 742 (72%)", "subsampling": "11"}
    ],
    "d1ca3a3723c1385d2989b199a7a30557": [
        {
            "description": "Apple QuickTime, " "Quality 244 (24%)",
            "subsampling": "221111",
        }
    ],
    "d1dc48d911055bc533779d6e086f7242": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 20", "subsampling": ""}
    ],
    "d1ef25928fd4eefe131ffcfc249b9f8a": [
        {
            "description": "Apple QuickTime, " "Quality 656 (64%)",
            "subsampling": "221111",
        }
    ],
    "d237b1202f88ba8183bc1cb69dd4be66": [
        {"description": "ACD Systems Digital " "Imaging, Quality 59", "subsampling": ""}
    ],
    "d241d5165e64e98024b47dfbf76be88c": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 19",
            "subsampling": "221111",
        }
    ],
    "d255f70a910a2d0039f4e792d2c01210": [
        {
            "description": "Canon PowerShot, " "Superfine Medium2",
            "subsampling": "211111",
        }
    ],
    "d26a06f6114d83714e3b64b6dbe97e6f": [
        {
            "description": "Apple QuickTime, " "Quality 963-967 (94%)",
            "subsampling": "11",
        }
    ],
    "d275e9aebd39cf411496caf6e54d0c5f": [
        {
            "description": "Apple QuickTime, " "Quality 256-257 (25%)",
            "subsampling": "221111",
        }
    ],
    "d2a1887cf45aecd63d838e585dbb5794": [
        {
            "description": "Apple QuickTime, " "Quality 233-234 (23%)",
            "subsampling": "11",
        }
    ],
    "d2baa8fbc56f0970f820c376c6065d41": [
        {
            "description": "Apple QuickTime, " "Quality 659 (64%)",
            "subsampling": "221111",
        }
    ],
    "d2e14d8ba7d38f7544b569eea7221255": [
        {"description": "Nikon Capture NX, " "Quality 37", "subsampling": "221111"}
    ],
    "d2e34c70872ac119dda6bdeeb36bf229": [
        {"description": "Nikon Capture NX, " "Quality 87", "subsampling": "111111"}
    ],
    "d2e983c44eae2983f48f526992fbbfb4": [
        {"description": "Apple QuickTime, " "Quality 575 (56%)", "subsampling": "11"}
    ],
    "d300f18258f46060d89c994dbc370131": [
        {
            "description": "Apple QuickTime, " "Quality 483 (47%)",
            "subsampling": "221111",
        }
    ],
    "d312a23c8ecb3bf59bc11bbe17d79e55": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 69",
            "subsampling": "111111",
        }
    ],
    "d33d12dc779097bee959fefac6de9a3e": [
        {
            "description": "Apple QuickTime, " "Quality 199-201 " "(19-20%)",
            "subsampling": "11",
        }
    ],
    "d35254d58224b1b6babda94d7f1a5ffe": [
        {
            "description": "Apple QuickTime, " "Quality 177-179 (17%)",
            "subsampling": "11",
        }
    ],
    "d3784280d08a8df51e607bde8c8b5ead": [
        {
            "description": "ACD Systems Digital " "Imaging, Quality 80 or " "81",
            "subsampling": "",
        }
    ],
    "d38be79f7c8c6c27a3268275b144add6": [
        {
            "description": "Apple QuickTime, " "Quality 866 (85%)",
            "subsampling": "211111",
        }
    ],
    "d39329b38fdcabe9e1ae5f1b205c825a": [
        {"description": "Apple QuickTime, " "Quality 408 (40%)", "subsampling": "11"}
    ],
    "d3b05f3cd78e0ac3ab37a02152e22831": [
        {"description": "Apple QuickTime, " "Quality 624 (61%)", "subsampling": "11"}
    ],
    "d3c0e7437c630f3bed0867737c5f1921": [
        {"description": "Apple QuickTime, " "Quality 300 (29%)", "subsampling": "11"}
    ],
    "d3ea3c519f92dd870fed03f63cabf05e": [
        {"description": "Apple QuickTime, " "Quality 424 (41%)", "subsampling": "11"}
    ],
    "d3eaad34ae4fc8a3ac6330c1c9dceb28": [
        {"description": "Apple QuickTime, " "Quality 247 (24%)", "subsampling": "11"}
    ],
    "d41d8cd98f00b204e9800998ecf8427e": [
        {"description": "No DQT defined", "subsampling": ""}
    ],
    "d48c2b9e514e25fcc4b3f2408d168d72": [
        {"description": "ACD Systems Digital " "Imaging, Quality 24", "subsampling": ""}
    ],
    "d4bb4c59b5284630a4c716a0290d9091": [
        {
            "description": "Apple QuickTime, " "Quality 416 (41%)",
            "subsampling": "221111",
        }
    ],
    "d4f1922c71a6c96a530a9a8268fbc63b": [
        {"description": "ACD Systems Digital " "Imaging, Quality 88", "subsampling": ""}
    ],
    "d5220fcfa99764e440684fbac6273cff": [
        {
            "description": "Apple QuickTime, " "Quality 482 (47%)",
            "subsampling": "221111",
        }
    ],
    "d528fac9b63536ff52041745945dcb09": [
        {
            "description": "Pentax *istDS, Better " "(edit in camera)",
            "subsampling": "211111",
        }
    ],
    "d55d9744065708d7b6fa7fb6e8eb2453": [
        {
            "description": "Apple QuickTime, " "Quality 458 (45%)",
            "subsampling": "221111",
        }
    ],
    "d57ac6956e4fe86c386f0eef00a5e021": [
        {"description": "Pentax Optio S, Best " "(E)", "subsampling": "221111"}
    ],
    "d58f5d339b69e1296911a3387cc664a4": [
        {
            "description": "Apple QuickTime, " "Quality 389 (38%)",
            "subsampling": "221111",
        }
    ],
    "d5994dbe056ea3544b3256a7a6b53749": [
        {
            "description": "Apple QuickTime, " "Quality 692 (68%)",
            "subsampling": "221111",
        }
    ],
    "d5b2902ae3fcd87e1521da86585e7b3a": [
        {
            "description": "Apple QuickTime, " "Quality 732-733 " "(71-72%)",
            "subsampling": "11",
        }
    ],
    "d5c95455812515ad4855ed725d5bf2d9": [
        {
            "description": "Apple QuickTime, " "Quality 168-170 " "(16-17%)",
            "subsampling": "11",
        }
    ],
    "d5d329f5687d154e4ceeb48697b848ba": [
        {
            "description": "Apple QuickTime, " "Quality 245-246 (24%)",
            "subsampling": "11",
        }
    ],
    "d5d484b68e25b44288e67e699829695c": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "65 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 65",
            "subsampling": "111111",
        },
    ],
    "d5ec901d20f3887007d0f4cfb7d1460d": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 62", "subsampling": ""}
    ],
    "d606add3e7590885ac8978af6d09a2aa": [
        {
            "description": "Apple QuickTime, " "Quality 514 (50%)",
            "subsampling": "221111",
        }
    ],
    "d61168238621bd221ef1eb3dcbe270a3": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 14", "subsampling": ""}
    ],
    "d61807da54a72c4651466049c9f67541": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "74",
            "subsampling": "",
        }
    ],
    "d62cd17e8e04ebd568a8f5abc38cad4a": [
        {"description": "Apple QuickTime, " "Quality 405 (40%)", "subsampling": "11"}
    ],
    "d6390cc36d2f03c1d2dd13d6910ca46b": [
        {
            "description": "ACD Systems Digital "
            "Imaging, Quality 100; "
            "Pentax K20D/OptioE60 "
            "Premium",
            "subsampling": "",
        },
        {
            "description": "Canon Digital Photo " "Professional, Quality " "10",
            "subsampling": "211111",
        },
        {"description": "Canon ZoomBrowser, " "Highest", "subsampling": "211111"},
        {
            "description": "PENTAX PHOTO " "Laboratory, Highest " "quality",
            "subsampling": "211111",
        },
        {
            "description": "Sony Image Data Suite, " "Quality 1 (high " "quality)",
            "subsampling": "211111",
        },
        {
            "description": "Pentax *istDS, Best " "(edit in camera)",
            "subsampling": "211111",
        },
    ],
    "d6438ea5a93b6d4d0ba26de7c56f2634": [
        {
            "description": "Apple QuickTime, " "Quality 904-905 (88%)",
            "subsampling": "11",
        }
    ],
    "d64e7ff8292fd77131932864d3c9ce7c": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "78 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 78",
            "subsampling": "111111",
        },
    ],
    "d67da3fcbac8975acffe7f1ab088f646": [
        {
            "description": "Apple QuickTime, " "Quality 362 (35%)",
            "subsampling": "221111",
        }
    ],
    "d6e206f8224d6a3582fb1066b511437b": [
        {
            "description": "Apple QuickTime, " "Quality 309 (30%)",
            "subsampling": "221111",
        }
    ],
    "d71c8ddb9117920304d83a6f8b7832a4": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 38",
            "subsampling": "221111",
        }
    ],
    "d7437a18e86ac2832d73204acd82aa89": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 21", "subsampling": ""}
    ],
    "d768df38fb51c4b9977e5d7185f97a6c": [
        {"description": "FixFoto, Quality 16", "subsampling": ""}
    ],
    "d781cc6f686fc7c7b9b6eef90fab4d87": [
        {"description": "Apple QuickTime, " "Quality 550 (54%)", "subsampling": "11"}
    ],
    "d798b707a6b83eb54664abe0833b46aa": [
        {"description": "FixFoto, Quality 20", "subsampling": ""}
    ],
    "d7c835210eec5a8bedb3a18d32cbe066": [
        {"description": "Apple QuickTime, " "Quality 389 (38%)", "subsampling": "11"}
    ],
    "d81683c0458d9ad72751530d6fbc1389": [
        {
            "description": "Apple QuickTime, " "Quality 635 (62%)",
            "subsampling": "221111",
        }
    ],
    "d83207842d60965f9d194d89f3281ccd": [
        {
            "description": "Apple QuickTime, " "Quality 245-246 (24%)",
            "subsampling": "221111",
        }
    ],
    "d835580b2be669d4aa6c68ead27c0c2f": [
        {
            "description": "Apple QuickTime, " "Quality 202-203 (20%)",
            "subsampling": "221111",
        }
    ],
    "d876e8934da14a985abda0ebe722bbee": [
        {"description": "Apple QuickTime, " "Quality 720 (70%)", "subsampling": "11"}
    ],
    "d8bd88390c27b2b05a0784eafd4b31ef": [
        {
            "description": "Apple QuickTime, " "Quality 318 (31%)",
            "subsampling": "221111",
        }
    ],
    "d8c5179c2419775f43e9a7899bacddd7": [
        {"description": "Apple QuickTime, " "Quality 528 (52%)", "subsampling": "11"}
    ],
    "d8c54333eb475b8db9f32f11fe96337e": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "89 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 89",
            "subsampling": "111111",
        },
    ],
    "d8cd0ca367d9afaf9a1aca0415da5361": [
        {
            "description": "Apple QuickTime, " "Quality 800 (78%)",
            "subsampling": "211111",
        }
    ],
    "d8ef40736b072f09bead5f73f5ec1372": [
        {"description": "Nikon Capture NX, " "Quality 79", "subsampling": "211111"}
    ],
    "d91cd4a2dcd1a29e6ef652ebcfdd58d7": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 73", "subsampling": ""}
    ],
    "d92c5bba7cfd1bfbb8c662c1a27ca413": [
        {"description": "Apple QuickTime, " "Quality 412 (40%)", "subsampling": "11"}
    ],
    "d94d79b70686d3e2568d61d07e5819eb": [
        {"description": "Apple QuickTime, " "Quality 418 (41%)", "subsampling": "11"}
    ],
    "d9653333a3af8842dd4b72856ac4ef4e": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 42",
            "subsampling": "221111",
        }
    ],
    "d9696efa02b9de813caf8d684b06346f": [
        {
            "description": "Apple QuickTime, " "Quality 561 (55%)",
            "subsampling": "221111",
        }
    ],
    "d973f38c501796adff40c4f70cbd8885": [
        {"description": "Apple QuickTime, " "Quality 638 (62%)", "subsampling": "11"}
    ],
    "d9794fa54e2ef47be48b972cdca910c2": [
        {
            "description": "Apple QuickTime, " "Quality 569 (56%)",
            "subsampling": "221111",
        }
    ],
    "d97b27b45fdbe82a79364e0939adbf90": [
        {"description": "Pentax K10D (AI)", "subsampling": "121111"}
    ],
    "d9a914baea5468bb52c09d1d0b5bd131": [
        {"description": "Apple QuickTime, " "Quality 887 (87%)", "subsampling": "11"}
    ],
    "d9dadfb6f0a25765abe00e69857c5520": [
        {"description": "Nikon Capture NX, " "Quality 27", "subsampling": "221111"}
    ],
    "d9e0a4c08ef5d7f72eecce74c94c054d": [
        {
            "description": "Apple QuickTime, " "Quality 713 (70%)",
            "subsampling": "221111",
        }
    ],
    "d9e503dc2dd4f6493be988ecb0f44f2c": [
        {
            "description": "Apple QuickTime, " "Quality 793-795 " "(77-78%)",
            "subsampling": "11",
        }
    ],
    "da2501a6f59b2256adb0833b58b504f2": [
        {
            "description": "Apple QuickTime, " "Quality 709 (69%)",
            "subsampling": "221111",
        }
    ],
    "da29cc9a4d5fd7e0dc36a2dd0c70e84f": [
        {"description": "Apple QuickTime, " "Quality 539 (53%)", "subsampling": "11"}
    ],
    "da4c88f145393972fbe9d3f40838cab9": [
        {"description": "Apple QuickTime, " "Quality 587 (57%)", "subsampling": "11"}
    ],
    "dab4fa97da49aa37889185c5b43917c1": [
        {"description": "Apple QuickTime, " "Quality 651 (64%)", "subsampling": "11"}
    ],
    "db1ae392a31d30cd5564dc7bbea24019": [
        {
            "description": "Apple QuickTime, " "Quality 542 (53%)",
            "subsampling": "221111",
        }
    ],
    "db5b3a078a942131b5d86bc189baac24": [
        {
            "description": "Apple QuickTime, " "Quality 779 (76%)",
            "subsampling": "211111",
        }
    ],
    "db87a4c5c1d4e03dc6645bcf0535a930": [
        {"description": "Pentax K10D (AJ)", "subsampling": "211111"}
    ],
    "db8d4df12405d0d69eb25f06a963ac5b": [
        {"description": "Canon DV", "subsampling": "211111"}
    ],
    "dba2f5203ffecada66a8bf9b1272f1eb": [
        {"description": "Apple QuickTime, " "Quality 510 (50%)", "subsampling": "11"}
    ],
    "dbb17a02e661f2475411fc1dc37902ef": [
        {"description": "Apple Aperture Quality " "2", "subsampling": "221111"}
    ],
    "dbdc6a6f3c9ffff19e67cfad2cc51ae4": [
        {
            "description": "Apple QuickTime, " "Quality 0-63 (0-6%)",
            "subsampling": "221111",
        }
    ],
    "dbee605b07dfe30c992622877dffb049": [
        {
            "description": "Apple QuickTime, " "Quality 204-205 (20%)",
            "subsampling": "11",
        }
    ],
    "dc0278d78fa5c8daf84f8c2672f582c6": [
        {
            "description": "Apple QuickTime, " "Quality 932-933 (91%)",
            "subsampling": "11",
        }
    ],
    "dc0dc92085037072e27247f64af0f22d": [
        {"description": "ACD Systems Digital " "Imaging, Quality 7", "subsampling": ""}
    ],
    "dc149d41f08d16cb9d52a5bdd487a67e": [
        {
            "description": "Pentax " "*istD/K100Dsuper/Optio300GS, " "Best",
            "subsampling": "121111",
        }
    ],
    "dc19a48af9051bbdc54cf7e88c03f13e": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 88",
            "subsampling": "111111",
        }
    ],
    "dc2af4340202aa481491b86539888720": [
        {"description": "Apple QuickTime, " "Quality 402 (39%)", "subsampling": "11"}
    ],
    "dca5476d81d0ceca97f480fecd09b23c": [
        {"description": "Pentax K10D (AN)", "subsampling": "211111"}
    ],
    "dcc3ffcda228ab283d53e1dc2cb739ef": [
        {
            "description": "Apple QuickTime, " "Quality 322-324 " "(31-32%)",
            "subsampling": "221111",
        }
    ],
    "dccca51d261b315120f069697872377d": [
        {
            "description": "Apple QuickTime, " "Quality 223-224 (22%)",
            "subsampling": "11",
        }
    ],
    "dcecd4f366d521e118e94d87ef915caa": [
        {
            "description": "Apple QuickTime, " "Quality 441 (43%)",
            "subsampling": "221111",
        }
    ],
    "dcfe5898ec101a8b2bf98330445dd1bf": [
        {"description": "Apple QuickTime, " "Quality 639 (62%)", "subsampling": "11"}
    ],
    "dd0a023941d7bfd118d272f4f925e6e2": [
        {
            "description": "Apple QuickTime, " "Quality 702 (69%)",
            "subsampling": "221111",
        }
    ],
    "dd54b4e3d8801f3a7969be542d165c6b": [
        {
            "description": "Apple QuickTime, " "Quality 110-116 (11%)",
            "subsampling": "11",
        }
    ],
    "dd71fdab3d46341a9b6ca0b6c6929d23": [
        {"description": "Apple QuickTime, " "Quality 535 (52%)", "subsampling": "11"}
    ],
    "dd757185a44c3d6222e9d16a0c2ee890": [
        {"description": "Apple QuickTime, " "Quality 895 (87%)", "subsampling": "11"}
    ],
    "dd8ad8ce688c4248f924022c38d3228c": [
        {"description": "Pentax Optio 43WR, Good", "subsampling": "211111"}
    ],
    "dd9b9d09a624deab730d9bd5b8825baa": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "79",
            "subsampling": "",
        }
    ],
    "ddbc4e6566bbcc74b6205526393ef468": [
        {
            "description": "Apple QuickTime, " "Quality 530 (52%)",
            "subsampling": "221111",
        }
    ],
    "ddc90333cb2279aa533a339710bd81ef": [
        {"description": "Apple QuickTime, " "Quality 906 (88%)", "subsampling": "11"}
    ],
    "dddc3adae44a64457b05416affc2502e": [
        {
            "description": "Apple QuickTime, " "Quality 306 (30%)",
            "subsampling": "221111",
        }
    ],
    "ddf1f3b922ea51f6f4ca3cb6863eeae0": [
        {
            "description": "Apple QuickTime, " "Quality 260-261 (25%)",
            "subsampling": "221111",
        }
    ],
    "de0547c872fed9c9c75c8fec2fe010e6": [
        {"description": "Apple QuickTime, " "Quality 416 (41%)", "subsampling": "11"}
    ],
    "de0c784b75953851dc370f4daecfa1a9": [
        {"description": "Nikon Capture NX, " "Quality 21", "subsampling": "221111"}
    ],
    "de0fb6d13e12e8df26140dd74691bf0f": [
        {
            "description": "Adobe Lightroom, " "Quality 39% - 46%",
            "subsampling": "221111",
        }
    ],
    "de3aa6ed96eaf3ed3cd3ea70a2f75002": [
        {"description": "Apple QuickTime, " "Quality 722 (71%)", "subsampling": "11"}
    ],
    "de6a322383022ee8d966e848a2df4f28": [
        {
            "description": "Apple QuickTime, " "Quality 444 (43%)",
            "subsampling": "221111",
        }
    ],
    "de802b8c64d7f854081c7df6ed345b43": [
        {
            "description": "Apple QuickTime, " "Quality 549 (54%)",
            "subsampling": "221111",
        }
    ],
    "de8310d09116a7a62965f3e0e43ef525": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "66 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 66",
            "subsampling": "111111",
        },
    ],
    "de93dd8ab7918b25f191923f4a43a5c2": [
        {
            "description": "Apple QuickTime, " "Quality 417 (41%)",
            "subsampling": "221111",
        }
    ],
    "de94c5591bafc7456ccaef430271b907": [
        {
            "description": "Adobe Lightroom, " "Quality 70% - 76%",
            "subsampling": "111111",
        },
        {"description": "Adobe Photoshop, " "Quality 9", "subsampling": "111111"},
    ],
    "deaa8bbd7c5414b93d8029aa14a76d3a": [
        {"description": "ACD Systems Digital " "Imaging, Quality 83", "subsampling": ""}
    ],
    "debd5adf671e3b907c10155cc910dcc1": [
        {"description": "Apple QuickTime, " "Quality 363 (35%)", "subsampling": "11"}
    ],
    "dec0717305bae8309a934e1d6a251d88": [
        {"description": "ACD Systems Digital " "Imaging, Quality 19", "subsampling": ""}
    ],
    "df02b0ea9dab7d291950b6cfc65c4bb1": [
        {"description": "Apple QuickTime, " "Quality 478 (47%)", "subsampling": "11"}
    ],
    "df1b50991b82b66c82dc856cf82383da": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "36",
            "subsampling": "",
        }
    ],
    "df54eb20ec90f41f1e6c37e241ee381c": [
        {"description": "Nikon Capture NX, " "Quality 84", "subsampling": "111111"}
    ],
    "df6535865562ce7cbf08e9368e991a95": [
        {
            "description": "Apple QuickTime, " "Quality 583 (57%)",
            "subsampling": "221111",
        }
    ],
    "df8ea903695e76e4b1466bdd3a3480c7": [
        {
            "description": "Apple QuickTime, " "Quality 899 (88%)",
            "subsampling": "211111",
        }
    ],
    "dfb203555c34fe146c526350e11309eb": [
        {
            "description": "Apple QuickTime, " "Quality 724 (71%)",
            "subsampling": "221111",
        }
    ],
    "dfcbd3df5c6b96106e6348b77f89c56a": [
        {"description": "Apple QuickTime, " "Quality 254 (25%)", "subsampling": "11"}
    ],
    "dffb0a244fa54783569693edf84d1cda": [
        {
            "description": "Apple QuickTime, " "Quality 891-893 (87%)",
            "subsampling": "11",
        }
    ],
    "e002d9728c73f60e4d0509e1cea9af43": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "13",
            "subsampling": "",
        }
    ],
    "e032225ecdcf1d91d85626df59a2d0c6": [
        {"description": "Apple QuickTime, " "Quality 693 (68%)", "subsampling": "11"}
    ],
    "e06d44ffef23792c88f215a5b2ed9478": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "35",
            "subsampling": "",
        }
    ],
    "e06eb7848ec8766239ff014aa8b62e49": [
        {"description": "Nikon D80, Normal", "subsampling": "211111"}
    ],
    "e082971717023e667f3d922bbccf089b": [
        {
            "description": "Apple QuickTime, " "Quality 546 (53%)",
            "subsampling": "221111",
        }
    ],
    "e09026128c9880b44ac71224f477cd3b": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 94", "subsampling": ""}
    ],
    "e0c38f0c5e6562445d4e92bae51713be": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "42 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 42",
            "subsampling": "111111",
        },
    ],
    "e10030f09a14acdd647eff13c0bf333a": [
        {
            "description": "Pentax " "*istD/DS/DS2/K100D/Optio330GS/33L, " "Best",
            "subsampling": "211111",
        }
    ],
    "e168523157ee45551ba30378d597dfd6": [
        {"description": "Apple QuickTime, " "Quality 366 (36%)", "subsampling": "11"}
    ],
    "e1e122ebb2733a5ccdb5ff1cdce86d4d": [
        {"description": "ACD Systems Digital " "Imaging, Quality 72", "subsampling": ""}
    ],
    "e1fedef5184beeb7b0f5c055c7ae1d31": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "95 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 95",
            "subsampling": "111111",
        },
    ],
    "e215df38e258b3d8bceb57aa64388d26": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 11", "subsampling": ""}
    ],
    "e22b26930415798b7ecf2b060c1cdc2a": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "61",
            "subsampling": "",
        }
    ],
    "e230e3ac7c740f3e8fe6bc74fff72c10": [
        {"description": "Apple QuickTime, " "Quality 399 (39%)", "subsampling": "11"}
    ],
    "e2408846813c1f5c7f5ce3cf69e741c4": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "9",
            "subsampling": "",
        }
    ],
    "e2b368a164b67e15598683f9f184bd77": [
        {
            "description": "Apple QuickTime, " "Quality 715 (70%)",
            "subsampling": "221111",
        }
    ],
    "e2cccecebc01c7d8a4fca2dab682ba8f": [
        {
            "description": "Apple QuickTime, " "Quality 1005-1009 " "(98-99%)",
            "subsampling": "11",
        }
    ],
    "e2d2755891b4e4bc5f7c8d76dcbb0d53": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 15", "subsampling": ""}
    ],
    "e2fe91d57078586f15b09e3b9c8cd3fa": [
        {"description": "Apple QuickTime, " "Quality 326 (32%)", "subsampling": "11"}
    ],
    "e3042cbd43d2067ae92e1a8ce3f2c5a1": [
        {"description": "Apple QuickTime, " "Quality 534 (52%)", "subsampling": "11"}
    ],
    "e331a0dd2c53616c2881bb381fc4c1e2": [
        {"description": "Apple QuickTime, " "Quality 782 (76%)", "subsampling": "11"}
    ],
    "e346ce6e3bee6abff16420f5ba95ceb9": [
        {
            "description": "Apple QuickTime, " "Quality 493 (48%)",
            "subsampling": "221111",
        }
    ],
    "e34d11f979458a87492b57eabfd4f4ea": [
        {
            "description": "Apple QuickTime, " "Quality 574 (56%)",
            "subsampling": "221111",
        }
    ],
    "e395118c42b6492dd4d9d30754f0a697": [
        {"description": "Apple QuickTime, " "Quality 438 (43%)", "subsampling": "11"}
    ],
    "e39b60fcecf3221d14c62dc13ddf4726": [
        {"description": "Nikon Capture NX, " "Quality 11", "subsampling": "221111"}
    ],
    "e3cc8a85db1a32e81650b9668b98644a": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "8",
            "subsampling": "",
        }
    ],
    "e3e7280c8a9e82d31e22d24d5b733580": [
        {
            "description": "ACD Systems Digital " "Imaging, Quality 35 or " "36",
            "subsampling": "",
        }
    ],
    "e3e88302627b6743725cace74ddb17f9": [
        {"description": "Apple QuickTime, " "Quality 446 (44%)", "subsampling": "11"}
    ],
    "e40f6a9a3daf4bfc42aedcb9107076ea": [
        {"description": "Apple QuickTime, " "Quality 962 (94%)", "subsampling": "11"}
    ],
    "e41806d0928fbb5552225e10db7b55d0": [
        {
            "description": "Apple QuickTime, " "Quality 412 (40%)",
            "subsampling": "221111",
        }
    ],
    "e41e5416e21dbfb5a41f006b3485f5bb": [
        {
            "description": "Apple QuickTime, " "Quality 513 (50%)",
            "subsampling": "221111",
        }
    ],
    "e43438348a912a2210261472d1a747ab": [
        {"description": "Apple QuickTime, " "Quality 899 (88%)", "subsampling": "11"}
    ],
    "e454ca92aca849d59b873d9be817baea": [
        {"description": "Apple QuickTime, " "Quality 633 (62%)", "subsampling": "11"}
    ],
    "e456c998dc126c1efad013eb7b0186c1": [
        {"description": "Nikon Capture NX, " "Quality 48", "subsampling": "221111"}
    ],
    "e4735f63e88baf04599afc034e690845": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "67 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 67",
            "subsampling": "111111",
        },
    ],
    "e477932560b308940ac7439eed9f63da": [
        {"description": "Apple QuickTime, " "Quality 454 (44%)", "subsampling": "11"}
    ],
    "e47902bc7ba3037921010c568648c8c3": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 27",
            "subsampling": "221111",
        }
    ],
    "e4b0c56d41f4af9e10971876ad7ad56d": [
        {
            "description": "Apple QuickTime, " "Quality 734 (72%)",
            "subsampling": "221111",
        }
    ],
    "e4d76c3cd4d36b72537a2234a3597933": [
        {"description": "Apple QuickTime, " "Quality 850 (83%)", "subsampling": "11"}
    ],
    "e4e5bc705c40cfaffff6565f16fe98a9": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "13 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 13",
            "subsampling": "111111",
        },
    ],
    "e55b5345d9668d1b11b657537f707072": [
        {"description": "Apple QuickTime, " "Quality 499 (49%)", "subsampling": "11"}
    ],
    "e55e0c1adbbca8b9d100881248050eb5": [
        {"description": "Pentax Optio 43WR, " "Better", "subsampling": "211111"}
    ],
    "e566eaef7eacd6c7161feebf4cec79e8": [
        {"description": "Apple QuickTime, " "Quality 665 (65%)", "subsampling": "11"}
    ],
    "e56ca8f4da20395ec1f87d380198fa0a": [
        {
            "description": "Apple QuickTime, " "Quality 595 (58%)",
            "subsampling": "221111",
        }
    ],
    "e56cf84423c16869a9a4fd6605b15ba4": [
        {"description": "Apple QuickTime, " "Quality 684 (67%)", "subsampling": "11"}
    ],
    "e57a9878be74473990343573c6585f79": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 48",
            "subsampling": "221111",
        }
    ],
    "e582a5f93f66cf34facfba5918a1d9e2": [
        {"description": "Apple QuickTime, " "Quality 772 (75%)", "subsampling": "11"}
    ],
    "e5abf48ce0cc2b4a3db7eca3a1112b7a": [
        {"description": "Nikon Capture NX, " "Quality 88", "subsampling": "111111"}
    ],
    "e5b0739f8e02c6d481e0cdafe7326ae2": [
        {
            "description": "Apple QuickTime, " "Quality 192-194 (19%)",
            "subsampling": "221111",
        }
    ],
    "e5dcd017a9734f9f0e18b515c7fa1787": [
        {
            "description": "Apple QuickTime, " "Quality 396 (39%)",
            "subsampling": "221111",
        }
    ],
    "e5deb190a5e17492a01e8136afdfd6c1": [
        {
            "description": "Apple QuickTime, " "Quality 289 (28%)",
            "subsampling": "221111",
        }
    ],
    "e5ec78e112e3ba6463de24b3518347eb": [
        {"description": "Apple QuickTime, " "Quality 609 (59%)", "subsampling": "11"}
    ],
    "e66c03f97b19213f385136f014c78ac1": [
        {
            "description": "Apple QuickTime, " "Quality 466-467 (46%)",
            "subsampling": "221111",
        },
        {
            "description": "Canon Digital Photo " "Professional, Quality 5",
            "subsampling": "211111",
        },
        {"description": "Canon ZoomBrowser, Low", "subsampling": "211111"},
    ],
    "e67a8a7e92a9f03413e9a67b99624b8b": [
        {
            "description": "Apple QuickTime, " "Quality 876-877 (86%)",
            "subsampling": "211111",
        }
    ],
    "e68841bf28d33d749d0031bfe3a5219c": [
        {
            "description": "Apple QuickTime, " "Quality 605 (59%)",
            "subsampling": "221111",
        }
    ],
    "e69be2174dbbfb952e54576fbdfe6c14": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 62",
            "subsampling": "111111",
        }
    ],
    "e6a0a679a13a99de16e13c6ea2829deb": [
        {
            "description": "Apple QuickTime, " "Quality 660-661 " "(64-65%)",
            "subsampling": "221111",
        }
    ],
    "e6c99d520b86fd6f5eb513d1a084324e": [
        {
            "description": "Apple QuickTime, " "Quality 808 (79%)",
            "subsampling": "211111",
        }
    ],
    "e76c1b26bbd196efe2e793e27727704d": [
        {"description": "Apple QuickTime, " "Quality 545 (53%)", "subsampling": "11"}
    ],
    "e76d86e8de4f0bf9e58cd389e0a8c117": [
        {
            "description": "Apple QuickTime, " "Quality 629 (61%)",
            "subsampling": "221111",
        }
    ],
    "e78229129afca214a07ad978262c545e": [
        {
            "description": "Apple QuickTime, " "Quality 947-951 " "(92-93%)",
            "subsampling": "11",
        }
    ],
    "e7914fbf6c9b2a127af3676726e6bd8b": [
        {
            "description": "Apple QuickTime, " "Quality 452 (44%)",
            "subsampling": "221111",
        }
    ],
    "e7b9303f785f78a2cb27f83616c18726": [
        {
            "description": "Apple QuickTime, " "Quality 365 (36%)",
            "subsampling": "221111",
        }
    ],
    "e7e7befa282a985a0532634f360df7db": [
        {
            "description": "Apple QuickTime, " "Quality 600 (59%)",
            "subsampling": "221111",
        }
    ],
    "e7f293f640878b53fe95a7cb0b1dcc83": [
        {
            "description": "Apple QuickTime, " "Quality 711-712 " "(69-70%)",
            "subsampling": "221111",
        }
    ],
    "e800426d2ef8d3cda13a0b41f1b2cc5a": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "10",
            "subsampling": "",
        }
    ],
    "e8032085aa55f664f7f74201ac10bb99": [
        {"description": "Apple QuickTime, " "Quality 735 (72%)", "subsampling": "11"}
    ],
    "e83f8505dc3f5f46b37e22b590f71b98": [
        {
            "description": "Apple QuickTime, " "Quality 516 (50%)",
            "subsampling": "221111",
        }
    ],
    "e8b31dbd18c91229a3c40356efeb2622": [
        {
            "description": "Apple QuickTime, " "Quality 460 (45%)",
            "subsampling": "221111",
        }
    ],
    "e8b4ef8f94d89c59c855758a73ec451f": [
        {"description": "Apple QuickTime, " "Quality 682 (67%)", "subsampling": "11"}
    ],
    "e8bdbff8c7908e36c51e1344c0e99746": [
        {"description": "Apple QuickTime, " "Quality 309 (30%)", "subsampling": "11"}
    ],
    "e8ff3d165b4c028c18ec8a8f940a12a1": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 18", "subsampling": ""}
    ],
    "e9206045838e9f5f9bd207744254e96d": [
        {"description": "Pentax Optio 430, Best", "subsampling": "221111"}
    ],
    "e9275719ef4cb335f9dfed63c3737f0e": [
        {
            "description": "Apple QuickTime, " "Quality 252-253 (25%)",
            "subsampling": "11",
        }
    ],
    "e93244fdb14bb27a2c30ee133b3e9f5e": [
        {"description": "Apple QuickTime, " "Quality 857 (84%)", "subsampling": "11"}
    ],
    "e9387b4065bba8570375d6535ab2124b": [
        {"description": "Nikon Capture NX, " "Quality 52", "subsampling": "221111"}
    ],
    "e9555e593a6fd9aeee399de16080cd61": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 30", "subsampling": ""}
    ],
    "e97694f0093de13987a335e131b30eb0": [
        {"description": "Pentax Optio SVi, Best", "subsampling": "221111"}
    ],
    "e9c647b8bf2d7535d259eed6fbabe206": [
        {"description": "Apple QuickTime, " "Quality 288 (28%)", "subsampling": "11"}
    ],
    "e9ef286567fd84a1f479b35ca00db43c": [
        {"description": "Adobe Photoshop, " "Quality 2", "subsampling": "11"}
    ],
    "ea25d0beaa91434a14348fb60f5cff31": [
        {
            "description": "Apple QuickTime, " "Quality 398 (39%)",
            "subsampling": "221111",
        }
    ],
    "ea2f997a0261bab501bf122b04cbc859": [
        {"description": "Canon EOS 1DSmkII, Fine", "subsampling": "211111"}
    ],
    "ea445840d29c51009a2a8cd49b96ccee": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "72 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 72",
            "subsampling": "111111",
        },
    ],
    "ea50813e06203c2ad1165252bcb99a1d": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "48 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 48",
            "subsampling": "111111",
        },
    ],
    "ea65bdd87f78f7507fe6098473cbe0c9": [
        {"description": "Apple QuickTime, " "Quality 751 (73%)", "subsampling": "11"}
    ],
    "eaead98bbdfde35210f48286662e8ad2": [
        {"description": "Canon DV Hi-Res", "subsampling": "211111"}
    ],
    "eaffe0714878be5fb67a914f5bb79fef": [
        {"description": "Apple QuickTime, " "Quality 302 (29%)", "subsampling": "11"}
    ],
    "eb4eb617beaa4f23acf41167742806fc": [
        {
            "description": "Apple QuickTime, " "Quality 900-901 (88%)",
            "subsampling": "211111",
        }
    ],
    "eb625c64e32314f51dc4286564a71f7b": [
        {"description": "Panasonic DMC-FZ10, " "High", "subsampling": "211111"}
    ],
    "eb68a0ff9c83267e5fb5e998365b4480": [
        {
            "description": "Apple QuickTime, " "Quality 392 (38%)",
            "subsampling": "221111",
        }
    ],
    "eb728dc3105ddb5a0597384b54ed948c": [
        {"description": "Apple QuickTime, " "Quality 931 (91%)", "subsampling": "11"}
    ],
    "eb7d90d291044d1bd8f40ca1b3ce0ddf": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 91", "subsampling": ""}
    ],
    "eb8e5c42d31b916737ac21dffd6f012b": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 47",
            "subsampling": "221111",
        }
    ],
    "eb9d48d135b2c61c51fc3f23b0001b4d": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 44", "subsampling": ""}
    ],
    "ebb774b4e106d1a9df5824958d4e5a95": [
        {
            "description": "Apple QuickTime, " "Quality 650 (63%)",
            "subsampling": "221111",
        }
    ],
    "ebce337e9ef5a07775cebe40d7623862": [
        {
            "description": "Apple QuickTime, " "Quality 469 (46%)",
            "subsampling": "221111",
        }
    ],
    "ebd575cf069eb906d2f2b2e202f67247": [
        {
            "description": "Apple QuickTime, " "Quality 226-227 (22%)",
            "subsampling": "11",
        }
    ],
    "ebf82c50697d66a6913727095299f192": [
        {
            "description": "Apple QuickTime, " "Quality 694-695 (68%)",
            "subsampling": "11",
        }
    ],
    "ec2fd56a50df0e42498018d441a3aa75": [
        {
            "description": "Apple QuickTime, " "Quality 624 (61%)",
            "subsampling": "221111",
        }
    ],
    "ec440a2ffcbce8895beb663b36975073": [
        {
            "description": "Apple QuickTime, " "Quality 780-781 (76%)",
            "subsampling": "211111",
        }
    ],
    "ec662935c494c5abd6f6c907f77be65c": [
        {
            "description": "Apple QuickTime, " "Quality 941-943 (92%)",
            "subsampling": "11",
        }
    ],
    "ec6c55677b94970bc09f70265f1d5b55": [
        {
            "description": "Canon Digital Photo " "Professional, Quality 2",
            "subsampling": "211111",
        }
    ],
    "ec76274ff22c07e53299ad34633ba88f": [
        {
            "description": "Apple QuickTime, " "Quality 1021-1023 " "(100%)",
            "subsampling": "211111",
        }
    ],
    "ec994ef421efd6bc78671858b9f942ad": [
        {"description": "ACD Systems Digital " "Imaging, Quality 89", "subsampling": ""}
    ],
    "ecbf939a145939d5aa48fc3c9e19cfe8": [
        {"description": "Apple QuickTime, " "Quality 787 (77%)", "subsampling": "11"}
    ],
    "ececf8dfa473110534b506db58d98f15": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 42", "subsampling": ""}
    ],
    "ed3d3b9ff9faf0009e44b9803f6295d7": [
        {"description": "FixFoto, Quality 18", "subsampling": ""}
    ],
    "ed6aec096e8776b483b2c2b3d7e15d76": [
        {
            "description": "ACD Systems Digital " "Imaging, Quality 10 or " "11",
            "subsampling": "",
        }
    ],
    "ed6b90ca62ed648d1102e1c506a0af26": [
        {
            "description": "Apple QuickTime, " "Quality 626 (61%)",
            "subsampling": "221111",
        }
    ],
    "ed923fdb1e5009215a49c0d92061c3b0": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "38",
            "subsampling": "",
        }
    ],
    "edb0be7fcce943c28d02ff78ae600afb": [
        {
            "description": "Apple QuickTime, " "Quality 850 (83%)",
            "subsampling": "211111",
        }
    ],
    "edda5d6ae456d4cdccec80e390ac9279": [
        {
            "description": "Apple QuickTime, " "Quality 472 (46%)",
            "subsampling": "221111",
        }
    ],
    "ee1c033afaf4cd5263ff2b1c1ff8966c": [
        {"description": "Canon PowerShot, " "Superfine", "subsampling": "211111"}
    ],
    "ee58773aa7b774040d650365937cf173": [
        {
            "description": "Apple QuickTime, " "Quality 300 (29%)",
            "subsampling": "221111",
        }
    ],
    "ee5b4ed7f04821d1e3a509d7565cb10d": [
        {
            "description": "Apple QuickTime, " "Quality 865 (84%)",
            "subsampling": "211111",
        }
    ],
    "eef05c558c1aba5cf2891fb13ee07167": [
        {"description": "Apple QuickTime, " "Quality 504 (49%)", "subsampling": "11"}
    ],
    "eef3afec34329517513541a8509b7aab": [
        {"description": "Apple QuickTime, " "Quality 397 (39%)", "subsampling": "11"}
    ],
    "ef0cd1902fb1afe284468a67eaffd078": [
        {"description": "Nikon Capture NX, " "Quality 49", "subsampling": "221111"},
        {
            "description": "Pentax " "*istDS/K100D/K100Dsuper, " "Good",
            "subsampling": "211111",
        },
    ],
    "ef4fa43f4d548e0687c4d4151a0bf1bd": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 91",
            "subsampling": "111111",
        }
    ],
    "ef511ac2c9d7153c16e3e1846325b727": [
        {"description": "Apple QuickTime, " "Quality 681 (67%)", "subsampling": "11"}
    ],
    "ef938a0533502fe19f311d46c43fa86c": [
        {
            "description": "Apple QuickTime, " "Quality 214-215 (21%)",
            "subsampling": "11",
        }
    ],
    "efa024d741ecc5204e7edd4f590a7a25": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "3 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 3",
            "subsampling": "111111",
        },
    ],
    "efbc50df45bc1d1fbbbd29c3e5de04b2": [
        {"description": "Nikon Capture NX, " "Quality 1", "subsampling": "221111"}
    ],
    "efbe7634221900639b3c072395c61bef": [
        {"description": "Pentax K10D (AO)", "subsampling": "211111"}
    ],
    "efd780e10dcd0ab8ca0a0f4f3cb215d3": [
        {
            "description": "Apple QuickTime, " "Quality 419 (41%)",
            "subsampling": "221111",
        }
    ],
    "eff737b226fbce48c42625c5bf9dabb6": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "44 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 44",
            "subsampling": "111111",
        },
    ],
    "f04fed79cdc47709d649187cfcc7e342": [
        {
            "description": "Apple QuickTime, " "Quality 846-849 (83%)",
            "subsampling": "211111",
        }
    ],
    "f05c48d79edbefdb4d260dc23cf258e6": [
        {"description": "Apple QuickTime, " "Quality 462 (45%)", "subsampling": "11"}
    ],
    "f06ddea698cebe653bdd0c208c3d8c95": [
        {"description": "Apple QuickTime, " "Quality 443 (43%)", "subsampling": "11"}
    ],
    "f080b02331ac8adf03de2281042d2b49": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "74 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 74",
            "subsampling": "111111",
        },
    ],
    "f0e3f635bbcf96654812e8c78b227701": [
        {"description": "Apple QuickTime, " "Quality 506 (49%)", "subsampling": "11"}
    ],
    "f0ebdd8d44ac1a80727041a087553847": [
        {"description": "Apple QuickTime, " "Quality 687 (67%)", "subsampling": "11"}
    ],
    "f1262dfcada6e6c2cd4b9fa7e881233b": [
        {"description": "Pentax *istDL/DS, " "Better", "subsampling": "211111"}
    ],
    "f178977e9e0133711f395943816d26aa": [
        {"description": "Apple QuickTime, " "Quality 723 (71%)", "subsampling": "11"}
    ],
    "f1a8af8c0abe4b3423d5ac8c6273a7ca": [
        {
            "description": "Apple QuickTime, " "Quality 432 (42%)",
            "subsampling": "221111",
        }
    ],
    "f1b005980104aac41b49973beed9c8c2": [
        {"description": "ACD Systems Digital " "Imaging, Quality 78", "subsampling": ""}
    ],
    "f1c23475d19d9e950dbc4086902365a3": [
        {"description": "Apple QuickTime, " "Quality 401 (39%)", "subsampling": "11"}
    ],
    "f1d9a0410c5ea11613569783625f5cf3": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "24",
            "subsampling": "",
        }
    ],
    "f1de58c1c6a48dc36ce7e8c69636539c": [
        {
            "description": "Apple QuickTime, " "Quality 544 (53%)",
            "subsampling": "221111",
        }
    ],
    "f1e8d9b3d66fa34ec9a51a987b48a159": [
        {
            "description": "Apple QuickTime, " "Quality 223-224 (22%)",
            "subsampling": "221111",
        }
    ],
    "f20a253d2513f4d8f2cfeea980852820": [
        {"description": "Apple QuickTime, " "Quality 451 (44%)", "subsampling": "11"}
    ],
    "f2423a8ae68a49cc6191a2ec80367893": [
        {
            "description": "Apple QuickTime, " "Quality 1005-1006 (98%)",
            "subsampling": "211111",
        }
    ],
    "f251d4554524d22f94a34668ab17957c": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "93",
            "subsampling": "",
        }
    ],
    "f2d84e1114ef85682818b96720d439b5": [
        {"description": "Apple QuickTime, " "Quality 578 (56%)", "subsampling": "11"}
    ],
    "f30792e8fad278c3e1677b5f5b74c682": [
        {
            "description": "Apple QuickTime, " "Quality 716-717 (70%)",
            "subsampling": "221111",
        }
    ],
    "f3235a7d187d083b7b7ead949653f730": [
        {
            "description": "PENTAX PHOTO " "Laboratory, High " "quality",
            "subsampling": "211111",
        },
        {"description": "Pentax K20D/K200D, Best " "(D)", "subsampling": "211111"},
    ],
    "f3526abe33de71ad0eb728c9d446b545": [
        {"description": "Apple QuickTime, " "Quality 896 (88%)", "subsampling": "11"}
    ],
    "f3795398903c82e1beababf95d3a8413": [
        {"description": "Apple QuickTime, " "Quality 561 (55%)", "subsampling": "11"}
    ],
    "f3a55e422a4ab829b2c1f5a1784ce9f6": [
        {"description": "Nikon Capture NX, " "Quality 53", "subsampling": "221111"}
    ],
    "f3c42f077883313db21c72bd240de05f": [
        {
            "description": "Apple QuickTime, " "Quality 276 (27%)",
            "subsampling": "221111",
        }
    ],
    "f3e1672b93ff159231c51b1b157e45fd": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 53", "subsampling": ""}
    ],
    "f3ef06f90579eaf1008e07b94e818a40": [
        {"description": "Apple QuickTime, " "Quality 531 (52%)", "subsampling": "11"}
    ],
    "f40fb322c4bde68a2902c86c613af841": [
        {
            "description": "Apple QuickTime, " "Quality 674 (66%)",
            "subsampling": "221111",
        }
    ],
    "f45d495d3b470eadba70bcca888042b3": [
        {
            "description": "Apple QuickTime, " "Quality 380 (37%)",
            "subsampling": "221111",
        }
    ],
    "f4693035f8db19e0788f41255c3c052e": [
        {"description": "Nikon Capture NX, " "Quality 50", "subsampling": "221111"}
    ],
    "f46e96afa026233c1662c9114feb61e9": [
        {"description": "Nikon Capture NX, " "Quality 42", "subsampling": "221111"}
    ],
    "f4923d7b7dedd365646169e720eee427": [
        {"description": "Apple QuickTime, " "Quality 600 (59%)", "subsampling": "11"}
    ],
    "f4d19ed563e2d0519d6a547088771ddb": [
        {"description": "Adobe Photoshop, " "Quality 1", "subsampling": "11"}
    ],
    "f4dba22dd251350a21f8122f2777e7b0": [
        {"description": "Pentax K10D (AP)", "subsampling": "211111"}
    ],
    "f4f9d5c07c78e8700a6f3def0782a18e": [
        {"description": "ACD Systems Digital " "Imaging, Quality 2", "subsampling": ""}
    ],
    "f54c2ea8437408238f6c181a355af6cb": [
        {
            "description": "Apple QuickTime, " "Quality 827-829 (81%)",
            "subsampling": "211111",
        }
    ],
    "f56a4679494e5af4692381caa63b9062": [
        {"description": "Apple QuickTime, " "Quality 341 (33%)", "subsampling": "11"}
    ],
    "f57e9a5f1d8dea7fd83a1b5840243686": [
        {
            "description": "Apple QuickTime, " "Quality 616-617 (60%)",
            "subsampling": "11",
        }
    ],
    "f60d4afe566a641f0187a42ca6462560": [
        {"description": "Apple QuickTime, " "Quality 281 (27%)", "subsampling": "11"}
    ],
    "f6150beda200179d9744527637e52baa": [
        {"description": "Apple QuickTime, " "Quality 344 (34%)", "subsampling": "11"}
    ],
    "f6308a717437d3653b0751ebf511db0f": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "49 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 49",
            "subsampling": "111111",
        },
    ],
    "f647f0fb4320c61f52e2a79d12bbc8cc": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 4", "subsampling": ""}
    ],
    "f64d88456f97a65fe562eb69e619782a": [
        {"description": "Apple QuickTime, " "Quality 685 (67%)", "subsampling": "11"}
    ],
    "f6c4502144a2e5c82c07994d3cd01665": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 16", "subsampling": ""}
    ],
    "f6d9c8699e54823040b66c4b8e1361aa": [
        {
            "description": "Apple QuickTime, " "Quality 295 (29%)",
            "subsampling": "221111",
        }
    ],
    "f73704219e174961963f0fcd832b09a8": [
        {
            "description": "Apple QuickTime, " "Quality 830-832 (81%)",
            "subsampling": "11",
        }
    ],
    "f73f690cacd5d4e247f59964ad0f43b9": [
        {"description": "Apple QuickTime, " "Quality 460 (45%)", "subsampling": "11"}
    ],
    "f7425d5d0a0207e6dfaa0ee7c35d4ec6": [
        {"description": "Apple QuickTime, " "Quality 349 (34%)", "subsampling": "11"}
    ],
    "f7493b01895b7880c651841c73678d33": [
        {"description": "Apple QuickTime, " "Quality 547 (53%)", "subsampling": "11"}
    ],
    "f74b3853185743c111ccb13e6febdc21": [
        {"description": "Pentax Optio T20 (B)", "subsampling": "211111"}
    ],
    "f7a5ea485a254cba0d39cdeaf89ad344": [
        {
            "description": "Apple QuickTime, " "Quality 799 (78%)",
            "subsampling": "211111",
        }
    ],
    "f7adac1fb54bb1fc566b66822122a9c6": [
        {
            "description": "Apple QuickTime, " "Quality 401 (39%)",
            "subsampling": "221111",
        }
    ],
    "f7cba1affebd362a322abd45ce580e56": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "70",
            "subsampling": "",
        }
    ],
    "f7d70cfab7ff888c97078d277fa01307": [
        {"description": "Apple QuickTime, " "Quality 442 (43%)", "subsampling": "11"}
    ],
    "f7d803e16f0c66df7d46747715b1ae24": [
        {
            "description": "Apple QuickTime, " "Quality 1003 (98%)",
            "subsampling": "211111",
        }
    ],
    "f7e5656e1f2cf036e9a57a6c02373398": [
        {
            "description": "Apple QuickTime, " "Quality 538 (53%)",
            "subsampling": "221111",
        }
    ],
    "f83c5bc303fa1f74265863c2c6844edf": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "0 or 1",
            "subsampling": "",
        }
    ],
    "f83d978290d0699054eabb0a7811c7a4": [
        {"description": "Pentax K10D (BA)", "subsampling": "211111"},
        {"description": "Pentax K10D (BB)", "subsampling": "211111"},
    ],
    "f841cbd6a77d64924ab19845219f3399": [
        {
            "description": "Apple QuickTime, " "Quality 216-217 (21%)",
            "subsampling": "11",
        }
    ],
    "f8948967aeda9fb6ca1637a082ed04db": [
        {"description": "Apple QuickTime, " "Quality 321 (31%)", "subsampling": "11"}
    ],
    "f8df76525f7f97d2e89173989e6786af": [
        {
            "description": "Apple QuickTime, " "Quality 802-804 " "(78-79%)",
            "subsampling": "211111",
        }
    ],
    "f8e99ed03828752f16c51bb8c9887e9e": [
        {"description": "Apple QuickTime, " "Quality 503 (49%)", "subsampling": "11"}
    ],
    "f8ede291b1272576d1580e333d30103e": [
        {
            "description": "Adobe Lightroom, " "Quality 31% - 38%",
            "subsampling": "221111",
        }
    ],
    "f90135fcff0e1720dda86e9ad718c0c0": [
        {"description": "Pentax K10D (AQ)", "subsampling": "211111"}
    ],
    "f9176b3ef0b4038c6c52b30ba033eb7f": [
        {"description": "Apple QuickTime, " "Quality 814 (79%)", "subsampling": "11"}
    ],
    "f91cfb708c99c2fef0f7148976514f44": [
        {
            "description": "Apple QuickTime, " "Quality 1001-1002 (98%)",
            "subsampling": "11",
        }
    ],
    "f94618c1a011209cb3b060887c7e244e": [
        {"description": "Apple QuickTime, " "Quality 493 (48%)", "subsampling": "11"}
    ],
    "f97cd4c7b1125556dc3eb57fc494e6b5": [
        {
            "description": "Apple QuickTime, " "Quality 1007-1009 " "(98-99%)",
            "subsampling": "211111",
        }
    ],
    "f984581f90913e44f3898fffd8fce8b0": [
        {
            "description": "Apple QuickTime, " "Quality 563 (55%)",
            "subsampling": "221111",
        }
    ],
    "f98a4286abf1cbe8bf46fba1e78cec61": [
        {
            "description": "Apple QuickTime, " "Quality 371 (36%)",
            "subsampling": "221111",
        }
    ],
    "f9988c61ae580fcfc8bf929134b07c2e": [
        {"description": "Apple QuickTime, " "Quality 333 (33%)", "subsampling": "11"}
    ],
    "f9a93cb70da7bbe87e35cd9980a5fd47": [
        {"description": "Pentax K10D (AK)", "subsampling": "211111"}
    ],
    "f9b83ba21b86a3d4ddb507e3edce490c": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 68",
            "subsampling": "111111",
        }
    ],
    "f9bff3eeb4e94fb9ab4820184b0b6058": [
        {
            "description": "Apple QuickTime, " "Quality 263 (26%)",
            "subsampling": "221111",
        }
    ],
    "f9ef906cd67c9f9b62514a6ac1f8bd3f": [
        {"description": "Apple QuickTime, " "Quality 255 (25%)", "subsampling": "11"}
    ],
    "fa11118bb9f90b1464e34c785d0da357": [
        {
            "description": "Apple QuickTime, " "Quality 239-240 (23%)",
            "subsampling": "11",
        }
    ],
    "fa3d7753be7b329ab9961657cbc65386": [
        {"description": "Pentax K10D (AR)", "subsampling": "211111"}
    ],
    "fa620c67ab09a4c0d1c5b8e65ade361e": [
        {
            "description": "ACD Systems Digital " "Imaging, Quality 30 or " "31",
            "subsampling": "",
        }
    ],
    "fa6f80883480ab3ddea8ee2f6796a14b": [
        {
            "description": "Apple QuickTime, " "Quality 959-961 (94%)",
            "subsampling": "11",
        }
    ],
    "fa8720d025f2a164542b6a8e31112991": [
        {
            "description": "PENTAX PHOTO " "Laboratory, Medium " "quality",
            "subsampling": "211111",
        },
        {"description": "Pentax K10D (AS)", "subsampling": "211111"},
        {"description": "Pentax K10D/K100D", "subsampling": "211111"},
    ],
    "fa987940fdedbe883cc0e9fcc907f89e": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "8 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 8",
            "subsampling": "111111",
        },
    ],
    "fa99ff1ecc29c5caa95fa62189fca670": [
        {
            "description": "Apple QuickTime, " "Quality 881-886 " "(86-87%)",
            "subsampling": "11",
        }
    ],
    "fb3c0cc15ad21b6c19576dd8d7d29a0e": [
        {
            "description": "Apple QuickTime, " "Quality 251 (25%)",
            "subsampling": "221111",
        }
    ],
    "fb549f21b7ad3b556bc91165b3067a77": [
        {"description": "Apple QuickTime, " "Quality 275 (27%)", "subsampling": "11"}
    ],
    "fb64b35fe4021c34f16cf5bb1e59c0e8": [
        {"description": "Apple QuickTime, " "Quality 805 (79%)", "subsampling": "11"}
    ],
    "fb91d6a8a1b72388d68130f551698865": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 97",
            "subsampling": "111111",
        }
    ],
    "fbe0f5b89f266ff382f2b14c70a83097": [
        {
            "description": "Apple QuickTime, " "Quality 524 (51%)",
            "subsampling": "221111",
        }
    ],
    "fbf3d8d87f68077aa95e5e40047c1607": [
        {
            "description": "Apple QuickTime, " "Quality 260-261 (25%)",
            "subsampling": "11",
        }
    ],
    "fc0d8f17be060220464fe7bc0a2d754e": [
        {
            "description": "Apple QuickTime, " "Quality 581 (57%)",
            "subsampling": "221111",
        }
    ],
    "fc28ca358af7cd55dc78853e4288f26d": [
        {"description": "Apple QuickTime, " "Quality 304 (30%)", "subsampling": "11"}
    ],
    "fc41ab8251718977bc6676f502f457e0": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "51 (Grayscale)",
            "subsampling": "11",
        },
        {
            "description": "StereoPhoto Maker, No "
            "compression ghosting, "
            "Quality 51",
            "subsampling": "111111",
        },
    ],
    "fc5812ad9a4cd0122eb1c63f0ac3b5a3": [
        {"description": "Corel Paint Shop Pro " "PHOTO, Quality 81", "subsampling": ""}
    ],
    "fc6dfb9669566b249cb03228aeb020c3": [
        {"description": "Apple QuickTime, " "Quality 589 (58%)", "subsampling": "11"}
    ],
    "fc8d384969030e7bc0255d34a7a5c0b0": [
        {
            "description": "Apple QuickTime, " "Quality 906 (88%)",
            "subsampling": "211111",
        }
    ],
    "fc923f2d38e0e549134e1ec86f58149a": [
        {
            "description": "ACD Systems Digital " "Imaging, Quality 60 or " "61",
            "subsampling": "",
        }
    ],
    "fc9d0f82571701e8b4cf764125ac0d2e": [
        {
            "description": "Apple QuickTime, " "Quality 352 (34%)",
            "subsampling": "221111",
        }
    ],
    "fc9f2bd278075ea89d482e1f9e66738f": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "64",
            "subsampling": "",
        }
    ],
    "fca91c73d4275748587f97b472b59280": [
        {
            "description": "Apple QuickTime, " "Quality 195-196 (19%)",
            "subsampling": "221111",
        }
    ],
    "fcb49e821b83f8436d450b03f1b1f182": [
        {
            "description": "Apple QuickTime, " "Quality 336 (33%)",
            "subsampling": "221111",
        }
    ],
    "fccd63ce166e198065eaae05c8d78407": [
        {"description": "Adobe Photoshop, " "Quality 5", "subsampling": "11"}
    ],
    "fcd8c97cf6004230444ce21dab8a167f": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "58",
            "subsampling": "",
        }
    ],
    "fcef35c97674aeb26c67e539b726057f": [
        {"description": "Pentax Optio S, Best " "(A)", "subsampling": "221111"}
    ],
    "fd2f7a6518c12848a9ecdb1c3beb1fa8": [
        {"description": "Apple QuickTime, " "Quality 415 (41%)", "subsampling": "11"}
    ],
    "fd3167b1cdcfa1bdd37a4841d37b1624": [
        {
            "description": "Apple QuickTime, " "Quality 716-717 (70%)",
            "subsampling": "11",
        }
    ],
    "fd3eed19f6667ab0bedfa3263390ce25": [
        {
            "description": "ACD Systems Digital " "Imaging, Quality 5 or 6",
            "subsampling": "",
        }
    ],
    "fd732b0493e7ff16da4bde7faa88e22d": [
        {"description": "Apple QuickTime, " "Quality 455 (44%)", "subsampling": "11"}
    ],
    "fdbe851f6e559bc17ce3610b91e7fead": [
        {"description": "Apple QuickTime, " "Quality 727 (71%)", "subsampling": "11"}
    ],
    "fde14219617069bbf6b26dcb42036de7": [
        {"description": "Apple QuickTime, " "Quality 541 (53%)", "subsampling": "11"}
    ],
    "fdf6b04a2d8ac06d3fe64d1dceba4cd9": [
        {"description": "Apple QuickTime, " "Quality 725 (71%)", "subsampling": "11"}
    ],
    "fe44d8625d6242f4b5deb82be8ccaacf": [
        {"description": "Apple QuickTime, " "Quality 595 (58%)", "subsampling": "11"}
    ],
    "fe85b802c5779dcf45ea4bb7749ee886": [
        {
            "description": "Canon Digital Photo " "Professional, Quality 7",
            "subsampling": "211111",
        }
    ],
    "fefd00ec4610895e4294de690f5977e9": [
        {
            "description": "Adobe Photoshop, Save " "for web, Quality 37",
            "subsampling": "221111",
        }
    ],
    "ff0758d87a0cbdb323fb93bf9ed1fdff": [
        {
            "description": "Apple QuickTime, " "Quality 307 (30%)",
            "subsampling": "221111",
        }
    ],
    "ff084566430a3ed4733cd59aec26a55d": [
        {
            "description": "Apple QuickTime, " "Quality 747 (73%)",
            "subsampling": "221111",
        }
    ],
    "ff0aa07a220cd8973a4b86f3ecd4325b": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "92",
            "subsampling": "",
        }
    ],
    "ff6a158f803e42bfbf9f702c016b84b3": [
        {"description": "Pentax K10D (AL)", "subsampling": "211111"}
    ],
    "ff6d4a4a60a1c5e032e7fb7d9c91f817": [
        {"description": "Pentax K10D (AM)", "subsampling": "211111"}
    ],
    "ff765e75c06c9db34f66ae7ee0202d05": [
        {"description": "Apple QuickTime, " "Quality 974 (95%)", "subsampling": "11"}
    ],
    "ff7a6007b6aab26f3c72c715ce487d72": [
        {"description": "Apple QuickTime, " "Quality 755 (74%)", "subsampling": "11"}
    ],
    "ff82adb92189413246aee9a992eb2013": [
        {"description": "Apple QuickTime, " "Quality 476 (46%)", "subsampling": "11"}
    ],
    "ffa7874d293c62ecc55c098b8f305ae1": [
        {
            "description": "Apple QuickTime, " "Quality 604 (59%)",
            "subsampling": "221111",
        }
    ],
    "ffadac945c3420537e21e67ab3a843d6": [
        {
            "description": "Apple QuickTime, " "Quality 873-875 (85%)",
            "subsampling": "211111",
        }
    ],
    "ffb8ea8efdb22c5c8256cc4e4008f11c": [
        {"description": "Apple QuickTime, " "Quality 310 (30%)", "subsampling": "11"}
    ],
    "ffc0192eb5a182370a641cffe9b1d71f": [
        {"description": "Apple QuickTime, " "Quality 567 (55%)", "subsampling": "11"}
    ],
    "ffcd5eab8daeced571d59d4cdcc002c4": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "50",
            "subsampling": "",
        }
    ],
    "ffd6e30af6d99997d38ec3e303687e25": [
        {
            "description": "Independent JPEG Group "
            "library (used by many "
            "applications), Quality "
            "37",
            "subsampling": "",
        }
    ],
    "ffe6bb565b2c9008ab917c57ba94cd67": [
        {"description": "ACD Systems Digital " "Imaging, Quality 99", "subsampling": ""}
    ],
}
