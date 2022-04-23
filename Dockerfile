FROM python:3.8

WORKDIR /main
COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "main.py"]