from goprohero import GoProHero
from BeautifulSoup import BeautifulSoup
import urllib
import requests
import time


class GoProConnectionError(Exception):

    def __init__(self):
        pass


class GoProPhotoBooth(object):
    """
    Establishes a connection to a WiFi-enabled GoPro camera
    and provides basic photo booth functionality.
    """

    def __init__(self, gopropassword, device_img_url, local_img_dir):

        # location of photos on device
        self.device_img_url = device_img_url

        # destination for downloaded photos
        self.local_img_dir = local_img_dir

        # for interaction with camera
        self.camera = GoProHero(password=gopropassword)
        status = self.camera.status()
        if status['summary'] == 'notfound':
            raise GoProConnectionError()

        if status['mode'] != 'still':
            # place camera in snapshot mode
            self.camera.command('mode', 'still')

        # make sure camera isn't in preview mode
        self.camera.command('preview', 'off')

    def get_photos_from_device(self):
        """
        Pulls all photos and videos from the camera over http, then
        deletes all photos from the camera.

        :return:
        True if photos/videos were pulled. False if no files found.
        """

        page = requests.get(self.device_img_url)

        soup = BeautifulSoup(page.text)

        img_names = [
            element['href'] for element in soup.findAll('a', attrs={'class': 'link'})
        ]

        if len(img_names) > 0:
            for name in img_names:

                opener = urllib.URLopener()

                opener.retrieve(self.device_img_url+name,
                                self.local_img_dir+name)

            self.camera.command('delete_all')

            return True

        else:
            return False

    def take_photo(self):
        """
        Verifies that the camera is in still mode, then takes a single photo
        and pulls all images from the database.

        :return:
        Bool. True if a photo
        """

        status = self.camera.status()
        if status['mode'] != 'still':
            # place camera in snapshot mode
            self.camera.command('mode', 'still')

        photo_successful = self.camera.command('record', 'on')

        if photo_successful:

            # sleep for two seconds so the camera can process
            # and serve the new photo via http

            retrieved = False
            while not retrieved:
                print("Waiting for image to be served.")
                time.sleep(2)
                retrieved = self.get_photos_from_device()

            print("Image got served.")
            return True

        else:
            return False

    def keep_alive(self):

        print self.camera.status()


if __name__ == '__main__':
    gppb = GoProPhotoBooth(
        'cyclops1',
        'http://10.5.5.9:8080/videos/DCIM/100GOPRO/',
        '/Users/wallacdc/Desktop/PhotoBooth/images/'
    )

    gppb.take_photo()  # takes a photo
