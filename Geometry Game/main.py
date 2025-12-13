from random import randint
from Point import Point
from Rectangle import Rectangle

rectangle = Rectangle(Point(randint(0,9), randint(0,9)),
                      Point(randint(10,19), randint(10,19)))

print(f"Rectangle Coordinates: {rectangle.low_left.x},{rectangle.low_left.y} and {rectangle.top_right.x},{rectangle.top_right.y}")

user_point = Point(float(input("Guess X: ")), float(input("Guess Y: ")))

print(f"Your answer is: {user_point.falls_in_rectangle(rectangle)}")

user_area_guess = input("What is the area of this rectangle?: ")

print(f"Your answer is: {rectangle.is_area_correct(user_area_guess)}")
