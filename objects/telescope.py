"""
Telescope Object
 Generic telescope object
"""

class Telescope:
    def __init__(self,name,focalLength,aperture,focalRatio):
        self.name=name
        self.focalLength = focalLength
        self.aperture = aperture
        self.focalRatio=focalRatio
    
    def baseLensMagnification(self,lensFocalLength):
        baseLensFocalLength=self.focalLength/lensFocalLength
        return baseLensFocalLength
    
    def baseBarlowMagnification(self,magnification):
        baseBarlowMagnification=self.focalLength*magnification
        return baseBarlowMagnification

    def lensBarlowMagnification(self,lensFocalLength,magnification):
        lensBarlowMagnification=self.focalLength*magnification/lensFocalLength
        return lensBarlowMagnification

    def highestUsefulMagnification(self):
        highestMagnification=self.aperture*30
        return highestMagnification
