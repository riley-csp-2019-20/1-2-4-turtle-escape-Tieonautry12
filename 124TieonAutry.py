import turtle as trtl
import random


ty = trtl.Turtle()
ty.pensize(3)
ty.ht()
ty.speed(0)

fish = trtl.Turtle()
fish.pencolor("red")

door_width = 15
wall_width = 15


count = 20


def fish_up():
    fish.setheading(90)
    fish.forward(10)

def fish_down():
    fish.setheading(270)
    fish.forward(10)

def fish_left():
    fish.setheading(180)
    fish.forward(10)

def fish_right():
    fish.setheading(0)
    fish.forward(10)



def drawDoor():
    ty.penup()
    ty.forward(door_width)
    ty.pendown()

def drawWall():
    ty.right(90)
    ty.forward(wall_width*2)
    ty.backward(wall_width*2)
    ty.left(90)

for i in range(25):

    if i > 4:

        door = random.randint(wall_width, count - 2*wall_width)
        barrier = random.randint(wall_width, count - 2*wall_width)

        if door < barrier:
            ty.forward(door)
            drawDoor()
            ty.forward(barrier-door-door_width)
            drawWall()
            ty.forward(count-barrier)

        else:
            ty.forward(barrier)
            drawWall()
            ty.forward(door-barrier)
            drawDoor()
            ty.forward(count-door-door_width)

    count = count + wall_width
    ty.left(90)



wn = trtl.Screen()
wn.onkeypress(fish_up, "Up")
wn.onkeypress(fish_down, "Down")
wn.onkeypress(fish_left, "Left")
wn.onkeypress(fish_right, "Right")
wn.listen()


wn.mainloop()