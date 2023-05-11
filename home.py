import streamlit as st
from PIL import Image
# sidebar


# Set page configuration
st.set_page_config(page_title="Home")

# Define columns for logo and app name
logo_col, name_col = st.columns([1, 4])

# Add logo to the logo column
with logo_col:
    st.image(Image.open('logo.png'), width=150)

# Add app name to the name column
with name_col:
    st.title("Study Buddy")
    st.caption('A smart tool for students :book:')
# Add the steps for using the app
# st.write("To use the app, follow these simple steps:")
# st.write("1. Upload a PDF document using the file uploader.")
# st.write("2. Wait for the app to process the document and extract its sentences.")
# st.write("3. Enter your question in the text box below.")
# st.write("4. Click the 'Find Similar Sentences' button to get the most relevant sentences from the document.")

# Add a button to get started
# st.button("Get Started")

# Add app description
st.subheader('Welcome to Study Buddy!')
st.write('AI-powered study assistant that helps you extract important information from your study materials and answer your questions quickly and accurately.')

# Add instructions on how to use the app
st.subheader('To Get Started !')

# st.write('To get started, upload your study materials in PDF format and wait for them to be processed. Once the processing is complete, you can type in your questions and Study Buddy will provide you with the most relevant answers.')