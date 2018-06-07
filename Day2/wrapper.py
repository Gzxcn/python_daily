import time
# 装饰器

# def log(func):
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper

# @log
# def time() :
#     print("2018-6-7")

# time()


def metric(func):
    def wrapper(*args, **kw):
        print("方法名：", func.__name__, time.asctime(time.localtime(time.time())))
        return func(*args, **kw)
    return wrapper


@metric
def sum_number(list) :
    sum = 0
    for i in list:
        sum = sum + i 
    print(sum)

l = list(range(5))
sum_number(l)

