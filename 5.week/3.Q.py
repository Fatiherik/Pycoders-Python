from random import randint
from random import sample
list=[]
i=1
while i<101:
    list.append(randint(1000000000,9999999999))
    i+=1
first_winner=sample(list,2)[0]
second_winner=sample(list,2)[1]
print("winner numbers are: "+str(first_winner)+" and "+str(second_winner))
