import turtle
sides = int(input("How many sides to the shape (must be > 2) ?  "))
color1 = input("What color for the outer shape?  ")
color2 = input("What color for the inner shapes?  ")
angleChange = 360 / sides
for outSteps in range(sides):
    turtle.color(color1)
    turtle.forward(100)
    turtle.right(angleChange)
    for inSteps in range(sides):
        if (inSteps == (sides - 1)) or (outSteps == (sides -1) and inSteps == 0):
            turtle.color(color1)
        else:
            turtle.color(color2)
        turtle.forward(50)
        turtle.right(angleChange)
