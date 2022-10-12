#First run 'pip install pillow' in terminal of pycharm then execute the below program

import PIL
from PIL import Image
from tkinter.filedialog import *
fl=askopenfilenames()
img = Image.open(fl[0])
img.save("CompressedImage1.jpg",optimize = True, quality =40)

