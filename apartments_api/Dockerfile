FROM python:3.7-alpine
WORKDIR /usr/src/app

RUN apk update \
    && apk add gcc python3-dev musl-dev curl

COPY ./requirements.txt ./requirements.txt


RUN pip3 install -r requirements.txt

COPY ./ ./

CMD ["flask", "run", "--host=0.0.0.0",  "--port=80"]
