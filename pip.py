from PIL import Image
from PIL import Image
img = Image.open('123.jpeg')
img.show()

from PIL import Image
img = Image.open('123.jpeg')
print(img.format) # Просмотр формата изображения. Выведет 'JPEG'
print(img.mode) # Просмотр типа цветового пространства. Выведет 'RGB'
print(img.size) # Просмотр размера изображения. Выведет (568, 305)
print(img.filename) # Просмотр имени файла. Выведет 'test.jpg'
r, g, b = img.split()
histogram = img.histogram()
print(histogram) # Просмотр значений RGB изображения. Выведет 1750, 255, 267, 237, 276, 299…

from PIL import Image
img = Image.open('123.jpeg')
cropped = img.crop((0, 0, 100, 200))
cropped.save('cropped_test.jpg')
img = Image.open('cropped_test.jpg')
img.show()

from PIL import Image
img = Image.open('123.jpeg')
rotated = img.rotate(180)
rotated.save('rotated_test.jpg')
img = Image.open('rotated_test.jpg')
img.show()

from PIL import Image
img = Image.open('123.jpeg')
img.save('test_png.png', 'png')

from PIL import Image, ImageDraw, ImageFont
img = Image.new('RGB', (200, 200), 'black')
img.save('test1.jpg')
img = Image.open('test1.jpg')
img.show()

from PIL import Image, ImageDraw, ImageFont
img = Image.new('RGB', (200, 200), 'black')
idraw = ImageDraw.Draw(img)
idraw.rectangle((0, 0, 100, 100), fill='white')
img.save('test1.jpg')
img = Image.open('test1.jpg')
img.show()