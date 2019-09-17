# Use an official Python alpine runtime as a parent image
FROM python:3.7-alpine

# Make /opt/app directory, add postgres dep and upgrade pip
RUN mkdir -p /opt/app && \
  apk add --no-cache postgresql-libs && \
  apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
  pip install --upgrade pip

# Project setup
WORKDIR /opt/app
COPY app.py requirements.txt /opt/app/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Run app.py when the container launches
CMD [ "python", "./app.py" ]