#                                       STANDARDISATION PROCESS
#Type of order
class Order:
    #Constructor
    def __init__(self):
        #  print(">> init exceute")
        # print("self is: ",self)
        self.oid = 0
        self.customername = "NA"
        self.dishes = 0
        self.price = 0

    # OVER-WRITING : update
    def __init__(self,oid,name,dishes,price):
        self.oid = oid
        self.customername = name
        self.dishes = dishes
        self.price = price
#Rule : when object will be created,init will be excueted and self will contain it's hashcode

# Object Construction Statement
o1 = Order(1,"John",5,350)
print("o1 data : ",o1)

print()

o2 = Order(2,"Fionna",6,40)
print("o2 data : ",o2)

print()
print("o1 data : ",o1.__dict__)
print("o2 data : ",o2.__dict__)