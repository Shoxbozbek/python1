class Vektorlar:
    
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, value):
        return Vektorlar(self.x + value.x, self.y +value.y)
    
    def __repr__(self):
        return f"X ning qiymati: {self.x} va Y ning qiymati: {self.y}"
    
    
v1 = Vektorlar(10, 10)
v2 = Vektorlar(10, 10)
v3 = Vektorlar(250, 150)
    
print(v1 + v2 +v3)
    
    
    
    
    
    
    
    
    