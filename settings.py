import os

from GoProPhotoBooth import GoProPhotoBooth


GOPRO_PASSWORD = 'cyclops1'
GOPRO_URL = 'http://10.5.5.9:8080/videos/DCIM/100GOPRO/'

PROJECT_PATH = os.path.dirname(os.path.realpath(__file__))
SAVE_DIR = '{}/templates/assets/photos'.format(PROJECT_PATH)

# BOOTH = GoProPhotoBooth(GOPRO_PASSWORD, GOPRO_URL, SAVE_DIR)
