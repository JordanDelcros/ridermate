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

display = Adafruit_SSD1306.SSD1306_128_32(rst=RST)

display.begin()

display.clear()

display.display()

width = display.width
height = display.height

image = Image.new("1", (width, height))

draw = ImageDraw.Draw(image)

draw.rectangle((0, 0, width, height), outline = 0, fill = 0)

padding = 0
top = padding
bottom = height - padding

x = 0

# font = ImageFont.load_default()
font = ImageFont.truetype("silkscreen.ttf", 11)

while True:

	draw.rectangle((0, 0, width, height), outline = 0, fill = 0)

	cmd = "hostname -I | cut -d\' \' -f1"
	IP = subprocess.check_output(cmd, shell = True )
	cmd = "top -bn1 | grep load | awk '{printf \"CPU Load: %.2f\", $(NF-2)}'"
	CPU = subprocess.check_output(cmd, shell = True )
	cmd = "free -m | awk 'NR==2{printf \"Mem: %s/%sMB %.2f%%\", $3,$2,$3*100/$2 }'"
	MemUsage = subprocess.check_output(cmd, shell = True )
	cmd = "df -h | awk '$NF==\"/\"{printf \"Disk: %d/%dGB %s\", $3,$2,$5}'"
	Disk = subprocess.check_output(cmd, shell = True )

	# Write two lines of text.

	# draw.text((x, top), "IP: " + str(IP), font = font, fill = 255)

	# draw.text((x, top + 10), str(CPU), font = font, fill = 255)

	# draw.text((x, top + 20), str(MemUsage), font = font, fill = 255)

	# draw.text((x, top + 30), str(Disk), font = font, fill = 255)

	draw.text((x, top), str("Rider Mate mark 1"), font = font, fill = 255)

	display.image(image)

	display.display()

	time.sleep(.1)
