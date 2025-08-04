FROM python:3.13.3

WORKDIR /src

COPY requirements.txt .
RUN pip install -r requirements.txt

CMD [ "python", "app.py" ]