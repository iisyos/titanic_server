FROM python:3.10-buster

ENV LANG C.UTF-8
ENV TZ Asia/Tokyo

WORKDIR /app

COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ./src/ ./

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000", "--reload"]
