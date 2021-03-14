# Pull image
FROM python:3.8.8-slim-buster

# Set work directory
WORKDIR /usr/src/app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# Install development dependencies
COPY ./dev-requirements.txt /usr/src/app/dev-requirements.txt
RUN pip install -r dev-requirements.txt

# Copy project
COPY . /usr/src/app

EXPOSE 5000