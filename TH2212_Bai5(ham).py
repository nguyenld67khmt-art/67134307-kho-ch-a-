def tongtu(A):
    a=0
    for i in range (1,A+1):
        a = a + i
    return a
X= tongtu(5)
def tongmau(A):
    b=0
    for i in range (1,A+1):
        b = b + i*2
    return b
Y= tongmau(5)
c=X/Y
print("dap an cua day so nay la: ",c)

