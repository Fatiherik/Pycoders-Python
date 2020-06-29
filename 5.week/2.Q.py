from math import gcd
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
x=gcd(a,b)
lcm=int(a*b/x)
print("The least common multiple of "+str(a)+" and "+str(b)+" is: "+str(lcm))