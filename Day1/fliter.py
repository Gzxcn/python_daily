# filter

def not_empty(string) :
    if isinstance(string,str) : 
        return string.strip()

string  = ["Admin ","",123," AD  ",None]

print(list(filter(not_empty,string)))

# 筛选出 质数 
l = list(range(100))
l = list(l[3:])

# 每项都除以小于它本身的数
def func(n):
    return lambda x : x % n == 1
# 生成一个奇数列（偶数一定是素数）
def func2() :
    n = 1
    while True:
        n = n + 2
        yield n 

def primes():
    it = func2()
    while True :
        n = next(it)
        yield n 
        it = filter(func(n),it)
# 打印前50项
# for i in primes():
#     if i < 50 :
#         print(i)

# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数
def is_palindrome(n) :
    str1 = str(n)
    str2 = str(n)[::-1]
    if str1 == str2 :
        return str1
string = [123456,12321,456654,23214]
print(list(filter(is_palindrome,string)))