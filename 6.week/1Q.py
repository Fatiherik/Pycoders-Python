class Manufactory():
    def __init__(self, id, brand, model, production_date,no):
        self.id = id
        self.brand = brand
        self.model = model
        self.production_date = production_date
        self.no = no

    def phone_information(self):
        print("""id= {}
brand= {}
model= {}
production_date= {}
no= {}""".format(self.id, self.brand, self.model, self.production_date, self.no))


iphone = Manufactory(101, "iphone", "7S", "01.01.2016", "5000")
samsung = Manufactory(201, "samsung", "J10", "01.01.2017", "5001")
huawei= Manufactory(301, "huawei", "X30", "01.01.2018", "5002")
lg= Manufactory(401, "lg", "P10", "01.01.2019", "5003")
xaomi= Manufactory(501, "xaomi", "Smart", "01.01.2020", "5004")

print(iphone.id)
samsung.phone_information()


