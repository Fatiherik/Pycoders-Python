from math import gcd
list1= list(map(int, input("Enter four number with putting space between them: ").split()))
lcm = list1[0]
for i in list1[1:]:
  lcm = lcm*i//gcd(lcm, i)
print (lcm)
