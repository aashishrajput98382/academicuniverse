# 100% Real Live Multi-Modal Vision Benchmark Report (45 Specimens)

Direct neural inference via **MiniCPM-V 7.6B** on physical files from `D:/AU_DIC_Benchmark_60k`:

- **Total Physical Specimens Tested:** 45
- **Total Benchmark Time:** 2917.9 seconds
- **Mean Latency per Document:** 64.3s
- **Overall Student Name Recognition:** 97.8%
- **Overall University Recognition:** 93.3%

|   Sample_ID | Modality   | Quality_Profile   | File_Name                       |   Latency_Sec | GT_Student_Name   | Name_Match   | GT_University                         | University_Match   |
|------------:|:-----------|:------------------|:--------------------------------|--------------:|:------------------|:-------------|:--------------------------------------|:-------------------|
|           1 | PDF        | clean             | DOC-0010905E.pdf                |       5.81806 | Lakshay Sinha     | True         | Indira Gandhi College of Engineering  | True               |
|           2 | PDF        | clean             | DOC-001A07AB.pdf                |       7.191   | Prashant Kulkarni | True         | Vivekananda Technical University      | True               |
|           3 | PDF        | clean             | DOC-001F58BA.pdf                |      68.9795  | Harsh Patel       | True         | Sri Ramanujan Institute of Technology | True               |
|           4 | PDF        | clean             | DOC-0024DCD6.pdf                |      66.1229  | Siddharth Nair    | True         | Indira Gandhi College of Engineering  | True               |
|           5 | PDF        | clean             | DOC-0031A4A3.pdf                |      67.2589  | Kavya Sharma      | False        | Indira Gandhi College of Engineering  | True               |
|           6 | PNG        | clean             | DOC-0010905E_clean.png          |      46.4384  | Lakshay Sinha     | True         | Indira Gandhi College of Engineering  | True               |
|           7 | PNG        | clean             | DOC-001A07AB_clean.png          |      67.4032  | Prashant Kulkarni | True         | Vivekananda Technical University      | True               |
|           8 | PNG        | clean             | DOC-001F58BA_clean.png          |      66.6436  | Harsh Patel       | True         | Sri Ramanujan Institute of Technology | True               |
|           9 | PNG        | clean             | DOC-0024DCD6_clean.png          |      67.1469  | Siddharth Nair    | True         | Indira Gandhi College of Engineering  | True               |
|          10 | PNG        | clean             | DOC-0031A4A3_clean.png          |      65.8955  | Kavya Sharma      | True         | Indira Gandhi College of Engineering  | True               |
|          11 | PNG        | scanner_copy      | DOC-0010905E_scanner_copy.png   |      67.1446  | Lakshay Sinha     | True         | Indira Gandhi College of Engineering  | True               |
|          12 | PNG        | scanner_copy      | DOC-001A07AB_scanner_copy.png   |      69.8785  | Prashant Kulkarni | True         | Vivekananda Technical University      | True               |
|          13 | PNG        | scanner_copy      | DOC-001F58BA_scanner_copy.png   |      65.7747  | Harsh Patel       | True         | Sri Ramanujan Institute of Technology | True               |
|          14 | PNG        | scanner_copy      | DOC-0024DCD6_scanner_copy.png   |      66.056   | Siddharth Nair    | True         | Indira Gandhi College of Engineering  | True               |
|          15 | PNG        | scanner_copy      | DOC-0031A4A3_scanner_copy.png   |      67.5169  | Kavya Sharma      | True         | Indira Gandhi College of Engineering  | True               |
|          16 | PNG        | mobile_camera     | DOC-0010905E_mobile_camera.png  |      65.3525  | Lakshay Sinha     | True         | Indira Gandhi College of Engineering  | True               |
|          17 | PNG        | mobile_camera     | DOC-001A07AB_mobile_camera.png  |      66.0715  | Prashant Kulkarni | True         | Vivekananda Technical University      | True               |
|          18 | PNG        | mobile_camera     | DOC-001F58BA_mobile_camera.png  |      67.5549  | Harsh Patel       | True         | Sri Ramanujan Institute of Technology | False              |
|          19 | PNG        | mobile_camera     | DOC-0024DCD6_mobile_camera.png  |      66.1511  | Siddharth Nair    | True         | Indira Gandhi College of Engineering  | True               |
|          20 | PNG        | mobile_camera     | DOC-0031A4A3_mobile_camera.png  |      65.0902  | Kavya Sharma      | True         | Indira Gandhi College of Engineering  | True               |
|          21 | PNG        | rotated_90        | DOC-0010905E_rotated_90.png     |      66.0461  | Lakshay Sinha     | True         | Indira Gandhi College of Engineering  | True               |
|          22 | PNG        | rotated_90        | DOC-001A07AB_rotated_90.png     |      67.3182  | Prashant Kulkarni | True         | Vivekananda Technical University      | True               |
|          23 | PNG        | rotated_90        | DOC-001F58BA_rotated_90.png     |      66.7766  | Harsh Patel       | True         | Sri Ramanujan Institute of Technology | False              |
|          24 | PNG        | rotated_90        | DOC-0024DCD6_rotated_90.png     |      68.2771  | Siddharth Nair    | True         | Indira Gandhi College of Engineering  | True               |
|          25 | PNG        | rotated_90        | DOC-0031A4A3_rotated_90.png     |      78.1839  | Kavya Sharma      | True         | Indira Gandhi College of Engineering  | True               |
|          26 | JPEG       | clean             | DOC-0010905E_clean.jpeg         |      64.9452  | Lakshay Sinha     | True         | Indira Gandhi College of Engineering  | True               |
|          27 | JPEG       | clean             | DOC-001A07AB_clean.jpeg         |      73.5246  | Prashant Kulkarni | True         | Vivekananda Technical University      | True               |
|          28 | JPEG       | clean             | DOC-001F58BA_clean.jpeg         |      72.5686  | Harsh Patel       | True         | Sri Ramanujan Institute of Technology | True               |
|          29 | JPEG       | clean             | DOC-0024DCD6_clean.jpeg         |      68.4556  | Siddharth Nair    | True         | Indira Gandhi College of Engineering  | True               |
|          30 | JPEG       | clean             | DOC-0031A4A3_clean.jpeg         |      70.264   | Kavya Sharma      | True         | Indira Gandhi College of Engineering  | True               |
|          31 | JPEG       | scanner_copy      | DOC-0010905E_scanner_copy.jpeg  |      66.6555  | Lakshay Sinha     | True         | Indira Gandhi College of Engineering  | True               |
|          32 | JPEG       | scanner_copy      | DOC-001A07AB_scanner_copy.jpeg  |      67.214   | Prashant Kulkarni | True         | Vivekananda Technical University      | True               |
|          33 | JPEG       | scanner_copy      | DOC-001F58BA_scanner_copy.jpeg  |      65.9559  | Harsh Patel       | True         | Sri Ramanujan Institute of Technology | True               |
|          34 | JPEG       | scanner_copy      | DOC-0024DCD6_scanner_copy.jpeg  |      72.7684  | Siddharth Nair    | True         | Indira Gandhi College of Engineering  | True               |
|          35 | JPEG       | scanner_copy      | DOC-0031A4A3_scanner_copy.jpeg  |      66.5783  | Kavya Sharma      | True         | Indira Gandhi College of Engineering  | True               |
|          36 | JPEG       | mobile_camera     | DOC-0010905E_mobile_camera.jpeg |      65.546   | Lakshay Sinha     | True         | Indira Gandhi College of Engineering  | True               |
|          37 | JPEG       | mobile_camera     | DOC-001A07AB_mobile_camera.jpeg |      69.0618  | Prashant Kulkarni | True         | Vivekananda Technical University      | True               |
|          38 | JPEG       | mobile_camera     | DOC-001F58BA_mobile_camera.jpeg |      70.2121  | Harsh Patel       | True         | Sri Ramanujan Institute of Technology | True               |
|          39 | JPEG       | mobile_camera     | DOC-0024DCD6_mobile_camera.jpeg |      64.4907  | Siddharth Nair    | True         | Indira Gandhi College of Engineering  | True               |
|          40 | JPEG       | mobile_camera     | DOC-0031A4A3_mobile_camera.jpeg |      68.0522  | Kavya Sharma      | True         | Indira Gandhi College of Engineering  | True               |
|          41 | JPEG       | rotated_90        | DOC-0010905E_rotated_90.jpeg    |      66.7348  | Lakshay Sinha     | True         | Indira Gandhi College of Engineering  | True               |
|          42 | JPEG       | rotated_90        | DOC-001A07AB_rotated_90.jpeg    |      68.8929  | Prashant Kulkarni | True         | Vivekananda Technical University      | True               |
|          43 | JPEG       | rotated_90        | DOC-001F58BA_rotated_90.jpeg    |      69.0987  | Harsh Patel       | True         | Sri Ramanujan Institute of Technology | False              |
|          44 | JPEG       | rotated_90        | DOC-0024DCD6_rotated_90.jpeg    |      60.7364  | Siddharth Nair    | True         | Indira Gandhi College of Engineering  | True               |
|          45 | JPEG       | rotated_90        | DOC-0031A4A3_rotated_90.jpeg    |      61.0651  | Kavya Sharma      | True         | Indira Gandhi College of Engineering  | True               |