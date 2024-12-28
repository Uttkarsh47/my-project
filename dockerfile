FROM python:3.12-slim

WORKDIR /app

COPY . /app


RUN pip install boto3 pymysql

ENV S3_BUCKET=""
ENV S3_KEY=""
ENV RDS_HOST=""
ENV RDS_USER=""
ENV RDS_PASSWORD=""
ENV RDS_DB=""

CMD ["python", "app.py"]

