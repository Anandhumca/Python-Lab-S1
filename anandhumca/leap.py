curr=int(input("Enter Current Year:"))
fut=int(input("Enter Future Year:"))
print("Leap Years:")
for curr in range(curr,fut+1):
    if((curr%4==0)and curr%100!=0 or curr%400==0):
        print(curr)
