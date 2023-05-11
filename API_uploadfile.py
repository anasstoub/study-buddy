# from fastapi import FastAPI, File, UploadFile
# from normalisation import extract_text_from_pdf, split_text_into_sentences_and_words, remove_stop_words

# app = FastAPI()

# @app.post("/pdf-text/")
# async def extract_pdf_text(pdf_file: UploadFile = File(..., media_type="application/pdf")):
#     # Get the file name and content
#     file_name = pdf_file.filename
#     file_content = await pdf_file.read()
#     # Save the PDF file
#     with open(file_name, 'wb') as f:
#         f.write(file_content)
#     # Extract the text from the PDF file
#     text = extract_text_from_pdf(file_name)
#     # split the text into sentences and words
#     sentences = split_text_into_sentences_and_words(text)
#     # Remove stop words from each sentence
#     filtered_sentences = remove_stop_words(sentences)
#     # Return the text
#     return {'filtred_Sentences': filtered_sentences}
# -----------------------------------------------------------------------------------------------------------------
from fastapi import FastAPI, File, UploadFile
from normalisation import extract_text_from_pdf, split_text_into_sentences
from sentence_transformers import SentenceTransformer, util
app = FastAPI()
text = ""
sentences = []
model = SentenceTransformer('all-MiniLM-L6-v2')
import numpy as np
from typing import List

@app.post("/pdf-text/")
async def extract_pdf_text(pdf_file: UploadFile = File(..., media_type="application/pdf")):
    global text, sentences
    # Get the file name and content
    file_name = pdf_file.filename
    file_content = await pdf_file.read()
    # Save the PDF file
    with open(file_name, 'wb') as f:
        f.write(file_content)
    # Extract the text from the PDF file
    text = extract_text_from_pdf(file_name)
    # split the text into sentences and words
    sentences = split_text_into_sentences(text)
    # Return the text
    return(f"Sentences: {sentences}")

    # return {'sentences': sentences}

@app.post("/find-similar-sentences/")
async def find_similar_sentences(question: str): #, sentences: List[str]
    question_embedding = model.encode([question])[0]
    sentence_embeddings = model.encode(sentences)
    similarities = util.pytorch_cos_sim(question_embedding, sentence_embeddings)
    similarities = similarities.tolist()
    similarities = similarities[0]
    similarities = np.array(similarities)
    top_indices = similarities.argsort()[-5:][::-1]
    # similar_sentences contains the top_indices and the similarity score
    similar_sentences = []
    for i in top_indices:
        similar_sentences.append({'sentence': sentences[i], 'similarity_score': similarities[i]})
    return {'similar_sentences': similar_sentences}

