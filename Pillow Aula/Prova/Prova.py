from PIL import Image, ImageDraw, ImageFont

im = Image.new('RGB', (500, 500), (140, 0, 255))
draw = ImageDraw.Draw(im)
font = ImageFont.truetype(r'C:\Windows\Fonts\ALGER', 80)
text = 'Bernardo\n   Hazime'
draw.text((40, 170), text, font=font, fill=(0, 255, 0))
im.show()