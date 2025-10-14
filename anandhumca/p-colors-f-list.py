clist1=set()
clist2=set()
n1=int(input("Enter The Number Of Colors In List1:"))
print("Enter The Colors To List1:")
for i in range(n1):
    color=input()
    clist1.add(color)
n2=int(input("Enter The Number Of Colors In List2:"))
print("Enter The Colors To List2:")
for i in range(n2):
    color=input()
    clist2.add(color)
diff=clist1.difference(clist2)
print("colors in list1 not in list2:",diff)
