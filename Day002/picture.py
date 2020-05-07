from PIL import Image
import time


def img(str):
    im = Image.open(str)
    out = im.rotate



out = im.rotate(90, expand=1)
out.save('tab2.jpg')
im.close()

g = Image.open('tab2.jpg')

g.show()
g.close()

br = Image.open('brock.jpg')
brr = br.rorate(270, expand=1)
brr.save('brock2.jpg')
br.close
br.show()
im = Image.open("C:\\Users\\Chris Walters\\100 Days of Code\\Day002\\tab.jpg")