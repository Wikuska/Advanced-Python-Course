class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def falls_in_rectangle(self, rectangle):
        if min(rectangle.point1.x, rectangle.point2.x) < self.x < max(rectangle.point1.x, rectangle.point2.x) and min(rectangle.point1.y, rectangle.point2.y) < self.y < max(rectangle.point1.y, rectangle.point2.y):
            return True
        else:
            return False 
        
    def distance_from_point(self, point):
        return ((point.x - self.x)**2 + (point.y - self.y)**2)**0.5

class GuiPoint(Point):
    
    def draw(self, canvas, size = 5, color = "red"):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)
