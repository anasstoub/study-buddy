import streamlit as st
from PIL import Image
import requests
from urllib.parse import urlencode

url1= "http://localhost:8000/pdf-text/"
url2="http://localhost:8000/find-similar-sentences/"


# Set page configuration
st.set_page_config(page_title="upload pdf")

# Define columns for logo and app name
logo_col, name_col = st.columns([1, 4])

# Add logo to the logo column
with logo_col:
    st.image(Image.open('logo.png'), width=150)

# Add app name to the name column
with name_col:
    st.title("Study Buddy")
    st.caption('A smart tool for students :book:')

upload=st.file_uploader(":green[choose a file]", type='pdf')


def process_pdf_file(pdf_file):
    progress_bar = st.progress(0)
    response= requests.post(url1,files={"pdf_file": pdf_file})
    sentences= response.json()  
    progress_bar.progress(100)
    return sentences 
if upload is not None:
    button_col, success_col = st.columns([1, 4])
    if button_col.button("process file"):
            sentences = process_pdf_file(upload)
            success_col.write(":green[your pfs has been processed successfully]")
            with st.expander("view sentences"):
                st.write({'sentences': sentences})


st.subheader("what is your question ?")
question = st.text_input("Enter some text","", key="input_question", label_visibility="collapsed", placeholder="Put your question here")

def send_question_to_api(question):
    api_endpoint = "http://localhost:8000/find-similar-sentences/"
    query_params = urlencode({'question': question})
    url = f"{api_endpoint}?{query_params}"
    response = requests.post(url)
    return response.json()
if question is not None:
    if upload is not None:
        if st.button('Find Similar Sentences'):
            response = send_question_to_api(question)
            # Handle the response from the API
            st.write(response)
    else:
        st.warning('you should upload a pdf first')


