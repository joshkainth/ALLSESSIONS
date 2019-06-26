# list1 = [3,8,9,7,6]
list2 = map(int, input("Enter elements in list : ").split())
rotation = int(input("Enter how many times you want to rotate :"))
list2 = list(list2)
for i in range(int(rotation)):
    list2 = list2[-1:] + list2[:-1]
    print(f"after {i+1} rotation : ",list2)