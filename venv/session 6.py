class order:
    pass

o1 = order()
o2 = order()

o3 = o1 # Reference Copy

print("o1 data : ",o1.__dict__)
print("o2 data : ",o2.__dict__)
print("o3 data : ",o3.__dict__) 