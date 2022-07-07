from PIL import Image, ImageDraw, ImageFont

# Carregar ou importar uma imagem
# im = Image.open('spiderverse.jpg')
# im.show()

# Converter a cor da imagem
# im = Image.open('spiderverse.jpg')
# im = im.convert('1')
# im.show()


# Descobrir o tamanho da imagem
# im = Image.open('spiderverse.jpg')
# print(im.size)
# x, y = im.size
# im.show()


# Criar uma imagem do zero
# im = Image.new('RGB', (150, 150), (150, 0, 200))
# im.save('imagem.png')
# im.show()

# Criar uma imagem dividida em dois
# im = Image.new('RGB', (150, 150), (0, 180, 225))
# x, y = im.size
# for i in range(x):
#     for j in range(y):
#         if i < x // 2:
#             im.putpixel((i, j), (150, 0, 200))
# im2 = ImageDraw.Draw(im)
# im2.ellipse((x//2-50, y//2-50, x//2+50, y//2+50), fill=(105, 255, 55))
# bordas:  (ponto Upper-Left) (ponto Upper-Right);  cor: R    G    B
# im.show()


# Pegar as cores de uma imagem
# im = Image.open('spiderverse.jpg')
# x, y = im.size
# im.show()
# for i in range(x):
#     for j in range(y):
#         r, g, b = im.getpixel((i, j))
#         print(r, g, b)


# Mudar o tamanho das imagens
# im = Image.open('spiderverse.jpg')
# print(im.size)
# im = im.resize((100,100))
# im.show()

# im1 = Image.open('spiderverse.jpg')
# im2 = Image.open('capivarinha.png').resize(im1.size)
# mask = Image.new('L', im1.size)
# draw = ImageDraw.Draw(mask)
# draw.rectangle((600, 0, 1410, 800), fill=255)
# im = Image.composite(im1, im2, mask)
# im.show()

# image = Image.open(r'capivarinha.png')
# draw = ImageDraw.Draw(image)
# font = ImageFont.truetype(r'C:\Windows\Fonts\ALGER', 40)
# text = 'CAPIVARA DO BALACOBACO'
# draw.text((40, 200), text, font=font, fill=(0, 255, 0))
# image.show()