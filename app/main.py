from fastapi import FastAPI
from fastapi import File 
from fastapi import UploadFile,Depends
from sqlalchemy.orm import Session
from app.db import models,database
from app.services.extractor import extract_text_from_pdf 

app = FastAPI(title="Intelligent Document Processing System")
models.Base.metadata.create_all(bind=database.engine)

def get_db():
    db=database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"message": "Welcome to the Document Processing API"}

@app.post("/upload")
async def upload_file(file:UploadFile = File(...)):
    
    db=database.SessionLocal()

    file_content = await file.read()
    text = extract_text_from_pdf(file_content)

    new_doc=models.Document(filename=file.filename,content=text)

    db.add(new_doc)
    db.commit()
    db.refresh(new_doc)


    return {"id":new_doc.id,"filename":new_doc.filename,preview:new_doc.content[:100]+"..." if len(text)>100 else text}


