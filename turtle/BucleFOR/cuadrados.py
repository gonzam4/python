import turtle

wn = turtle.Screen()
wn.bgcolor("grey")

turtle.speed(5)
turtle.left(20)
turtle.color("orange")

turtle.begin_fill()
for i in range(4):
  turtle.forward(50)
  turtle.left(90)
  turtle.forward(50)
turtle.end_fill()
turtle.left(30)
turtle.color("red")

turtle.begin_fill()
for i in range(4):
  turtle.forward(50)
  turtle.left(90)
  turtle.forward(50)
turtle.end_fill()
turtle.left(40)
turtle.color("blue")
turtle.begin_fill()

for i in range(4):
  turtle.forward(50)
  turtle.left(90)
  turtle.forward(50)
turtle.end_fill() 
turtle.left(60)
turtle.color("black")
turtle.begin_fill()

for i in range(4):
  turtle.forward(50)
  turtle.left(90)
  turtle.forward(50) 
turtle.end_fill() 
