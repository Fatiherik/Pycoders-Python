kitchen=int(input("enter the monthly kitchen expense: "))
education=int(input("enter the monthly education expense: "))
clothing=int(input("enter the monthly clothing expense: "))
transportation=int(input("enter the monthly transportation expense: "))
total=kitchen+education+clothing+transportation
print("rate of kitchen expenses: "+str(kitchen/total))
print("rate of education expenses: "+str(education/total))
print("rate of clothing expenses: "+str(clothing/total))
print("rate of transportation expenses: "+str(transportation/total))