import turtle as a
import random
from  time import sleep
def liner():
    height = input('выберите длину линий(длиные, средние или короткие)').lower()
    if height == 'длиные':
       line_lenght = 250
    elif height == 'средние':
        line_lenght = 200
    elif height == 'короткие':
        line_lenght = 100
    return line_lenght
def width():
    titanic = input('выберите ширину линий(широкая, средняя, узкая)').lower()
    if titanic == 'широкая':
        line_weights = 50
    elif titanic == 'средняя':
        line_weights = 30
    elif titanic == 'узкая':
        line_weights = 10
    return line_weights

def nokaut():
    limit_left = (-a.window_width() / 2) + 100
    print(limit_left)
    limit_right = (a.window_width() / 2) - 100
    print(limit_right)
    limit_up = (a.window_height() / 2) - 100
    limit_down = (-a.window_height() / 2) + 100
    (x, y) = t.pos()
    simfonia_morey = limit_left < x < limit_right and limit_up > y > limit_down
    print(simfonia_morey)
    return simfonia_morey
def move_turtle(liners):
    pen_colors = ['red', 'orange', 'yellow', 'green', 'blue']
    t. color(random.choice(pen_colors))
    t.shapesize(3,3,1)
    t.stamp()
    if nokaut():
        angle = random.randint(0, 180)
        t.right(angle)
        t.forward(liners)
    else:
        t.backward(liners)
#  liners = width()

t = a.Turtle()
a.bgcolor('black')
t.shape('turtle')
t.color("black")
liners = width()
print(liners)
t.pensize(liners)
lenght = liner()
print(lenght)

#sleep(12)
while True:
    move_turtle(lenght)


