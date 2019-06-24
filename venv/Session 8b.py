class counter:
    def __init__(self):
        self.count = 1

    def incrementcount(self):
        self.count = self.count + 1

    def show(self):
        print("Count is : ",self.count)

c1 = counter()
c2 = counter()
c3 = c1

c1.incrementcount()
c2.incrementcount()
c3.incrementcount()

c1.incrementcount()
c3.incrementcount()

c1.show()
c2.show()
c3.show()