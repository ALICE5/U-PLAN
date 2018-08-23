# x = abs(-10)
# print(x)


def my_abs(x):
    if x >= 0 :
        return x
    else:
        return -x

result = my_abs(-100)
print(result)




def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def dev(x,y):
    return x/y



def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

print(fact(10))

def func1(a):
    print(max(a))
    print(min(a))

func1([1,2,3,4,5,6,7,8,9,0,100])

