# OmniCare TinyML

On-device anomaly detection for wearable health monitoring.

## Algorithm
Welford online statistics + EMA + adaptive Z-score + spike/plateau classifier.

## Sensors (7 channels)
HR, SpO2, EDA, SkinTemp, AmbTemp, Motion, PM2.5

## Platform
ESP32-S3, Arduino IDE

## Status
- Python validation on real dataset: complete
- Arduino firmware: compiles (306 KB, 23% flash)
- Live sensor testing: pending hardware

## File
- `omnicare_tinyml_7ch.ino` — main firmware
