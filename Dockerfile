FROM python:3.6
ENV PYTHONUNBUFFERED=1
RUN mkdir /code
RUN python -m pip install --upgrade pip
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
# ADD . /code/