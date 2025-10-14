clrs=[]
count=int(input("Enter The Number Of Colors:"))
print("Enter The Colors:")
for i in range(count):
    color=input()
    clrs.append(color)
print("First Color:",clrs[0],"Last Color:",clrs[count-1])
