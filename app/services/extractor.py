from pypdf import PdfReader
from io import BytesIO

def extract_text_from_pdf(file_content: bytes)->str:
    stream=BytesIO(file_content)
    reader=PdfReader(stream)
    text=""
    for page in reader.pages:
        text+=page.extract_text()+"\n"
    return text.strip()