class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def falls_in_rectangle(self, low_left, up_right):
        if low_left[0] < self.x < up_right and low_left[1] < self.y < up_right[1]:
            return True
        else:
            return False 
        
    def distance_from_point(self, point):
        return ((point.x - self.x)**2 + (point.y - self.y)**2)**0.5
    
