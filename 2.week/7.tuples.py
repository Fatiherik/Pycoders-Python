tup1 = ('n', 'e', 't', 'h', 'e', 'r', 'l', 'a', 'n', 'd', 's')
new_tup1="".join(tup1)
print(new_tup1)

tup2 = [(3,6), (5,8), (7,4)]
unzip_tup2 = [tuple(i for i, j in tup2), tuple(j for i, j in tup2)]
print(unzip_tup2)


tup3 = [("a", 1), ("a", 2), ("a", 3), ("b", 1), ("b", 2), ("c", 1)]
new_tup3 = {}
for a, b in tup3:
    new_tup3.setdefault(a, []).append(b)
print (new_tup3)