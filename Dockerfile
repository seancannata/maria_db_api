FROM ubuntu

RUN apt-get update -y
RUN apt-get install -y python3-pip python3.8

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

RUN export APP_SETTINGS="config.DevelopmentConfig"
RUN export DATABASE_URL="localhost"
RUN export FLASK_APP=app.py

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]