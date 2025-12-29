a=float(input("Nhap he so a: "))
b=float(input("Nhap he so b: "))
if a==0 and b==0:
    print(f'Phuong trinh vo nghiem')
if a==0 and b != 0 :
    print(f'Phuong trinh vo so nghiem')
if a != 0:
    x = -b/a
    print(f'phuong trinh {a}x + {b} = 0, co nghiem la {x:.2f}')
