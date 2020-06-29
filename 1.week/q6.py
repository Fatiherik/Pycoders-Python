number=int(input("enter a number: "))
a=2
prime=True
while a<number:
    if number%a!=0:
        pass
    else:
        print("it is a not prime number")
        prime=False
        break
    a+=1
if prime:
    print("it is a prime number")
