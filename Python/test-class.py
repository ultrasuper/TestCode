
'''
class Rectangle:
    def init(self, length=10, width=8):
        self.length = length
        self.width = width
        return self
    def show(self):
        print "length:", self.length
        print "width:", self.width

r1 = Rectangle()
r1.init(20,10)
r1.show()
'''
class Rectangle():
    def init(self ,length, width):
        self.length = length
        self.width = width
        return self
    def show(self):
        print "length:", self.length
        print "width:", self.width

r1 = Rectangle()
r1.init(30,24)
r1.show()

