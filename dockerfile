FROM python:3.9.1-alpine3.12

COPY normalisation.py /app/normalisation.py
COPY API_uploadfile.py /app/API_uploadfile.py

WORKDIR /app

RUN pip install --upgrade pip

RUN pip install pdfminer pypdf2 nltk fastapi uvicorn
RUN pip install python-multipart
RUN python -m nltk.downloader punkt stopwords

CMD ["uvicorn", "API_uploadfile:app", "--host", "0.0.0.0", "--port", "8080"]
