x=int(input("nhap bao nhieu so: "))
ds=[]
dss=[]
c=0
dsss=[]
for i in range (1,x+1):
    a=int(input(f'nhap so hang thu {i}: '))
    ds.append(a)
def is_armstrong(n):
    if n< 0:
        return False
    str_n = str(n)
    k = len(str_n)
    total = 0
    for digit in str_n:
        total += int(digit) ** k
    return total == n
for n in ds:
    b=is_armstrong(n)
    if b == True:
        d=n
        dsss.append(d)
        c += 1
print(f'so so armstrong la: {c}')
print('cac so armstrong la: ',(dsss))



