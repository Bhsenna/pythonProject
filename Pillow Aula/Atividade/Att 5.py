from PIL import Image, ImageDraw

im = Image.new('RGB', (2600, 2400), (0, 255, 255))
im2 = Image.open('dino.jpg')
x, y = im2.size
im3 = Image.new('RGB', (x, y), (255, 255, 255))
for i in range(x):
    for j in range(y):
        r, g, b = im2.getpixel((i, j))
        im3.putpixel((i, j), (255 - r, 255 - g, 255 - b))
mask = im3.convert('L')
dino = Image.new('RGB', (260, 240), (255, 0, 0))
x, y = im.size
k, l = dino.size
for i in range(x):
    for j in range(y):
        if not i % k and not j % l:
            im.paste(dino, (i, j), mask=mask)
im.show()