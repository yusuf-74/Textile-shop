FROM python:latest

WORKDIR /server

# System dependencies are updated less often than python dependencies
RUN pip3 install --upgrade pip 

# Python dependencies are updated less often than source code so we need layer arch
COPY requirements.txt .

RUN pip3 install -r requirements.txt


