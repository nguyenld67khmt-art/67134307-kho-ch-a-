w=float(input("nhap chieu dai hinh chu nhat: "))
h=float(input("nhap chieu rong hinh chu nhat: "))
w=float(input("nhap do dai canh 1 hinh chu nhat: "))
h=float(input("nhap do dai canh 2 hinh chu nhat: "))
while w <= 0 or w>=100 :
    print("khong hop le")
    w=float(input("nhap do dai canh 1 hinh chu nhat: "))
while h <= 0 or h>=100 :
    print("khong hop le")
    h=float(input("nhap do dai canh 2 hinh chu nhat: "))
S=w*h
P=(w+h)*2
print(f"Chu vi hinh chu nhat la: {P:.2f}")
print(f"Dien tich hinh chu nhat la: {S:.2f}")