fibo=[0,1]
number=int(input("enter a number until which you want to find Fibonacci numbers: "))
while fibo[-1]+fibo[-2]<=number:
    fibo.append(fibo[-1]+fibo[-2])
print(tuple(fibo))