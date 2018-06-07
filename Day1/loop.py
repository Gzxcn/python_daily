
l = list(range(10))  # 创建 0-9的list序列

# 对 l 进行逐项求和
sum = 0
for x in l :
    sum += x
print(sum)


def one(**x):
    print(x)
    b = ()
    for a in x.values():
        b += (a,)
    print(b)

dect = {"one": 1, "two": 2, "three": 3}

one(**dect)
