import boto3
import pymysql
import os

S3_BUCKET = os.getenv("S3_BUCKET")
S3_KEY = os.getenv("S3_KEY")
RDS_HOST = os.getenv("RDS_HOST")
RDS_USER = os.getenv("RDS_USER")
RDS_PASSWORD = os.getenv("RDS_PASSWORD")
RDS_DB = os.getenv("RDS_DB")

def read_from_s3():
    s3 = boto3.client("s3")
    try:
        response = s3.get_object(Bucket=S3_BUCKET, Key=S3_KEY)
        data = response["Body"].read().decode("utf-8")
        print("Data read from S3 successfully.")
        return data
    except Exception as e:
        print(f"Error reading from S3: {e}")
        return None

def write_to_rds(data):
    try:
        connection = pymysql.connect(
            host=RDS_HOST,
            user=RDS_USER,
            password=RDS_PASSWORD,
            database=RDS_DB,
        )
        cursor = connection.cursor()
        cursor.execute("INSERT INTO your_table (data_column) VALUES (%s)", (data,))
        connection.commit()
        print("Data written to RDS successfully.")
        connection.close()
    except Exception as e:
        print(f"Error writing to RDS: {e}")

def handler():
    data = read_from_s3()
    if data:
        write_to_rds(data)

if __name__ == "__main__":
    handler()

