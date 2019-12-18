FROM python:3.7-alpine

WORKDIR /app

COPY requirements.txt* .

#RUN pip install --upgrade pip
RUN pip install gunicorn flask
RUN touch requirements.txt
RUN pip install -r requirements.txt

CMD ["gunicorn", "-b", ":5000", "app:app"]

