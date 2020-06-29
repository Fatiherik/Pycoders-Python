slip=int(input("enter how many index you will slip: "))
list_elements=[]

while True:
    elements =input("enter the elements of list: ")
    if elements == "q":
        break
    else:
        list_elements.append(elements)

new_order= list_elements[slip:]+list_elements[:slip]
print("The new order of the list is: "+' '.join(new_order))
