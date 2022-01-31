import random
from webbrowser import BackgroundBrowser
from PIL import Image
import os
#Set Dpi Length
Dpilength = (500,500)
#Set max generate images
gen=12
for m in range(0,gen):
    r = lambda: random.randint(0,255)
    nama = print('#%02X%02X%02X' % (r(),r(),r()))
    nama2 = str('#%02X%02X%02X' % (r(),r(),r()))
    print(nama2)
    webhexcolor = nama2
    im = Image.new("RGB", Dpilength , webhexcolor)
    im.save( os.path.abspath(os.getcwd()) + "/Background/"+ str(nama2) +".png")