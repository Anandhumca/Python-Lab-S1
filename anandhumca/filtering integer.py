num=[]
n=int(input("Enter The Number Of Elements:"))
print("Enter The List Of Integers:")
for i in range(1,n+1):
    e=int(input())
    if(e>100):
        num.append("over")
    else:
        num.append(e)
print("Entered List:",num)
