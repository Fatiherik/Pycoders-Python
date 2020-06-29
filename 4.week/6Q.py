def reading_number(n):
    first_digit=n//10
    second_digit=n%10
    first_dict = {1:"ten",2:"twenty",3:"thirty",4:"forty",5:"fifty",6:"sixty",7:"seventy",8:"eighty",9:"nighty"}
    second_dict = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
    print(first_dict[first_digit]+" "+second_dict[second_digit])

reading_number(28)