# 📄 Invoice-Parser

This project uses the **Mistral OCR API** to extract structured text and images from PDF invoices (or any PDF document).  

It processes a PDF file, sends it to Mistral’s OCR model, and saves:

- Extracted text (as Markdown)
- Extracted images/figures
- A complete combined Markdown file

---

## 🚀 Features

- Upload PDF to Mistral OCR API
- Extract text as structured Markdown
- Extract and save embedded images
- Automatically replace image placeholders in Markdown
- Save full document output locally

---

## 🧠 How It Works

1. Uploads PDF to Mistral API
2. Gets a signed URL
3. Processes document using `mistral-ocr-latest`
4. Extracts:
   - Page-by-page Markdown
   - Embedded images (Base64 → PNG)
5. Saves:
   - `images/` folder (all extracted images)
   - `complete.md` (full document Markdown)

---

## ⚙️ Requirements

- Python 3.9+
- Mistral AI Python SDK
- python-dotenv

Install dependencies:

```bash
pip install requirements.txt
```

## 🔑 Setup

Create a .env file:

MISTRAL_API_KEY=your_api_key_here


Place your PDF file in the project directory (default name: index.pdf)

## ▶️ Run the Script
python pdf_ocr.py


After running:

OCR: ocr_results_3_index


You will find:

complete.md → Full extracted document

images/ → All extracted figures and embedded visuals

## 📝 Core Functions
process_pdf(pdf_path, api_key)

## Handles:

Uploading file

Calling OCR API

Saving results

save_ocr_results(ocr_response, output_dir)

Decodes Base64 images

Saves images locally

Rewrites Markdown image references

Combines all pages into a single file

## 📊 Use Cases

Invoice parsing

Receipt digitization

Document processing

Extracting figures from research PDFs

Converting scanned PDFs to Markdown

## 🔮 Future Improvements

Add JSON structured invoice extraction

Add automatic field detection (Total, VAT, Date, etc.)

Add web interface

Add batch PDF processing

Deploy as API service


