FROM python:3.9
WORKDIR /app

COPY . .
RUN apt-get update && apt-get install python3-pip -y
RUN pip3 install -r ./requirements.txt

EXPOSE 8000
CMD ["gunicorn", "app:app", "--worker-class", "gevent", "--bind", "0.0.0.0:8000"]
# CMD ["python3", "app.py"]