FROM base-python:latest

RUN mkdir /myapp

WORKDIR /myapp

COPY * .

EXPOSE 9000/tcp

CMD ["python3","employee-service.py"]
