principal=int(input("enter the principal amount: "))
time=int(input("enter the period of time (year): "))
interest_rate=int(input("enter the rate of interest: "))
total_interest=principal*time*(interest_rate/100)
print("total interest: "+str(total_interest))
print("average monthly interest: "+str(total_interest/(12*time)))
print("average daily interest: "+str(total_interest/(360*time)))
print("total balance: "+str(total_interest+principal))

