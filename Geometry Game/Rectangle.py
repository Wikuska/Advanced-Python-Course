class Rectangle:
    
    def __init__(self, low_left, top_right):
        self.low_left = low_left
        self.top_right = top_right
        
    def is_area_correct(self, area_guess):
        if area_guess == (self.top_right.x - self.low_left.x) * (self.top_right.y - self.low_left.y):
            return True
        else:
            return False