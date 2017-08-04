import boto
import boto.s3
import uuid
import sys
from boto.s3.key import Key

import secret

ACCESS_KEY = secret.AWS_ACCESS_KEY_ID
SECRET = secret.AWS_SECRET_ACCESS_KEY


def uuid_filename(extension='.jpg'):
    return '{}{}'.format(
        uuid.uuid1().get_hex(),
        extension
    )

def upload_to_s3(file, filename=None):
    connection = boto.connect_s3(ACCESS_KEY, SECRET)
    bucket = connection.get_bucket(secret.AWS_BUCKET_NAME)
    k = Key(bucket)
    k.key = filename or uuid_filename()
    k.set_contents_from_filename(file, cb=percent_cb, num_cb=10)

def percent_cb(complete, total):
    sys.stdout.write('.')
    sys.stdout.flush()
