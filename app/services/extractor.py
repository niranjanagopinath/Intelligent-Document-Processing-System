from pypdf import PdfReader
from io import BytesIO
import pytesseract 
import pdf2image

def extract_text_from_pdf(file_content: bytes)->str:
    stream=BytesIO(file_content)
    reader=PdfReader(stream)
    text=""
    for page in reader.pages:
        text+=page.extract_text()+"\n"
    return text.strip()

    if text=="":
        images=pdf2image.convert_from_bytes(file_content)
        for image in images:
            text+=pytesseract.image_to_string(image,lang='eng')
    return text.strip()


