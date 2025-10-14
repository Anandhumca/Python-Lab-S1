def findgcd(a,b):
    while b:
        a,b=b,a%b
    return a
num1=int(input("Enter  The First Number:"))
num2=int(input("Enter The Second Number:"))
gcd=findgcd(num1,num2)
print(f"The GCD of {num1} and {num2} is {gcd}.")
