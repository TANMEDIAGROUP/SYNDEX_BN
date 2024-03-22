# python version
FROM python:3.8.1
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1
COPY requirements.txt requirements.txt
#install dependencies 
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 3000
RUN python3 server.py makemigrations api
RUN python3 server.py migrate api
RUN python3 server.py runserver 3000