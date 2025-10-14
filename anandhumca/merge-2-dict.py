mydict1={}
print("Enter The Elements of First Dict:")
while True:
    key=input("Enter A Key(or 'q' to quit):")
    if key=='q':
        break
    value=int(input("Enter A Value:"))
    mydict1[key]=value
print("Enter The Elements of Second Dict:")
mydict2={}
while True:
    key=input("Enter A Key(or 'q' to quit):")
    if key=='q':
        break
    value=int(input("Enter A Value:"))
    mydict2[key]=value
print(mydict1|mydict2)
