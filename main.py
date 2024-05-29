from controller import *
from objects.zhumell114 import *
from objects.lens import *

telescope = Zhumell114()
lens = lens("17mm", 17)

userInput = input("Enter Lens Magnification: (17mm) ")

if userInput == "":
    lensMagnification = lens.magnification
else:
    customLens = lens(userInput,int(userInput))
    lensMagnification = customLens.magnification

print(lensMagnification)
