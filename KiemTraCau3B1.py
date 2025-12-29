n=int(input("nhap bao nhieu so: "))
ds=[]
dscan=[]
for i in range (1,n+1):
    a=int(input(f'nhap so hang thu {i}: '))
    ds.append(a)
for so in ds:
    if so % 6 ==0:
        dscan.append(so)
print(dscan)
    
