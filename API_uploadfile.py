from fastapi import FastAPI, File, UploadFile
from normalisation import extract_text_from_pdf, split_text_into_sentences_and_words, remove_stop_words



app = FastAPI()

@app.post("/pdf-text/")
async def extract_pdf_text(pdf_file: UploadFile = File(..., media_type="application/pdf")):
    # Get the file name and content
    file_name = pdf_file.filename
    file_content = await pdf_file.read()
    # Save the PDF file
    with open(file_name, 'wb') as f:
        f.write(file_content)
    # Extract the text from the PDF file
    text = extract_text_from_pdf(file_name)
    # split the text into sentences and words
    sentences = split_text_into_sentences_and_words(text)
    # Remove stop words from each sentence
    filtered_sentences = remove_stop_words(sentences)
    # Return the text
    return {'filtred_Sentences': filtered_sentences}


