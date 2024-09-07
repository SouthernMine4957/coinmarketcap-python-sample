FROM python:3.12.0a1-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x /usr/local/bin/python

RUN chmod +x main.py

CMD ["/bin/sh"]