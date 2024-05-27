"""
Compass Degrees
North: 90  East: 90 | South: 180  | West: 270

"""

degrees=0
drgInc=1
counter=0


userInput=int(input("Enter degrees "))

""" 
    if degrees == userInput :
        print(userInput,"!!")
        break
"""


while degrees<360:

    if degrees==0:
            print("North")
            
            
    elif degrees==90:
            print("East")
            
            
    elif degrees==180:
            print("South")
            

    elif degrees==270:
            print("West")
            
            
    else:
            print(degrees)
    counter+=1
    degrees+=drgInc
   
    
print("End of Line")
