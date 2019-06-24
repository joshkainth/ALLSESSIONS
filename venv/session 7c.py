"""
    1. Create database
    2. Create table in database following
    3. Add mysql-connector library
"""
import mysql.connector
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
c1.phone = input("Enter the Phone Number : ")
c1.email = input("Enter the Email : ")

choice = input("Would You Like to Save Customer (yes/no) : ")
if choice == "yes":

    # 1. Write SQL STATEMENT
    sql = "insert into customer values(null, '{}' , '{}','{}')".format(c1.name,c1.phone,c1.email)

    # 2. Create Connection With Database
    con = mysql.connector.connect(user = "root", password = "", host = "localhost", database = "customer_table")

    # 3. Create cursor from connection to excute sql commands : insert
    cursor = con.cursor()
    cursor.execute(sql)

    # 4. Commit as Transaction
    con.commit() #Transaction

    print(c1.name,"Saved in DATABASE")
