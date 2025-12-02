so  =list(map(int, input('nhap day so cua cach nau 1 dau cach:').split()))
max = so[0]
for i in so:
    if i>max:
        max=i
print('so lon nhat trong day la: ',max)
        