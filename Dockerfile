FROM ubuntu

RUN apt-get update -y
RUN apt-get install -y python3-pip python3.8 curl
RUN apt-get install -y wget 

RUN wget https://downloads.mariadb.com/MariaDB/mariadb_repo_setup
RUN chmod +x mariadb_repo_setup
RUN ./mariadb_repo_setup \
   --mariadb-server-version="mariadb-10.2"
RUN apt-get install libmariadb3 libmariadb-dev -y

COPY ./requirements.txt /requirements.txt
RUN pip3 install -r requirements.txt

ADD app.py /

EXPOSE 5000

CMD [ "python3", "./app.py" ]
# CMD ["flask", "run"]
# CMD ["python3" "manage.py" "run" "-h" "0.0.0.0"]