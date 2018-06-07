# 闭包

def count() :
    a = [0] 
    def add():
        a[0] += 1 
        return a[0] 
    return add
f = count()

print(f())
print(f())
print(f())
print(f())
print(f())

