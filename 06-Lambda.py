#lambda, the anonymous function
y= lambda x: x**2
print (y(3))

#this is a function
def fun1(i):
    return i+3

print(fun1(3))

#this lambda is the same as fun1
print((lambda i:i+3)(3))

#print only even numbers in the list
a = [1, 2, 3, 4, 5]
ev = list(filter(lambda x: x%2==0, a))
print(ev)

#sub 2
c = [1, 2, 3, 4, 5]
s = list(map(lambda x: x-2, c))
print(s)

