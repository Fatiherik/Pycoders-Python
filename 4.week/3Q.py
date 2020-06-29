def perfect_number(n):
    list=[]
    for i in range(1,n+1):
        toplam = 0
        for y in range(1,i):
            if i%y == 0:
                toplam+=y
        if toplam==i:
            list.append(i)
    print(list)

perfect_number(1000)