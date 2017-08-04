import time

from os import listdir, remove as remove_file
from os.path import isfile, join

from utils import upload_to_s3

from settings import SAVE_DIR


def list_files(path):
    return [file for file in listdir(path) if isfile(join(path, file)) and file.endswith('.jpg')]


if __name__ == '__main__':
    print 'Watching folder for images...'

    while True:
        filenames = list_files(SAVE_DIR)

        if len(filenames) != 0: # new files to upload to S3
            print '\n New pictures to upload to S3: %s' % str(filenames)

            for filename in filenames:
                path = join(SAVE_DIR, filename)
                upload_to_s3(path, filename=filename)
                remove_file(path)

            print '\n finished uploading!'

        time.sleep(10)
