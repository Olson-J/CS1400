import turtle

turtle.speed(100)
turtle.hideturtle()

# yellow circle for face
turtle.pensize(15)
turtle.color("yellow")
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()

# eyes
turtle.penup()
turtle.goto(-20, 55)
turtle.pensize(10)
turtle.color("black")
turtle.pendown()
turtle.circle(5)
turtle.penup()
turtle.forward(40)
turtle.pendown()
turtle.circle(5)

# mask body
turtle.penup()
turtle.pensize(5)
turtle.goto(-20, 30)
turtle.color("light blue")
turtle.begin_fill()
turtle.pendown()
turtle.forward(40)
turtle.right(20)
turtle.forward(2)
turtle.right(40)
turtle.forward(2)
turtle.right(40)
turtle.forward(2)
turtle.forward(20)
turtle.right(80)
turtle.forward(35)
turtle.right(75)
turtle.forward(24)
turtle.right(40)
turtle.end_fill()
turtle.penup()

# mask tie, upper left
turtle.left(90)
turtle.forward(5)
turtle.color("white")
turtle.pendown()
turtle.forward(35)
turtle.penup()

# mask tie, lower left
turtle.goto(-20, 4)
turtle.left(50)
turtle.pendown()
turtle.forward(8)
turtle.penup()

# mask tie, lower right
turtle.goto(22, 4)
turtle.left(130)
turtle.pendown()
turtle.forward(8)
turtle.penup()

# mask tie, upper left
turtle.goto(27, 30)
turtle.pendown()
turtle.left(45)
turtle.forward(30)

# left eyebrow
turtle.penup()
turtle.color("black")
turtle.pensize(3)
turtle.left(100)
turtle.goto(-15, 85)
turtle.pendown()
turtle.circle(10, 140)
turtle.penup()


# right eyebrow
turtle.goto(30,80)
turtle.right(60)
turtle.pendown()
turtle.forward(20)
turtle.penup()

# text
turtle.goto(-50, -40)
turtle.write("This emoji is skeptical that mesh masks are CDC approved",move = False)
turtle.goto(-50, -55)
turtle.write("It will give you this lollipop to wear a better one", move = False)

# lollipop
turtle.goto(-70, -40)
turtle.left(70)
turtle.pendown()
turtle.color("brown")
turtle.forward(20)
turtle.penup()
turtle.back(20)
turtle.color("pink")
turtle.left(90)
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()

turtle.done()