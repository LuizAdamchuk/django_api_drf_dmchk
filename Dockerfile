# Pull base image
FROM python:3.8.9

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY ./requirements.txt .
COPY ./config/.env ./config
RUN apt-get -y update && apt-get install -y cron && touch /var/log/cron.log && pip3 install --upgrade pip
RUN pip install -r requirements.txt

# Copy project
COPY . .

CMD service cron start