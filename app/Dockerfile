FROM python:3.12
WORKDIR /app
COPY . /app
RUN [ -f requirements.txt ] && pip install -r requirements.txt || echo "requirements.txt not found"
CMD ["python", "main.py"]