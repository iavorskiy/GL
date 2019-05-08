FROM python:3.6
WORKDIR /script
COPY gl.py ./
RUN pip install --upgrade pip
RUN pip install psutil
ENTRYPOINT  [ "python", "./gl.py" ]


