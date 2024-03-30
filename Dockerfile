FROM python:3.9-slim

EXPOSE 8080
WORKDIR /app

COPY . ./

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
