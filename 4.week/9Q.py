def alphabetic_order():
    words=input("Enter the words by putting '-' between them: ")
    names=words.split("-")
    ordered_names=sorted(names)
    for i in ordered_names:
        print(i,end="-")
alphabetic_order()