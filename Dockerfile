FROM python:3.6
ENV PYTHONUNBUFFERED=1
RUN mkdir -p /data/web/
RUN python -m pip install --upgrade pip
WORKDIR /data/web/
ADD requirements.txt /data/web/
RUN pip install -r requirements.txt
# ADD . /code/