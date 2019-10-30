class Circle():

    pi = 3.14

    def __init__(self,redius=1):
        self.redius = redius
        print (self.pi)

class Test(Circle):
    def __init__(self):
        print (self.pi)

mytest = Test()

