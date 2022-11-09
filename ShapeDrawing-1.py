import turtle
from turtle import *

#changes the window name
window = turtle.Screen()
window.title("Drawing a Shape")

#change the background color 
turtle.bgcolor("light blue")


color('forest green', 'red')
begin_fill()
while True:
    forward(300)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()