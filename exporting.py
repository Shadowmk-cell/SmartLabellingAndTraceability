# exporting the pdf

from fpdf import FPDF
from datetime import datetime
import os

def safe_str(value):
    return str(value) if value is not None else "N/A"

def create_pdf(data, qr_path, output_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Title
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "Device Traceability Report", ln=True, align='C')
    pdf.ln(10)

    # Device Info
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, f"Device Name: {safe_str(data.get('Device ID'))}", ln=True)
    pdf.cell(0, 10, f"Batch ID: {safe_str(data.get('Batch ID'))}", ln=True)
    pdf.ln(5)

    # Issues
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "Issue Report:", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, f"TM1: {safe_str(data.get('TM1 Issue'))}", ln=True)
    pdf.cell(0, 10, f"TM2: {safe_str(data.get('TM2 Issue'))}", ln=True)
    pdf.cell(0, 10, f"TM3: {safe_str(data.get('TM3 Issue'))}", ln=True)
    pdf.ln(5)

    # Admin Comment
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "Admin Comment:", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, safe_str(data.get("Admin Comment")))
    pdf.ln(10)

    # Add QR image if exists
    if qr_path and os.path.exists(qr_path):
        pdf.image(qr_path, x=80, w=50)
        pdf.ln(10)

    # Footer
    pdf.set_font("Arial", size=10)
    pdf.cell(0, 10, f"Report generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True)

    # Save
    pdf.output(output_path)
