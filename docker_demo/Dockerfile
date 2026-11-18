FROM python:3.12-slim
#sets folder inside the container as work dir
WORKDIR /app
#copy local folder to the work dir
copy . /app
#when container starts - opens hello.py with python
ENTRYPOINT ["python3", "hello.py"]