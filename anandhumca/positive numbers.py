limit=int(input("Enter The Limit:"))
num=[]
for i in range(0,limit):
    a=int(input("Enter The Number:"))
    num.append(a)
print("List:",num)
print("Positive Numbers:")
for x in num:
    if(x>0):
        print(x)
