class customer:
    def __init__(self,name = "NA",phone = "NA",email = "NA"):
        self.name = name
        self.phone = phone
        self.email = email

# c1 = customer("John",4759863215,"john@example.com")
# print(c1.__dict__)
c1 = customer()
# print(c1.__dict__)

c1.name = input("Enter the Name : ")
c1.phone = int(input("Enter the Phone Number : "))
c1.email = input("Enter the Email : ")

# print(c1.__dict__)

#problem : whatever data you add in object will be temporary
#          because object will be deleted automactically and data will be lost

# Solution :
# 1. Save Data in Files
# 2. Save Data in Database

# OBJECT RELATIONAL MAPPING | ORM
# to creat table  see the structure of your object
# Type of Object i.e Class name will be Table name
# Customer -> Table Name
# Columns in the table will be those which are attributes of your Object
# name phone and email are column names
# Table can have 1 extra column to uniquley identify a row
# That column is primary key

choice = input("Would You Like to Save Customer (yes/no) : ")
if choice == "yes":
    file = open("E:\Created File\customer.csv","a")
    data = ("{},{},{}\n".format(c1.name,c1.phone,c1.email))
    file.write(data)
    file.close()