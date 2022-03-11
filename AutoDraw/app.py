from turtle import *

import turtle
turtle.bgpic("image.png")
# self defined function to print coordinate
def buttonclick(x,y):   
    f = open("koordinat.txt","a")
    f.write("({0},{1})".format(x,y)+ "\n")
    f.close()
 
 #onscreen function to send coordinate


onscreenclick(buttonclick,1)
listen()  # listen to incoming connections
speed(10) # set the speed
done()    # hold the screen