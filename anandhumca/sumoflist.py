num_list=[]
n=int(input("Enter The Number Of Values In List:"))
print("Enter The Elements To The List:")
for i in range(n):
    val=int(input())
    num_list.append(val)
total=0
for item in num_list:
    total=total+item
print("The Sum Of All Items In The List Is",total)
