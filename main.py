from controller import *
from telescopes.zhumell114 import *
from telescopes.lens_calculator import *

telescope = Zhumell114()
lens = lens("17mm", 17)

userInput = input("Enter Lens Magnification: (17mm) ")

if userInput == "":
    lensMagnification = lens.magnification
else:
    customLens = lens(userInput,int(userInput))
    lensMagnification = customLens.magnification

print(lensMagnification)
