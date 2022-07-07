from PIL import Image, ImageDraw

im = Image.open('spiderverse.jpg')
x, y = im.size
im2 = Image.new('RGB', (x, y), (255, 255, 255))
for i in range(x):
    for j in range(y):
        r, g, b = im.getpixel((i, j))
        im2.putpixel((i, j), (255 - r, 255 - g, 255 - b))
im3 = ImageDraw.Draw(im2)
im3.ellipse((x//2-5, y//2-5, x//2+5, y//2+5), fill=(255, 0, 0))
im2.show()