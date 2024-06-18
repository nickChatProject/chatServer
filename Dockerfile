#
FROM python:3.10-slim

#
WORKDIR /chatServer

#
RUN export ENV=prod
RUN mkdir files
RUN mkdir images

#
COPY requirements.txt ./requirements.txt

#
RUN pip install --no-cache-dir --upgrade -r /chatServer/requirements.txt

#

COPY app ./app

#
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]