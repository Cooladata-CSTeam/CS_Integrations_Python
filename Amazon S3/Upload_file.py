from boto.s3.connection import S3Connection
from boto.s3.key import Key
import datetime
import pandas as pd

AWS_ACCESS_KEY = '<your access key>'
AWS_SECRET_KEY = '<your secret key>'
BUCKET_NAME = '<S3 bucket name>'
file_name = '<file name to upload>' + datetime.datetime.now().strftime("%Y-%m-%d") + '<extension.csv>'
folder_name = '<folder name in S3 bucket>'


conn = S3Connection(AWS_ACCESS_KEY, AWS_SECRET_KEY)
mybucket = conn.get_bucket(BUCKET_NAME)
key = Key(mybucket, folder_name+"/"+file_name)

csv_file = data.to_csv(file_name)
key.set_contents_from_filename(file_name)

coolaResult = data