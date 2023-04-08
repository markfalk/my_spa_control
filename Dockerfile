FROM python:3

COPY *.py requirements.txt .

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "./main.py"]
