class school():

    sayac=0
    mat=[]
    fizik = []
    turkce = []
    total=[]

    def __init__(self, tc, isim, soyisim, mat_not, fizik_not, turkce_not):
        self.tc = tc
        self.isim = isim
        self.soyisim = soyisim
        self.mat_not = mat_not
        self.fizik_not = fizik_not
        self.turkce_not = turkce_not
        school.sayac=school.sayac+1
        if self.mat_not>50:
            school.mat.append(self.isim)
        if self.fizik_not>50:
            school.fizik.append(self.isim)
        if self.turkce_not>50:
            school.turkce.append(self.isim)

        if (self.mat_not + self.fizik_not + self.turkce_not) / 3 > 50:
            school.total.append(self.isim)

ahmet = school("1111111", "ahmet", "yener",70,60,40)
mehmet = school("2222222", "mehmet", "basaran", 80,60,20)
ali= school("3333333", "ali", "koc",10, 20, 30)

print(school.sayac)
print(school.mat)
print(school.fizik)
print(school.turkce)
print(school.total)