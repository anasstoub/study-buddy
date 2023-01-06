from fastapi import FastAPI, File, UploadFile
from normalisation import extract_text_from_pdf, split_text_into_sentences_and_words, remove_stop_words



app = FastAPI()

@app.post("/upload-file/")
async def upload_pdf(file: UploadFile = File(..., media_type="application/pdf")):
    text = extract_text_from_pdf(file)
    sentences = split_text_into_sentences_and_words(text)
    sentences = remove_stop_words(sentences)
    return {"sentences": sentences}