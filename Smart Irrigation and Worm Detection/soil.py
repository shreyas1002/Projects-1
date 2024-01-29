import RPi.GPIO as GPIO
import time
from time import sleep
GPIO.setmode(GPIO.BCM)
Soil = 16

GPIO.setup(Soil, GPIO.IN)
GPIO.setwarnings(False)

#oled
import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import subprocess
RST = 0
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
disp.begin()
disp.clear()
disp.display()
width = disp.width
height = disp.height
image1 = Image.new('1', (width, height))
draw = ImageDraw.Draw(image1)
padding = -2
top = padding
bottom = height-padding
x = 0
font = ImageFont.load_default()

print("*******************Soil Sensor Activated************")
while True:
  got_something = GPIO.input(Soil)
  print(got_something)
  disp.clear()
  disp.display()
  image = draw.text((x, top+8),"Soil Sensor:"+str(got_something) ,  font=font, fill=255)
  disp.image(image1)
  disp.display()
  disp.clear()
  time.sleep(2)

  if got_something:
    print("Moisture Low")
    time.sleep(1)
   
  else:
    print("Moisture High")
    time.sleep(1)
  print("-------------------------------------")
