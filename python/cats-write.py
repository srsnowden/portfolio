from yattag import Doc, indent

doc, tag, text = Doc().tagtext()

i = 101

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
                im_name = "uploads/" + str(i) + ".jpg"
                th_name = "thumbnails/" + str(i) + "a.jpg"
                with tag('div', klass='column'):
                    with tag('div', klass='gallery'):
                        with tag('a', ('target', '_blank'), ('href', f"{im_name}")):
                            doc.stag ('img',('src', f"{th_name}"))
                i -= 1

result = indent(doc.getvalue())

with open('index.html', 'w') as f:
    f.writelines(result)