list_elements=[]
while True:
    items = input("Enter the list items (to stop the program please enter 'q'): ")
    if items== "q":
        break
    else:
        list_elements.append(int(items))

leng=len(list_elements)
max_count=0
for i in list_elements:
    item_count=list_elements.count(i)
    if item_count>max_count:
        max_count=item_count
        max_rep_number=i

original_list=list_elements.copy()
list_elements.reverse()

max_distance=(leng-1-list_elements.index(max_rep_number))-original_list.index(max_rep_number) #(index of last max_rep_number)-(index of first max_rep_number)
print("Max Distance between the maximum repeated number ({}) is: {}".format(max_rep_number,max_distance))