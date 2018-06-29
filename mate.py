import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import subprocess

RST = None
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

display = Adafruit_SSD1306.SSD1306_128_32(rst = RST)

display.begin()

display.clear()

display.display()

width = display.width
height = display.height

image = Image.new("1", (width, height))

draw = ImageDraw.Draw(image)

draw.rectangle((0, 0, width, height), outline = 0, fill = 0)

x = 0
y = -7

# font = ImageFont.load_default()
font = ImageFont.truetype("zero.ttf", 16)

while True:

	draw.text((x, y), str("Rider Mate mark 1"), font = font, fill = 255)

	draw.rectangle((0, 1, width, height - 1), outline = 0, fill = 255)

	display.image(image)

	display.display()

	time.sleep(.1)
