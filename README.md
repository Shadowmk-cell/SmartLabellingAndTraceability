# Design and implement a smart, automated system for product labeling and traceability

A Streamlit-based application for smart product labeling with integrated QR code generation, machine testing simulation, traceability reporting, and real-time validation. Designed for use in manufacturing, quality control, and logistics environments.

**Features**

Admin and Sensor modes for product entry
Simulated machine testing for TM1, TM2, and TM3 with pass/fail based on processing time
QR code generation for each product with encoded metadata
Centralized logging in Excel (inspection_log.xlsx)
PDF traceability report generation per device
OCR-based QR label validation from uploaded images
Visual analytics showing test machine failure statistics

**Technologies Used**
Python 3.x
Streamlit
openpyxl
qrcode
pillow
pyzbar
fpdf
pandas
plotly


**Folder Structure**

smart_labeling_project/
├── app.py
├── label_generator.py
├── pdf_export.py
├── utils.py
├── ocr_validator.py
├── requirements.txt
├── README.md
├── qr_codes                  # Stores generated QR images (excluded in .gitignore)
└── inspection_log.xlsx        # Excel log (auto-generated)


**Setup Instructions**
Clone the repository
git clone https://github.com/yourusername/smart-labeling-system.git
cd smart-labeling-system

Create and activate a virtual environment
python -m venv venv
source venv/bin/activate 

**Install dependencies**
pip install -r requirements.txt

**Run the application**
streamlit run apps.py

**Admin Credentials**
Some features require admin access:
Password: admin123


**Usage**
Use Sensor Mode for automated product simulation
Use Admin Mode for manual issue logging with custom test outcomes
Search by Device ID to view and export PDF traceability reports
Upload a scanned QR label to verify its authenticity using OCR
View failure statistics of test machines in the analytics section

**License**
This project is intended for educational and non-commercial use only.

