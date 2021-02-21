class Square:
    square_list = []

    def __init__(self,r):
        self.radius = r
        self.square_list.append(self.radius)

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.radius,self.radius,self.radius,self.radius)


s1 = Square(2)
s2 = Square(4)
s3 = Square(6)
print(Square.square_list)

print(s1)


def Result(o1,o2):
    return o1 is o2

result = Result(s1,s2)
print(result)
