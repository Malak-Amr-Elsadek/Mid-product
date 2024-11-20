number=input("Enter a number:")
length=len(number)

if length %2 ==0:
    mid1=int(number[length//2-1])
    mid2=int(number[length//2])
    product=mid1*mid2
    print("Middle product is",product)
else:
    mid=int(number[length//2])
    print("Mid digit is",mid)