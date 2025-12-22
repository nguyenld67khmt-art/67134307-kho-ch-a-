a=float(input("nhap do dai canh a: "))
b=float(input("nhap do dai canh b: "))
c=float(input("nhap do dai canh c: "))
while a+b <= c or a+c <= b or b+c <= a:
    print("khong hop le, nhap lai cac gia tri")
    a=float(input("nhap do dai canh a: "))
    b=float(input("nhap do dai canh b: "))
    c=float(input("nhap do dai canh c: "))
P=a+b+c
X=P/2
S=(X*(X-a)*(X-b)*(X-c))**0.5
print(f"Chu vi cua tam giac la: {P:.2f}")
print(f"Dien tich cua tam giac la: {S:.2f}")
