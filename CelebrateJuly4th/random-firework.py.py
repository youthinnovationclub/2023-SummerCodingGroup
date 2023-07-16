import turtle
import random

turtle.bgcolor('#f2cac7')

def get_mouse_click_coor(x, y):
  turtle.speed(0)
  print('Fiireeeworkkksss')
  firework = random.randint(0, 10) 
  if firework == 9:
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color('#0066ff')
    for i in range(36):
      turtle.speed(0)
      turtle.pensize(3)
      turtle.forward(60)
      turtle.right(180)
      turtle.forward(60)
      turtle.right(5)
    turtle.color('#ffffff')
    turtle.pensize(2)
    for i in range(20):
      turtle.forward(40)
      turtle.right(180)
      turtle.forward(40)
      turtle.left(8)
    turtle.color('red')
    for i in range(40):
      turtle.forward(20)
      turtle.right(180)
      turtle.forward(20)
      turtle.left(5)

  if firework == 8:
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
  
    for i in range(20):
      turtle.color('red')
      turtle.forward(60)
      turtle.right(145)

  if firework == 7:
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.pensize(2)
    turtle.speed(0)
    turtle.color('red')
    for i in range(50):
      turtle.forward(2)
      turtle.left(8)
    turtle.penup()
    turtle.right(90)
    turtle.forward(-9)
    turtle.pendown()
    turtle.color('white')
    for i in range(20):
      turtle.forward(40)
      turtle.right(180)
      turtle.forward(40)
      turtle.left(10)

  if firework == 6:
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.pensize(3)
    turtle.color('red')
    for i in range(100):
      turtle.forward(60)
      turtle.right(180)
      turtle.forward(60)
      turtle.right(2)
    turtle.color('blue')
    turtle.pensize(2.5)
    for i in range(50):
      turtle.forward(40)
      turtle.right(180)
      turtle.forward(40)
      turtle.right(8)
    turtle.color('white')
    turtle.pensize(2)
    for i in range(50):
      turtle.forward(20)
      turtle.right(180)
      turtle.forward(20)
      turtle.right(12)
    
  if firework == 5:
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.pensize(3)
    for i in range(20):
      turtle.color('red')
      turtle.forward(80)
      turtle.right(180)
      turtle.forward(80)
      turtle.left(8)
      turtle.color('blue')
      turtle.forward(80)
      turtle.right(180)
      turtle.forward(80)
      turtle.left(8)
      turtle.color('white')
      turtle.forward(80)
      turtle.left(180)
      turtle.forward(80)
      turtle.left(8)
      
  if firework == 4:
    turtle.penup()
    turtle.goto(x, y)
    turtle.color('white')
    turtle.pensize(2)
    turtle.pendown()
    for i in range(3):
      for i in range(5):
        turtle.forward(50)
        turtle.right(180)
        turtle.forward(50)
        turtle.right(5)
      turtle.color('blue')
      for i in range(5):
        turtle.forward(50)
        turtle.right(180)
        turtle.forward(50)
        turtle.right(5)
      turtle.color('red')
      for i in range(5):
        turtle.forward(50)
        turtle.right(180)
        turtle.forward(50)
        turtle.right(5)

  if firework == 3:
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color('red')
    turtle.pensize(5)
    for i in range(40):
      turtle.forward(80)
      turtle.right(180)
      turtle.forward(80)
      turtle.right(8)
    turtle.color('blue')
    for i in range(40):
      turtle.forward(70)
      turtle.right(180)
      turtle.forward(70)
      turtle.right(8)
    turtle.color('white')
    for i in range(40):
      turtle.forward(60)
      turtle.right(180)
      turtle.forward(60)
      turtle.right(8)
    turtle.color('red')
    for i in range(40):
      turtle.forward(50)
      turtle.right(180)
      turtle.forward(50)
      turtle.right(8)
    turtle.color('blue')
    for i in range(40):
      turtle.forward(40)
      turtle.right(180)
      turtle.forward(40)
      turtle.right(8)
    turtle.color('white')
    for i in range(40):
      turtle.forward(30)
      turtle.right(180)
      turtle.forward(30)
      turtle.right(8)
    turtle.color('red')
    for i in range(40):
      turtle.forward(30)
      turtle.right(180)
      turtle.forward(30)
      turtle.right(8)
    turtle.color('blue')
    for i in range(40):
      turtle.forward(20)
      turtle.right(180)
      turtle.forward(20)
      turtle.right(8)
    turtle.color('white')
    for i in range(40):
      turtle.forward(10)
      turtle.right(180)
      turtle.forward(10)
      turtle.right(8)
        
  if firework == 2:
    turtle.penup()
    turtle.goto(x, y)
    for i in range(50):
      turtle.pensize(3)
      turtle.forward(50)
      turtle.right(180)
      turtle.forward(50)
      turtle.right(10)
  
  
  else:
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    for i in range(23):
      turtle.pensize(1)
      turtle.speed(0)
      turtle.color('blue')
      turtle.forward(40)
      turtle.right(180)
      turtle.forward(40)
      turtle.left(8)

    turtle.penup()
    turtle.forward(20)
    turtle.right(90)
    turtle.pensize(1.5)
    turtle.pendown()
    turtle.color('#ff1200')
    for i in range(50):
      turtle.forward(3.5)
      turtle.right(10)
      
    turtle.penup()
    turtle.left(90)
    turtle.forward(11)
    turtle.right(90)
    turtle.color('#ffffff')
    turtle.pendown()

    for i in range(80):
      turtle.forward(2.6)
      turtle.right(4.5)

  


turtle.onscreenclick(get_mouse_click_coor)