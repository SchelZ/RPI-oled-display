from board import SCL, SDA
from PIL import Image, ImageDraw, ImageFont
import subprocess, busio, adafruit_ssd1306

i2c = busio.I2C(SCL, SDA)
disp = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

disp.fill(0)

width = disp.width
height = disp.height

image = Image.new("1", (width, height))
draw = ImageDraw.Draw(image)
x = 0
index = 0

font = ImageFont.load_default()

draw.rectangle((0, 0, width, height), outline=0, fill=0)
IP = subprocess.check_output("who | cut -d'(' -f2 |cut -d')' -f1 | grep -E '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'", shell=True).decode("utf-8")
for i in IP.split("\n")[:-1]:
        draw.text((x, index), f"{i}", font=font, fill=255)
        index += 12
disp.image(image)
disp.show()
