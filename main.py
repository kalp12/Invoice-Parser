from mistralai import Mistral
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ["MISTRAL_API_KEY"]
print(api_key)

client = Mistral(api_key=api_key)

uploaded_pdf = client.files.upload(
    file={
        "file_name": "testing.pdf",
        "content": open("testing.pdf", "rb"),
    },
    purpose="ocr"
)  

print(uploaded_pdf)