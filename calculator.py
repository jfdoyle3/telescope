from controller import *
from telescopes.zhumell114 import *

telescope = Zhumell114()

userInput = input("Enter Lens Magnification: (17mm) ")



print("\n"+telescope.name+" Base Telescope stats:")
print("--------------------------------")

# Focal Length
print("Focal Length: "+str(telescope.focalLength)+"mm")

#Barlow X2 Lens Effective Magnification
baseBarlowX2Magnification = telescope.baseBarlowX2Magnification()
print("Barlow X2 Lens Effective Magnification: "+str(baseBarlowX2Magnification)+"mm")

# Base Lens Magnification
baseLensMagnification = telescope.baseLensMagnification(lens)
print("Focal length at "+str(telescope.focalLength)+"mm with a "+str(lens)+"mm is "+str(round(baseLensMagnification))+"X magnification.")

# Barlow X2 Lens Magnification
lensBarlowX2Magnification = telescope.lensBarlowX2Magnification(lens)
print("Focal length at "+str(telescope.focalLength)+"mm with a "+str(lens)+"mm Barlow X2 gives a "+str(round(lensBarlowX2Magnification))+"X magnification.")

# Highest Useful Magnification
print("\nHighest Useful Magnification (x30): "+str(round(telescope.highestUsefulMagnification()))+"X on normal weather conditions.")
print("Highest Useful Magnification (x40): "+str(round(telescope.aperture*40))+"X on ideal weather conditions.")
print("Highest Useful Magnification (x50): "+str(round(telescope.aperture*50))+"X on ideal weather conditions.")





print("\n\n\nend of line")