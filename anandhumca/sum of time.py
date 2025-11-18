class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __add__(self, other):
        h = self.hour + other.hour
        m = self.minute + other.minute
        s = self.second + other.second

        m=m+s//60
        s=s%60

        h=h+m//60
        m=m%60
        
        return Time(h, m, s)


print("Time 1")
h1 = int(input("Enter hour: "))
m1 = int(input("Enter minute: "))
s1 = int(input("Enter second: "))
t1 = Time(h1, m1, s1)

print("\nTime 2")
h2 = int(input("Enter hour: "))
m2 = int(input("Enter minute: "))
s2 = int(input("Enter second: "))
t2 = Time(h2, m2, s2)

t3 = t1 + t2

print("\nTotal Time:", t3.hour, ":", t3.minute, ":", t3.second)
