data ={
'a': [5, 3, 9, 0, 2, 3, 1],
'b': [4, 7, 5, 1, 2],
'c': [8,1, 3, 2, 4]
}

new_data = {}
for key, value in data.items():
    new_data.setdefault(key,sorted(value))
print (new_data)

