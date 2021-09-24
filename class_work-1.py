'''
1. Given two integer numbers return their product.
If the product is greater then 1000, then return their sum.
'''

n1 = 100
n2 = 200
product=n1*n2
if product>1000:
    sum=n1+n2
    print("Their sum is = ", sum)
else:
    print("Their product is = ", product)
print("End")

