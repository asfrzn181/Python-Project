import turtle as tu
from turtleBeads import *
pen = tu.Turtle()
pen.speed(3)


def draw_fn(file):
    data = open(f'{file}.txt','r')
    f = 1
    for i in  data.readlines():
        print(i)
        i = (i.strip('\n')).strip('(').strip(')')
        x,y = tuple(map(float,i.split(',')))
        if f:
            pen.penup()
            pen.goto(x+10,(y))
            f = 0
            pen.pendown()
           
        else:
            pen.goto(x+10,(y))

draw_fn('hair1')
draw_fn('hair2')
draw_fn('acc')
draw_fn('hair3')
draw_fn('hair4')
draw_fn('face1')
draw_fn('face2')
draw_fn('detail_telinga')
draw_fn('eyebrow')
draw_fn('eyebrow2')
draw_fn('eyebrowline')
draw_fn('eyebrowline2')
draw_fn('eye')
draw_fn('eye2')
draw_fn('mulut')
draw_fn('hidung')
draw_fn('leher')
draw_fn('baju1')
draw_fn('baju2')
draw_fn('baju3')
draw_fn('baju4')
draw_fn('baju5')
draw_fn('baju6')
draw_fn('baju7')
draw_fn('baju8')
draw_fn('baju9')
draw_fn('baju10')
draw_fn('akse')
draw_fn('akse2')
draw_fn('akse3')
draw_fn('akse4')
draw_fn('akse5')
tu.done()