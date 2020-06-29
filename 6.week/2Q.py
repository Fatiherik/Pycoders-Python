class Manifacture():
    model = []
    date = []
    price = []
    phone_book = []

    def __init__(self, model, date, price, phone_book):
        self.model = model
        self.date = date
        self.price = price
        self.phone_book = phone_book
        Manifacture.model.append(self.model)
        Manifacture.date.append(self.date)
        Manifacture.price.append(self.price)
        Manifacture.phone_book.append(self.phone_book)

    def phone_information(self):
        print("""model= {}
date={}
price={}
phone_book={}""".format(self.model, self.date, self.price, self.phone_book))

    def check_phone_book(self):
        if inquiry_name in self.phone_book.keys():
            print(inquiry_name+" is already in your phone_book")
        else:
            print(inquiry_name+" is not in your phone book")

    def add_phone_book(self):
        if add_name in self.phone_book.keys():
            print(add_name+" is already in your phone book, please enter another name")
        else:
            self.phone_book[add_name]=add_number
            print(add_name+" is added in your phone_book")

    def del_phone_book(self):
        if del_name in self.phone_book.keys():
            self.phone_book.pop(del_name)
            print(add_name + " is deleted from your phone_book")
        else:
            print(del_name +" is already not in your phone_book")

    #classmethod
    def phone_general():
        a = len(Manifacture.model)
        for i in range(a):
            print("""                        model={}
                        date={}
                        price={}
                        phone_book={}
    """.format(Manifacture.model[i], Manifacture.date[i], Manifacture.price[i], Manifacture.phone_book[i]))

    def price_sorted():
        Manifacture.price.sort()
        print(Manifacture.price)

def inquiry_screen():
    exp=input("""
      1= Display all phone information
      2= Display a phone information
      3= Sort phones price
      4= Others
      Please choose what you want to do:""")
    return exp

iphone = Manifacture("iphone", "2016", 900, {"ayse":"6 44 523 596"})
samsung = Manifacture("samsung", "2017", 800, {"ali":"6 44 512 897"})
huawei= Manifacture("huawei", "2018", 700, {"akif":"6 44 159 753"})

while True:
    reply = inquiry_screen()

    if reply == "1":
        Manifacture.phone_general()
    elif reply == "2":
        choose_phone=input("Write a phone name whose information you want to display: ")
        if choose_phone=="iphone":
            iphone.phone_information()
        elif choose_phone == "samsung":
            samsung.phone_information()
        elif choose_phone == "huawei":
            huawei.phone_information()
    elif reply == "3":
        Manifacture.price_sorted()
    elif reply == "4":
        reply1 = input("""
              1= Display phone book
              2= Check a name in phone book
              3= Add a name in phone book
              4= Delete a name in phone book
              Please choose what you want to do: """)
        reply2 = input("Write a phone name: ")

        if reply1 == "1":
            if reply2 == "iphone":
                print(iphone.phone_book)
            elif reply2 == "samsung":
                print(samsung.phone_book)
            elif reply2 == "huawei":
                print(huawei.phone_book)

        elif reply1 == "2":
            inquiry_name=input("Enter the name that you want to check: ")
            if reply2 == "iphone":
                iphone.check_phone_book()
            elif reply2 == "samsung":
                samsung.check_phone_book()
            elif reply2 == "huawei":
                huawei.check_phone_book()

        elif reply1 == "3":
            add_name= input("Enter the name that you want to add: ")
            add_number= input("Enter the number that you want to add: ")
            if reply2 == "iphone":
                iphone.add_phone_book()
            elif reply2 == "samsung":
                samsung.add_phone_book()
            elif reply2 == "huawei":
                huawei.add_phone_book()

        elif reply1 == "4":
            del_name= input("Enter the name that you want to delete: ")
            if reply2 == "iphone":
                iphone.del_phone_book()
            elif reply2 == "samsung":
                samsung.del_phone_book()
            elif reply2 == "huawei":
                huawei.del_phone_book()

inquiry_screen()