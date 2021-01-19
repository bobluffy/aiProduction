# # base docker image for the run-time environment
FROM rackspacedot/python37
LABEL maintainer="bob <bobyuan1015@gmail.cn>"

#the run-time environment preparation
RUN apt-get update && \
         apt install -y openjdk-8-jdk gcc&&apt-get update --fix-missing && \
         pip install --upgrade numpy pandas requests flask_cors pymysql mrfh -i https://mirrors.aliyun.com/pypi/simple/&& \
         pip install gunicorn -i https://mirrors.aliyun.com/pypi/simple/&& \
         pip install flask -i https://mirrors.aliyun.com/pypi/simple/&& \
         pip install gevent -i https://mirrors.aliyun.com/pypi/simple/&& \
         pip install Cython -i https://mirrors.aliyun.com/pypi/simple/&& \
         pip install zhon -i https://mirrors.aliyun.com/pypi/simple/&& \
         pip install gensim -i https://mirrors.aliyun.com/pypi/simple/&& \
         pip install jieba -i https://mirrors.aliyun.com/pypi/simple/&& \
         pip install DBUtils -i https://mirrors.aliyun.com/pypi/simple/&& \
         pip install PyMySQL==0.10.1 -i https://mirrors.aliyun.com/pypi/simple/&& \
         pip install pandas==0.25.1 -i https://mirrors.aliyun.com/pypi/simple/&& \
         pip install PyYAML -i https://mirrors.aliyun.com/pypi/simple/
#          pip install python-Levenshtein -i https://mirrors.aliyun.com/pypi/simple/

#copy config and data files into the docker image
COPY app /data/ai_server/app
COPY confs /data/ai_server/confs
COPY test /data/ai_server/tests
COPY start.sh  /data/ai_server/start.sh

#expose the http port outside
EXPOSE 6666
WORKDIR /data/ai_server
ENV LANG C.UTF-8
ENV SHELL=/bin/bash
RUN ["chmod", "+x", "start.sh"]


#lanch the server once the docker is running
ENTRYPOINT ["./start.sh"]
