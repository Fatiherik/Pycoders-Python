def least_common_multiple(n1,n2):
    common_divisor=[]
    min_number=min(n1,n2)
    for i in range(1,min_number+1):
        if n1%i==0 and n2%i==0:
            common_divisor.append(i)
    least=int((n1*n2)/max(common_divisor))
    print(least)

least_common_multiple(3,4)