user_name=input("enter your user name (3-18 characters): ")
while str.isalpha(user_name)==False:
    print("user name can not include a number")
    user_name = input("enter your user name (3-18 characters): ")

password=input("enter yout password (6-12 characters): ")
while len (password)<6 or len(password)>12:
        print("the password should not be less than 6 or more than 12")
        password = input("enter yout password (6-12 characters): ")

print(user_name)
print(password)


