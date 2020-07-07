#functions

def fun1():
    print("Hello World")

fun1()


def fun2(x):
    y=2+x
    print(y)

fun2(2)
fun2(3)


def fun3(x, y):
    if x>y:
        print("x > y")
    elif x<y:
        print("x < y")
    else:
        print("x = y")

fun3(1, 3)
fun3(3, 1)
fun3(1,1)


#function call other function
#function 1
def sum_l(i):
    print(sum(i))

#function 2
def list_s(n):
    sum_l(range(n, 10))

list_s(5)

