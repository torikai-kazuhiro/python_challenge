##import math
##
##class Shape:
##    def __init__(self):
##        pass
##    
##    def what_am_i(self):
##        print("I am a shape")
##
##class Tectangle(Shape):
##    def __init__(self,l,w):
##        self.length = l
##        self.width = w
##
##    def calculate_perimeter(self):
##        return self.length*2 + self.width*2
##
##class Square(Shape):
##    def __init__(self,r):
##        self.radius = r
##
##    def calculate_perimeter(self):
##        return 2*math.pi*self.radius
##
##    def change_size(self,add):
##        self.radius = self.radius + add
##        
##
##tectangle = Tectangle(20,30)
##print(tectangle.calculate_perimeter())
##
##square = Square(2)
##print(square.calculate_perimeter())
##    
##square.change_size(-3)
##print(square.calculate_perimeter())
##
##shape = Shape()
##shape.what_am_i()
##tectangle.what_am_i()
##square.what_am_i()


##class Horse:
##    def __init__(self,name,rider):
##        self.name = name
##        self.rider = rider
##    
##
##class Rider:
##    def __init__(self,name):
##        self.name = name
##
##rider = Rider("Kaz")
##horse = Horse("red",rider)
##print(horse.rider.name)
##print(horse.name)
