import math
from shape import shape
class triangle(shape):
    def __init__(self, a, b, c, x, y):
        self.a = a
        self.b = b
        self.c = c
        self.x = x
        self.y = y
    
    def chu_vi(self):
        return self.a + self.b + self.c
    def dien_tich(self):
        p = self.chu_vi()/2
        return math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))