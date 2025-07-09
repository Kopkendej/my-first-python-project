import turtle
ablak = turtle.Screen()
ablak.title("Üzenet a teknőstől")

mate = turtle.Turtle()

mate.color("blue")
mate.pensize(3)

mate.penup()
mate.goto(-100, 0)
mate.pendown()

mate.write("Máté megyünk Gartic Phone?", font=("Arial", 24, "normal"))
turtle.done()