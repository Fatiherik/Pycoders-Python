alphabet=["a","b","c","d","e","f","g","h","i","j"]
my_tuple=(1,2,3,4,5,6,7,8,9,10)
word_intervals={i:tuple(10*alphabet.index(i)+s for s in my_tuple) for i in alphabet}
print(str(word_intervals).replace('), ','),\n '))
