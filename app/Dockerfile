FROM ubuntu:16.04

COPY . /app
WORKDIR /app

RUN apt-get update -y
RUN apt-get install -y libmysqlclient-dev python3-pip python3-dev build-essential
RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3"]
CMD ["app.py"]