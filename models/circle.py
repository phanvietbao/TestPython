import math
from shape import shape
class Circle(shape):
    def __init__(self, ban_kinh, x, y):
        self.ban_kinh = ban_kinh
        self.x = x
        self.y = y
    
    def chu_vi(self):
        return 2*math.pi*self.ban_kinh
    
    def dien_tich(self):
        return math.pi*self.ban_kinh*self.ban_kinh