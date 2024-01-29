import RPi.GPIO as GPIO
import dht11
import time

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
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
instance = dht11.DHT11(pin=20)
print("**********DHT 11 Sensor Activate************")
while True:
    result = instance.read()
    if result.is_valid():
        a = result.temperature
        print("Enviorment Tempreture:"+str(a))
        
        b = result.humidity
        print("Enviorment Humidity:"+str(b))
        disp.clear()
        disp.display()
        draw.text((x, top+25),"Humidity Sensor:"+str(b) ,  font=font, fill=255)
        draw.text((x, top+36),"Temp Sensor:"+str(a) ,  font=font, fill=255)
        disp.image(image1)
        disp.display()
        disp.clear()
        time.sleep(1)
        print("-------------------------------------")
            
    
   
        

                                                           

 
 

