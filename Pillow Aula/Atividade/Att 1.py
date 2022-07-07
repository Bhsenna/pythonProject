from PIL import  Image

im = Image.new('RGB', (300, 200), (255, 255, 255))
x, y = im.size
for i in range(x):
    for j in range(y):
        if i < x // 3:
            im.putpixel((i, j), (0, 0, 255))
        if i > 2 * (x // 3):
            im.putpixel((i, j), (255, 0, 0))
im.show()