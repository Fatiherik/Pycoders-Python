def counter():
    word=input("Enter a string: ")
    count_upper=0
    count_lower=0
    for i in word:
        if i.isupper():
            count_upper+=1
        else:
            count_lower+=1
    print("Lower letter: "+str(count_lower))
    print("Upper letter: " + str(count_upper))

counter()