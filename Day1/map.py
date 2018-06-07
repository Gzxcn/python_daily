from functools import reduce

l = list(range(10))

def count(x) :
    return x * x 

new_l = list(map(count,l))
print(new_l)

# reduce 
def add(*number) :
    sum = 0
    for n in number :
        sum += n 
    return sum 
print(reduce(add,[11,23,4,5]))


# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：

def prod(*number) :
    product = 1 
    for n in number :
        product *= n 
    return product

pl = list(range(6))
pl.remove(0)
print(reduce(prod,pl))
