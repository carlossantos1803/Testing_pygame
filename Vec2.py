class Vec2():
    x = 0
    y = 0
    def __init__(self, xin = 0, yin = 0):
        self.x = xin
        self.y = yin

    def __eq__(self, value: object) -> bool:
        return (self.x == value.x and self.y == value.y)
    
    def __ne__(self, value: object) -> bool:
        return (self.x != value.x or self.y != value.y)
    
    def __add__(self, value: object) -> bool:
        return Vec2(self.x+value.x,self.y+value.y)
    
    def __sub__(self, value: object) -> bool:
        return Vec2(self.x-value.x,self.y-value.y)
    
    def __mul__(self, value: object) -> object:
        return(self.x*value, self.y*value)
    
    def __truediv__(self, value: object) -> object:
        try:
            #tmp = Vec2()
            #tmp.x /= value
            #tmp.y /= value
            return Vec2(self.x/value,self.y/value)
        #except ZeroDivisionError:
            #print('zero division error occur')
        except Exception as e:
            print(e)
        #else:
            #return tmp
        
    def __iadd__(self, rhs: object) -> object:
        self.x += rhs.x
        self.y += rhs.y
        return self
    
    def __isub__(self, rhs: object) -> object:
        self.x -= rhs.x
        self.y -= rhs.y
        return self
    
    def __imul__(self, value: object) -> object:
        self.x *= value
        self.y *= value
        return self
    
    def __idiv__(self, value: object) -> object:
        try:
            self.x /= value
            self.y /= value
        except Exception as e:
            print(e)
        else:
            return self
    
    def __repr__(self): 
        return f"Vector{self.x,self.y}"