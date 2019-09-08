FROM python:3.6
ENV PYTHONUNBUFFERED=1
RUN mkdir -p /data/web/
RUN python -m pip install --upgrade pip
WORKDIR /data/web/
ADD requirements.txt /data/web/
# 用国内的源
RUN pip install -r requirements.txt
# -i https://pypi.tuna.tsinghua.edu.cn/simple/
# ADD . /code/