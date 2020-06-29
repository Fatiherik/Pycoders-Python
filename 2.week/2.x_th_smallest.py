list_elements=[]
while True:
    items = input("Enter the list items (to stop the program please enter 'q'): ")
    if items== "q":
        break
    else:
        list_elements.append(int(items))

x_th=int(input("Which number do you want to know as Xth smallest number in the list?: "))
list_elements.sort()
x_th_smallest=list_elements[x_th-1]

if x_th%10==1:
    suffix="st"
elif x_th%10==2:
    suffix="nd"
elif x_th%10==3:
    suffix="rd"
else:
    suffix="th"

print(str(x_th)+suffix+" smallest element in the given list is "+ str(x_th_smallest))
