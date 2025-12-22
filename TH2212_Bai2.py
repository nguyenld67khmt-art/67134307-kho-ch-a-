a=float(input("nhap a: "))
b=float(input("nhap b: "))
c=float(input("nhap c: "))
max=a
min=a
if b>a:
    max=b
    if c>b:
        max=c
    else:
        max=b
else:
    max=a
if a>b:
    min=b
    if b>c:
        min=c
    else:
        min=b
else:
    min=a
print(f"so lon nhat la: {max}")
print(f"so nho nhat la: {min}")
