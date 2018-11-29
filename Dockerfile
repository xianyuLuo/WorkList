FROM i.harbor.dragonest.net/public/python:3.6
COPY . /worklist
RUN pip3 install --trusted-host mirrors.aliyun.com -i http://mirrors.aliyun.com/pypi/simple -r /worklist/requirements.txt && \
  chmod +x /worklist/entrypoint.sh
USER root
WORKDIR /worklist