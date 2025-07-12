# Validation using OCR model

from pyzbar.pyzbar import decode
from PIL import Image
import time
import os
from generating import initialize_product

def QR_Image_Validation(image_path):
    initialize_product()
    start_time = time.time()

    try:
        img = Image.open(image_path)
        decoded = decode(img)

        if not decoded:
            raise ValueError("No QR code found in the image.")

        qr_data = decoded[0].data.decode('utf-8')
        lines = qr_data.split('\n')

        device_id = "N/A"
        batch_id = "N/A"

        for line in lines:
            if "device" in line.lower():
                device_id = line.split(":")[-1].strip()
            elif "batch" in line.lower():
                batch_id = line.split(":")[-1].strip()

        status = "REJECT"
        issue = "Device ID and Batch ID not found in QR data"

        if device_id != "N/A" and batch_id != "N/A":
            qr_path = f"qr_codes/{device_id}.png"
            if os.path.exists(qr_path):
                status = "PASS"
                issue = "No issue"
            else:
                issue = "Mismatch or missing QR code image"

        return {
            "device_id": device_id,
            "batch_id": batch_id,
            "status": status,
            "issue": issue,
            "time": round(time.time() - start_time, 2),
            "ocr_text": qr_data
        }

    except Exception as e:
        return {
            "device_id": "N/A",
            "batch_id": "N/A",
            "status": "REJECT",
            "issue": f"QR decode failed: {str(e)}",
            "time": round(time.time() - start_time, 2),
            "ocr_text": "QR decode failed"
        }
