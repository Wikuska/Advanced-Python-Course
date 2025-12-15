from random import randint
import turtle
from Point import Point, GuiPoint
from Rectangle import Rectangle, GuiRectangle

rectangle = GuiRectangle(Point(randint(0,200), randint(0,200)),
                      Point(randint(10,200), randint(10,200)))

# Print rectangle coordinates
print(f"Rectangle Coordinates: {rectangle.point1.x},{rectangle.point1.y} and {rectangle.point2.x},{rectangle.point2.y}")

# Get point guess from user
user_point = GuiPoint(float(input("Guess X: ")), float(input("Guess Y: ")))
print(f"Your answer is: {user_point.falls_in_rectangle(rectangle)}")

# Get area guess from user
user_area_guess = float(input("What is the area of this rectangle?: "))
print(f"Your answer is: {rectangle.is_area_correct(user_area_guess)}")

myturtle = turtle.Turtle()
rectangle.draw(canvas=myturtle)
user_point.draw(canvas=myturtle)
turtle.done()
