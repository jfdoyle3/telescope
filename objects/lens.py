class lens:
    def __init__(self,name,magnification):
        self.name=name
        self.focalLength=magnification
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 """       

    def baseLensMagnification(self,lensFocalLength):
        baseLensFocalLength=self.focalLength/lensFocalLength
        return baseLensFocalLength
    
    def baseBarlowX2Magnification(self):
        baseBarlowX2Magnification=self.focalLength*2
        return baseBarlowX2Magnification

    def lensBarlowX2Magnification(self,lensFocalLength):
        lensBarlowX2Magnification=self.focalLength*2/lensFocalLength
        return lensBarlowX2Magnification

    def highestUsefulMagnification(self):
        highestMagnification=self.aperture*30
        return highestMagnification



# Focal Length
print("Focal Length: "+str(telescope.focalLength)+"mm")




# Base Lens Magnification
baseLensMagnification=telescope.baseLensMagnification(lens)
print("Focal length at "+str(telescope.focalLength)+"mm with a "+str(lens)+"mm is "+str(round(baseLensMagnification))+"X magnification.")



#Barlow X2 Lens Effective Magnification
baseBarlowX2Magnification=telescope.baseBarlowX2Magnification()
print("Barlow X2 Lens Effective Magnification: "+str(baseBarlowX2Magnification)+"mm")



# Barlow X2 Lens Magnification
lensBarlowX2Magnification=telescope.lensBarlowX2Magnification(lens)
print("Focal length at "+str(telescope.focalLength)+"mm with a "+str(lens)+"mm Barlow X2 gives a "+str(round(lensBarlowX2Magnification))+"X magnification.")



# Highest Useful Magnification
print("\nHighest Useful Magnification (x30): "+str(round(telescope.highestUsefulMagnification()))+"X on normal weather conditions.")
print("Highest Useful Magnification (x40): "+str(round(telescope.aperture*40))+"X on ideal weather conditions.")
print("Highest Useful Magnification (x50): "+str(round(telescope.aperture*50))+"X on ideal weather conditions.")



"""