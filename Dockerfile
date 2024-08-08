FROM python:3.10-slim

WORKDIR /application

COPY . /application

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=application.py

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "application:application"]
