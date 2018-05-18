FROM python:3.6

WORKDIR /wxnacy

COPY requirements.txt ./
COPY app/local_config.py ./

RUN pip install --no-cache-dir -r requirements.txt
