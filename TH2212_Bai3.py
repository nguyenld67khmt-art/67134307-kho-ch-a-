a=input("nhap a: ")
b=input("nhap b: ")
c=input("nhap c: ")
def solonnhat(a,b,c):
    max=a
    if b>max:
        max=b
    if c>max:
        max=c
    return max
lonnhat=solonnhat(a,b,c)
def sonhonhat(a,b,c):
    min=a
    if b < min :
        min=b
    if c < min :
        min=c
    return min
nhonhat=sonhonhat(a,b,c)
print(f"so lon nhat la: {lonnhat}")
print(f"so nho nhat la: {nhonhat}")

    
                
    