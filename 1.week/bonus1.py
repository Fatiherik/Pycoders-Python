def libraryFine(d1, m1, y1, d2, m2, y2):

    if y1==y2 and m1==m2 and d1<=d2:
        fine=0
    elif y1==y2 and m1==m2 and d1>d2:
        fine = (d1-d2)*15
    elif y1==y2 and m1>m2:
        fine = (m1-m2)*500
    elif y1>y2:
        fine = 10000
    return fine

result = libraryFine(9, 8, 2015, 6, 6, 2015)

print(result)
