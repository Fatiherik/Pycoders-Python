data1 = set(["green", "blue"])
data2 = set(["blue", "yellow"])
print(data1.intersection(data2))

data1 = set(["apple", "mango"])
data2 = set(["mango", "orange"])
print(data1.difference(data2))
print(data2.difference(data1))

data1 = set([5, 10, 3, 15, 2, 20])
data1=list(data1)
max_number= data1[1]
min_number=data1[1]
for i in data1:
    if i>max_number:
        max_number=i
    if i<min_number:
        min_number=i
print(max_number)
print(min_number)