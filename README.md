# Warehouse Management System (WMS) - MVP

## Overview
This project is a beginner-friendly Minimum Viable Product (MVP) for a Warehouse Management System designed to streamline sales data cleaning, SKU/MSKU mapping, and basic analytics. The solution also demonstrates AI-assisted coding and a simple GUI and web dashboard.

## Features
- SKU to MSKU Mapping (with combo product support)
- GUI-based file loading and mapping
- Data Cleaning and Validation
- Streamlit dashboard with sales summaries
- AI Layer (Text-to-SQL prototype support)

## Tech Stack
- Python (pandas, tkinter, streamlit)
- Baserow (Relational DB)
- Streamlit (Dashboard UI)
- SQLGlot / OpenAI (Text-to-SQL simulation)

## Folder Structure
```
.
├── sku_mapper.py         # GUI tool for SKU -> MSKU mapping
├── preprocess.py         # Data cleaning script
├── app.py                # Streamlit frontend for sales metrics
├── README.md             # Project documentation
└── WMS_MVP_Assignment.pdf  # Full project report (compiled)
```

## Setup Instructions

1. **Install Dependencies**
```bash
pip install pandas streamlit
```

2. **Run SKU Mapper GUI**
```bash
python sku_mapper.py
```

3. **Clean Sales Data**
Edit `preprocess.py` if needed, then run:
```bash
python preprocess.py
```

4. **Launch Streamlit Dashboard**
```bash
streamlit run app.py
```

## Sample Data Format

### SKU Mapping CSV
```
SKU,MSKU
GLD,Golden Apple
ORG,Orange
```

### Sales Data CSV
```
SKU,Quantity,Price
GLD,10,5.00
ORG,15,4.50
```

## AI Tools Used
- Code suggestions and automation powered by ChatGPT (OpenAI)
- SQLGlot for converting natural language queries to SQL (can be plugged into Baserow or any RDBMS)

## Loom Video
> [Add your Loom video link here demonstrating app features]

## Submission
- Submit this repo or a ZIP file including all files.
- Email your submission to `vaibhav@cste.international` with the subject: `WMS Assignment - [Your Name]`.
- Ensure links (Loom, database, etc.) are publicly accessible.