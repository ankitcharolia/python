import sys
from google.cloud import storage

# Check if the bucket name is provided as a command-line argument
if len(sys.argv) < 2:
    print("Please provide the bucket name as a command-line argument.")
    sys.exit(1)

# Get the bucket name from the command-line argument
bucket_name = sys.argv[1]

# Create a client object
storage_client = storage.Client()

try:
    # Get the bucket
    bucket = storage_client.get_bucket(bucket_name)

    # Iterate over the blobs in the bucket
    blobs_total_size = 0
    for blob in bucket.list_blobs():
        blobs_total_size += blob.size

    # Convert the size to GB
    blobs_total_size_gb = blobs_total_size / (1024 ** 3)

    # Print the total size in GB
    print(f"Total size of blobs in '{bucket_name}': {blobs_total_size_gb} GB")

except Exception as e:
    print(f"Error occurred: {e}")
    sys.exit(1)

