import turtle

class Rectangle:
    
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
        
    def is_area_correct(self, area_guess):
        if area_guess == (self.point2.x - self.point1.x) * (self.point2.y - self.point1.y):
            return True
        else:
            return False
        
class GuiRectangle(Rectangle):
    
    def draw(self, canvas):
        canvas.penup()
        canvas.goto(self.point1.x, self.point1.y)
        canvas.pendown()
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)
        
