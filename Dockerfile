# Python and Linux Version 
FROM python:3.10.0a1-alpine3.12

COPY ./requirements.txt /requirements.txt

# Configure server
RUN set -ex \
    && pip install --upgrade pip \  
    && apk add build-base \
    && pip install --no-cache-dir -r /requirements.txt 

# Working directory
WORKDIR /app

ADD . .


# EXPOSE 8000

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

CMD gunicorn project.wsgi:application --bind 0.0.0.0:$PORT