import math
from shape import shape
class Rect(shape):
    def __init__(self, rong, dai, x, y):
        self.rong = rong
        self.dai = dai
        self.x = x
        self.y = y
    
    def chu_vi(self):
        return 2*(self.rong + self.dai)
    
    def dien_tich(self):
        return self.rong*self.dai