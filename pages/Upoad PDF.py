import streamlit as st
from PIL import Image
import requests
from urllib.parse import urlencode
import ast
url1 = "http://localhost:8000/pdf-text/"
url2 = "http://localhost:8000/find-similar-sentences/"

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

upload = st.file_uploader(":green[Choose a file]", type='pdf')
pdf_processed = st.session_state.get('pdf_processed', False)
question_entered = False
sentences = None
sentences = st.session_state.get('sentences', [])

def process_pdf_file(pdf_file):
    progress_bar = st.progress(0)
    response = requests.post(url1, files={"pdf_file": pdf_file})
    sentences = response.json()
    progress_bar.progress(100)
    return sentences

def send_question_to_api(question):
    api_endpoint = "http://localhost:8000/find-similar-sentences/"
    query_params = urlencode({'question': question})
    url = f"{api_endpoint}?{query_params}"
    response = requests.post(url)
    return response.json()

if upload is None:
    st.warning("Please upload a PDF file")
    pdf_processed = False
    question_entered = False
    st.session_state['pdf_processed'] = pdf_processed
    sentences = None  # Clear sentences when upload is None
    st.session_state['sentences'] = sentences

elif st.button("Process File"):
    sentences = process_pdf_file(upload)
    pdf_processed = True
    st.session_state['pdf_processed'] = pdf_processed
    st.session_state['sentences'] = sentences
    st.success(":green[Your PDF has been processed successfully]")

st.subheader("Sentences from PDF:")
with st.expander("View Sentences"):
    if sentences is not None:
        sentences_dict = {'sentences': sentences}
        sentences_list_str = sentences_dict['sentences']
    
        # Find the index of the first occurrence of '[' character
        index_start = sentences_list_str.index('[')
        
        # Remove the leading text and parse the string as a list
        sentences_list = ast.literal_eval(sentences_list_str[index_start:])
        
        num_sentences = st.number_input("Number of Sentences", min_value=1, max_value=len(sentences_list), value=5)
        
        # Display the selected number of sentences
        for index, sentence in enumerate(sentences_list[:num_sentences]):
            st.write(f"Sentence {index + 1}: {sentence}")



if pdf_processed:
    st.subheader("What is your question?")
    question = st.text_input("Enter your question", key="input_question", placeholder="Put your question here")
    find_similar_sentences = st.button('Find Similar Sentences')

    if question and find_similar_sentences:
        response = send_question_to_api(question)
        similar_sentences = response.get('similar_sentences', [])
        
        for index, sentence in enumerate(similar_sentences):
            sentence_text = sentence['sentence']
            similarity_score = sentence['similarity_score']

            # Convert similarity score to percentage
            similarity_percentage = similarity_score * 100
            if similarity_percentage < 60:
                st.warning('The accuracy of the sentence is less than 60%')
                st.stop()
            else:
                with st.expander(f'Sentence {index+1} | Accuracy: {similarity_percentage:.2f}%'):
                    st.write(sentence_text)

    elif question_entered:
        st.warning("Please enter a question and click the 'Find Similar Sentences' button")

if not pdf_processed:
    st.text("Please upload a PDF file and click the 'Process File' button")
    st.text("You can only enter a question after processing the PDF file.")
    st.text("The 'Find Similar Sentences' button will only work after you enter a question.")




# if not upload:
#     st.warning('You should upload a PDF file')
# def send_question_to_api(question):
#     api_endpoint = "http://localhost:8000/find-similar-sentences/"
#     query_params = urlencode({'question': question})
#     url = f"{api_endpoint}?{query_params}"
#     response = requests.post(url)
#     return response.json()

# if upload and pdf_processed:
    # st.subheader("What is your question?")
    # question = st.text_input("Enter your question", key="input_question", placeholder="Put your question here")

    # if st.button('Find Similar Sentences'):
    #     if question:
    #         response = send_question_to_api(question)
    #         similar_sentences = response.get('similar_sentences', [])

    #         for index, sentence in enumerate(similar_sentences):
    #             sentence_text = sentence['sentence']
    #             similarity_score = sentence['similarity_score']

    #             with st.expander(f'Sentence {index+1} | Accuracy: {similarity_score}'):
    #                 st.write(sentence_text)
    #     else:
    #         st.warning("Please enter a question")
    # else:
    #     st.warning("Please upload a PDF file")



