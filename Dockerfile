# FROM python:3.8

# COPY normalisation.py /app/normalisation.py
# COPY API_uploadfile.py /app/API_uploadfile.py
# COPY requirements.txt /app/requirements.txt
# COPY logo.png ./app/logo.png
# WORKDIR /app

# RUN pip install --upgrade pip

# # RUN pip install pdfminer pypdf2 nltk fastapi uvicorn 
# # RUN pip install torch==1.0.0
# # RUN pip install transformers== 4.26.0
# # RUN pip install sentence-transformers== 2.2.2

# # RUN pip install python-multipart == 0.0.5

# # RUN python -m nltk.downloader punkt stopwords
# RUN pip install -r requirements.txt
# RUN pip install gunicorn
# RUN pip install altair>=4.0.0 vega_datasets 
# # RUN pip install vegalite
# RUN python -m spacy download en_core_web_sm

# # CMD ["uvicorn", "API_uploadfile:app", "--host", "0.0.0.0", "--port", "8888"]
# # the command to run streamlit app
# # CMD ["streamlit", "run", "home.py"]

# # docker build -t api_uploadfile .


# CMD gunicorn -w 4 -k uvicorn.workers.UvicornWorker API_uploadfile:app --bind 0.0.0.0:80 & streamlit run home.py --server.port 8501
FROM python:3.9.1-slim-buster

COPY requirements.txt /app/requirements.txt
COPY logo.png /app/logo.png
COPY API_uploadfile.py /app/API_uploadfile.py
COPY home.py /app/home.py
# COPY pages /app/pages
COPY pages/Upoad_PDF.py /app/pages/Upoad_PDF.py

WORKDIR /app
WORKDIR /app/pages
# go back to the working directory to run the command
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install gunicorn
RUN pip install altair
RUN python -m spacy download en_core_web_sm

EXPOSE 80 8501

CMD gunicorn -w 4 -k uvicorn.workers.UvicornWorker API_uploadfile:app --bind 0.0.0.0:80 & streamlit run home.py --server.port 8501


