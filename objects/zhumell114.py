"""
 Zhumell 114 - https://zhumell.com/products/zhumell-z114-portable-altazimuth-reflector-telescope
    Objective/Aperture        114 mm / 4.5”
    Focal Length              450 mm
    Limiting Magnitude        12.98
    Focal Ratio               f/3.95
    Eyepiece Format           1.25”
    Finderscope               Red Dot Finder
    Mount Type                Tabletop altitudeazimuth / Dobsonian
    Tube Mount                Tube clamp 
    Mount Adjustments         Altitude-azimuth Altitude-azimuth
    Materials Wood,           Melamine Wood
"""

class Zhumell114:
    def __init__(self):
        self.name="Zhumell114"
        self.focalLength = 114
        self.aperture = 4.5
        self.focalRatio=3.95
    
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