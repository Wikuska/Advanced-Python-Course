class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def falls_in_rectangle(self, rectangle):
        if rectangle.low_left.x < self.x < rectangle.top_right.x and rectangle.low_left.y < self.y < rectangle.top_right.y:
            return True
        else:
            return False 
        
    def distance_from_point(self, point):
        return ((point.x - self.x)**2 + (point.y - self.y)**2)**0.5
    
