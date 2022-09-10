FROM python:3.10-buster

ENV LANG C.UTF-8
ENV TZ Asia/Tokyo

COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

WORKDIR /app

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000", "--reload"]
