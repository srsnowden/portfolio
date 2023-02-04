
import os
import shutil
import PIL
from PIL import Image

#piclist = next(os.walk("C:\Serenity\Test\images"))[2]
#picnum = int(sorted(piclist, reverse=True)[0][:-4]) + 1
#srcdir = "uploads"
#dstdir = "images"
#thmdir = "thumbnails"

up_dir = "/mnt/ark01/share/uploads"

im_dir = "/dist/cats/images"

th_dir = "/dist/cats/thumbs"

imglist = next(os.walk(up_dir))[2]

imgnum = int(sorted(imglist, reverse=True)[0][:-4]) + 1

for count, filename in enumerate(os.listdir(up_dir)):
    im_name = str(imgnum) + ".jpg"
    src = f"{up_dir}/{filename}"
    dst = f"{up_dir}/{im_name}"

    os.rename(src,dst)

    src = dst
    dst = f"{im_dir}/{im_name}"

    shutil.copy(src,dst)

    th_name = str(imgnum) + "a.jpg"
    th_dst = f"{th_dir}/{th_name}"

    img = Image.open(src)
    width = int(img.size[0]/5)
    height = int(img.size[1]/5)
    img = img.resize((width,height), Image.ANTIALIAS)
    img.save(th_dst)

    imgnum += 1

print i
