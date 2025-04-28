def download_blob(bucket_name, source_blob_name, destination_file_name):
    """Downloads a file from Google Cloud Storage"""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)

    blob.download_to_filename(destination_file_name)

    print(f"Blob {source_blob_name} downloaded to {destination_file_name}.")

# Example Usage
download_blob(
    bucket_name="your-gcs-bucket-name",
    source_blob_name="img/cymbal-product-image.png",
    destination_file_name="downloaded-cymbal-product-image.png",
)

