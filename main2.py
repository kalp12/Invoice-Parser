import os
import base64
import json
from mistralai import Mistral
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("MISTRAL_API_KEY")

if not API_KEY:
    raise ValueError("API Key not found! Set MISTRAL_API_KEY in environment variables.")

client = Mistral(api_key=API_KEY)

def process_pdf(pdf_path):
    """Processes a PDF file using Mistral OCR API."""
    with open(pdf_path, "rb") as f:
        file_bytes = f.read()
        encoded_pdf = base64.b64encode(file_bytes).decode("utf-8")

    document = {
        "type": "document_url",  # Use the correct type!
        "document_url": f"data:application/pdf;base64,{encoded_pdf}"
    }
    # file_bytes = pdf_path.read()
    # encoded_pdf = base64.b64encode(file_bytes).decode("utf-8")
    # document = {
    #     "type": "document_base64",
    #     "document_base64": encoded_pdf
    # }
    # preview_src = f"data:application/pdf;base64,{encoded_pdf}"

    # Send OCR request
    print("Processing OCR request...")
    ocr_response = client.ocr.process(
        model="mistral-ocr-latest",
        document=document,
        include_image_base64=True  # No need for image data
    )

    # Extract OCR results
    result_text = "\n\n".join(page.markdown for page in ocr_response.pages) if hasattr(ocr_response, "pages") else "No result found."

    # Save OCR result to file
    output_file = pdf_path.replace(".pdf", "2_ocr_result.txt")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(result_text)
    
    print(f"OCR processing complete! Results saved to {output_file}")
    return result_text

# Example usage
pdf_file = "testing.pdf"  # Change this to your PDF file path
ocr_text = process_pdf(pdf_file)

# Print OCR result (optional)
print("\nExtracted Text:\n", ocr_text)
