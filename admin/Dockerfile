FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip3 install --default-timeout=100 -r requirements.txt
COPY . /app