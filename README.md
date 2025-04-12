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
- SQLGlot for converting natural language queries to SQL

## Loom Video
> [Can't add my Loom video because of technical issues but demonstrating app features (which is the audio part)]
This is my MVP for the Warehouse Management System assignment. I’ve built this using Python, Pandas, Tkinter for GUI, and Streamlit for a web dashboard. Let me walk you through it.
>
Part 1: SKU Mapping GUI
python sku_mapper.py
In the GUI:
Upload a sample mapping CSV (SKU → MSKU)
Upload a sample sales CSV
Save the mapped output
This is a Tkinter-based GUI for mapping SKUs to Master SKUs, even across different formats.
>
Part 2: Data Cleaning
Open preprocess.py
Showing the input CSV in Notepad/Excel
Showing the cleaned output CSV
Here I’m cleaning sales data using Pandas, adding MSKUs, and filtering invalid rows
>
Part 3: 
Upload the cleaned CSV
Showing the bar chart of Quantity by MSKU
This dashboard gives a quick visual of sales quantities per MSKU using Streamlit.

Everything explained in Readme

