class Order:
    def __init__(self,oid,customername,dishes,price):
        self.oid = oid
        self.customername = customername
        self.dishes = dishes
        self.price = price

    def showorderdetails(self):
        print("#########################\t")
        print("Order Id : \t\t\t",self.oid)
        print("Customer Name : \t", self.customername)
        print("Total Dishes : \t\t", self.dishes)
        print("Order Price : \t\t", self.price)
        print("#########################\t")

choice = "yes"
orders = {}    #EMPTY LIST
while choice =="yes":
    oRef = Order(None,None,None,None)
    oRef.oid = int(input("Enter The Order ID : "))
    oRef.customername = input("Enter the Customer Name : ")
    oRef.dishes = int(input("Enter the Total dishes : "))
    oRef.price = int(input("Enter the Price : "))
    orders.add(oRef)  # LIST ACCESSING
    choice = input("You Want to enter more data (yes/no) : ")

# print("Before Sorting")
# for oRef in orders:
#     for j in range(0,len(orders)):
#         if(oRef.price[j]>oRef.price[j+1]):
#             temp = oRef.orders[j]
#             oRef.orders[j] = oRef.orders[j+1]
#             oRef.orders[j+1] = temp
# 
# print(oRef.__dict__,orders)
# 
# print("After Sorting")
# for oRef in orders:
    # oRef.showorderdetails()
print(oRef.__dict__)