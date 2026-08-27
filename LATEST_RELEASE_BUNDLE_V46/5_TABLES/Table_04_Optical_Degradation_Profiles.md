# Table 4: Optical Quality Degradation Profiles

| Profile Name | Target Simulation | Applied Image Transformations | Degradation Severity |
| :--- | :--- | :--- | :--- |
| clean | Pristine vector render | Direct 300 DPI PDF-to-image rasterization; uncompressed | None (0.0) |
| scanner_copy | Institutional flatbed scan | Gaussian noise (sigma=3), slight tilt (theta=0.5 deg), brightness shift (+10%) | Mild (1.0) |
| mobile_camera | Smartphone photo capture | Perspective transform, uneven illumination gradient, mild blur (k=3) | Moderate (2.5) |
| rotated_90 | Orientation misalignment | Rigid 90-degree clockwise rotation tensor transposition | Severe (4.0) |