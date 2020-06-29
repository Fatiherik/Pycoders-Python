a=1
while a<=100:
    if a%3==0 and a%5==0:
        print("FIZZBUZZ")
    elif a%3==0:
        print("FIZZ")
    elif a%5==0:
        print("BUZZ")
    else:
        print(a)
    a+=1