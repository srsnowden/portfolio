
import os
import shutil
import PIL
from PIL import Image
from yattag import Doc, indent

doc, tag, text = Doc().tagtext()

up_dir = "/mnt/ark01/share/Uploads"
im_dir = "/dist/cats/images"
th_dir = "/dist/cats/thumbnails"

imglist = next(os.walk(im_dir))[2]

imgnum = int(sorted(imglist, reverse=True)[0][:-4]) + 1

for count, filename in enumerate(os.listdir(up_dir)):
    im_name = str(imgnum).zfill(3)
    src = f"{up_dir}/{filename}"
    dst = f"{up_dir}/{im_name}.jpg"

    os.rename(src,dst)

    src = dst
    dst = f"{im_dir}/{im_name}"

    shutil.copy(src,dst)

    th_dst = f"{th_dir}/{im_name}a.jpg"

    img = Image.open(src)
    width = int(img.size[0]/5)
    height = int(img.size[1]/5)
    img = img.resize((width,height), Image.ANTIALIAS)
    img.save(th_dst)

    imgnum += 1

imglist = next(os.walk(up_dir))[2]

i = int(sorted(imglist, reverse=True)[0][:-4])

doc.asis('<!DOCTYPE html>')
with tag('html', ('lang', 'en')):
    with tag('head'):
        with tag('meta', ('charset', 'utf-8')):
            with tag('title'):
                text('cats')
            doc.stag ('link', ('rel', 'stylesheet'), ('href', 'cats.css'))
    with tag('body'):
        with tag('center'):
            while i > 0:
                im_name = "images/" + str(i).zfill(3) + ".jpg"
                th_name = "thumbnails/" + str(i).zfill(3) + "a.jpg"
                with tag('div', klass='column'):
                    with tag('div', klass='gallery'):
                        with tag('a', ('target', '_blank'), ('href', f"{im_name}")):
                            doc.stag ('img',('src', f"{th_name}"))
                i -= 1

result = indent(doc.getvalue())

with open('/dist/cats/index.html', 'w') as f:
    f.writelines(result)