names=[]
acount=0
n=int(input("Enter The Number Of First Names:"))
print("Enter The Names:")
for i in range(n):
    name=input()
    names.append(name)
for name in names:
    acount+= name.lower().count('a')
print("Number of a :",acount)
