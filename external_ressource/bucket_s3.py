import boto3

from config import s3_bucket, s3_key, s3_secret


def upload_s3(file, key_name, content_type):
    # create connection
    conn = boto3.client("s3", s3_key, s3_secret, )

    # upload the file after getting the right bucket
    bucket = conn.get_bucket(s3_bucket)

    obj = S3Key(bucket)
    obj.name = key_name
    obj.content_type = content_type
    obj.set_contents_from_string(file.getvalue())
    obj.set_acl('public-read')

    # fermer le fichier
    file.close()

    return obj.generate_url(expires_in=0, query_auth=False)
