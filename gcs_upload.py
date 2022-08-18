import os
import glob

from google.cloud import storage

project_id = 'hannstar-first'
bucket_name = 'gcp-introduction-hannstar'
bucket_file = 'test02.txt'
local_file = 'test.txt'
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = glob.glob("*.json")[0]

# Initialise a client
client = storage.Client(project_id)
# Create a bucket object for our bucket
bucket = client.get_bucket(bucket_name)
# Create a blob object from the filepath
blob = bucket.blob(bucket_file)
# Upload the file to a destination
blob.upload_from_filename(local_file)