#if_statement

x= [3, -0.0629, 7, -3, 6, 2,-4, 0, -1, 0.345]

for i in range(10):
    if x[i] >0:
        print(x[i], "is a positive number.")
    else:
        print(x[i], "is a negative number.")



#now let us use random numbers

from random import randint
y= randint(1, 10)
if y >5:
    print(y, "is greater than 5")
elif y <5:
    print(y, "is less than 5")
else:
    print(y, "is equal to 5")


