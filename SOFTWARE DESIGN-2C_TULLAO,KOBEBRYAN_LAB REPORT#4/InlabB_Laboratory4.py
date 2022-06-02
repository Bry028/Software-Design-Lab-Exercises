def product(a,b):
    if (a==0 or b==0):
        return 0
    elif(a<b):
        return product(b,a)
    elif b!=0:
        return (a+product(a,b-1))

a=int(input("Enter number 1: "))
b=int(input("Enter number 2: "))
print("Product =", product(a,b))