from PIL import Image

im = Image.new('1', (400, 400), 1)
x, y = im.size
k = 1
for i in range(x):
    for j in range(y):
        if not i % 50 and not j % 400:
            if k == 1:
                k = 0
            else:
                k = 1
        if not j % 50:
            if k == 1:
                k = 0
            else:
                k = 1
        im.putpixel((i, j), k)

im.show()