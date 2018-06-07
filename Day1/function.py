
def count(a,b) :
    sum = 0 
    sum = a + b  
    return sum 
print(count(4,5))

# 递归 
def my_count(a,b,stop,n=0) :
    # print(a,b,n)
    sum = a + b 
    n += 1
    b = b + 1
    if sum < stop : 
        return my_count(sum,b,stop,n)
    else : 
        return n  

print(my_count(0,1,99))

# 带* 传入 表示传入参数数量不确定  php 中有类似的 function cacl(a...){}
def calc(*number) :
    sum = 0 
    for i in number :
        sum += i 
    return sum 

num = [11,22,33]
# 变量前 带*  将指定变量名下所有参数都传入方法内
print(calc(*num))

print(calc(1,2))


# 可变参数传入 

def login_user(name,age,**keyword) :
    return {'name':name,'age':age,'keyword':keyword}

print(login_user("admin","123",descr="123",others="123"))


# 直接收关键字下的参数

def keyword_Receive(name,age,*,job,area) :
    return {'name': name, 'age': age, 'job': job, "area": area}

print(keyword_Receive("123","45",job="php",area="xiamen"))

# 关于 位置参数问题 

# 1. *号前  a b 代表位置参数  *号后  c d 代表关键字参数  
def position1(a,b,*,c,d):
    return(a,b,c,d)

print(position1(1, 2, c=3, d=4)) 

# 2. *号前 与上面相同  a b 为位置参数 *c 代表 除了 a b 赋值后 且 不是关键字参数的其他参数都赋值给c  *后的仍为关键字参数 
def position2(a,b,*c,d,e):
    return(a,b,c,d,e)

print(position2(1,2,3,4,5,6,7,d=8,e=9))

# 3. 大致情况与2相同， **e 是将其余所有都已字典的的形式赋值给e
def position3(a,b,*c,d,**e):
    return (a, b, c, d, e)
print(position3(1,2,3,4,5,d=6,e=7,f=8,g=9))







