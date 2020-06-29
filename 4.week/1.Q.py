def prime_number(number):
    a=2
    while a<number:
        if number%a!=0:
            pass
        else:
            print(str(number) +" is a not prime number")
            break
        a+=1
    else:
        print(str(number) +" is a prime number")

prime_number(123)