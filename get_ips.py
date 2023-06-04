from board import SCL, SDA
from PIL import Image, ImageDraw, ImageFont
import subprocess, busio, adafruit_ssd1306

index = 0
i2c = busio.I2C(SCL, SDA)
disp = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)
disp.fill(0)

image = Image.new("1", (disp.width, disp.height))
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()

draw.rectangle((0, 0, disp.width, disp.height), outline=0, fill=0)
IP = subprocess.check_output("who | cut -d'(' -f2 |cut -d')' -f1 | grep -E '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'", shell=True).decode("utf-8")
for i in IP.split("\n")[:-1]:
        draw.text((0, index), f"{i}", font=font, fill=255)
        index += 12
disp.image(image)
disp.show()
