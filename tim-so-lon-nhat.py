a=int(input('Nhap so dau tien: '))
b=int(input('Nhap so thu hai: '))
c=int(input('Nhap so thu ba: '))
if a > (b and c):
    print("so lon nhat la:",a)
elif b>(a and c):
    print("so lon nhat la",b)
else:
    print("so lon nhat la",c)
