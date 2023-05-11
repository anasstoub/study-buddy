FROM python:3.9.1-slim-buster

COPY normalisation.py /app/normalisation.py
COPY API_uploadfile.py /app/API_uploadfile.py
COPY requirements.txt /app/requirements.txt
WORKDIR /app

RUN pip install --upgrade pip

# RUN pip install pdfminer pypdf2 nltk fastapi uvicorn 
# RUN pip install torch==1.0.0
# RUN pip install transformers== 4.26.0
# RUN pip install sentence-transformers== 2.2.2

# RUN pip install python-multipart == 0.0.5

# RUN python -m nltk.downloader punkt stopwords
RUN pip install -r requirements.txt
RUN python -m spacy download en_core_web_sm

CMD ["uvicorn", "API_uploadfile:app", "--host", "0.0.0.0", "--port", "8888"]
# docker build -t api_uploadfile .
