FROM ubuntu:latest
FROM python:3
COPY . /app
WORKDIR /app
RUN pip install -r doc/requirements.txt
ENTRYPOINT ["python3"]
CMD ["app.py"]
