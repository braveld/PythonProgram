from PIL import Image
import numpy as np

img_file = 'D:/spams-python-v2.5-svn2014-07-04/spams-python/boat.png'

if __name__ == '__main__':
    try:
        img = Image.open(img_file)
    except:
        print "Cannot load image %s : skipping test" % img_file
    img.show()
