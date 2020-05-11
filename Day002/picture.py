from PIL import Image, ExifTags
import time

images = ('tab.jpg','bailey.jpg','benson.jpg','brindle.jpg','brock.jpg')

for i in images:
    im = Image.open(i)
    im.show()
    im.close()