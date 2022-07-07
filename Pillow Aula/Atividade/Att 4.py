from PIL import Image, ImageDraw

im1 = Image.open('bandeira.png')
X, Y = im1.size
im2 = Image.open('rato.jpeg').resize((Y//2, Y//2))
x, y = im2.size
mask = Image.new('L', im2.size)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0, x, y), fill=255)
mask.show()
im1.paste(im2, (X//2-x//2, Y//2-y//2), mask=mask)
im1.show()