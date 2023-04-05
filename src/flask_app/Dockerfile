FROM python:3.9
WORKDIR /app

COPY . .
RUN apt-get update && apt-get install python3-pip -y
RUN pip3 install flask==2.1.3 && \
  pip3 install flask-restful && \
  pip3 install flask-cors && \
  pip3 install flask-classful -U && \
  pip3 install Werkzeug==2.1.2 && \
  pip3 install pyyaml

EXPOSE 8000
CMD ["python3", "app.py"]