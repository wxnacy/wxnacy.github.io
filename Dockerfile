FROM python:3.5-slim
EXPOSE 8080
COPY . .
CMD gunicorn -c gunicorn_config.py run:app
