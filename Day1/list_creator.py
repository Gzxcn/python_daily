# 列表生成式 & 生成器

# 生成 [1x1,2x2,3x3,...,10x10]的列 

l = list(range(10))
l1 = []
for x in l :
    l1.append(x*x)
print(l1)

# 简化写法
l2 = [x*x for x in l ]
print(l2)

# 简化写法中 带条件判断  
l3 = [x*x for x in l if x % 2 == 0] #偶数保留
print(l3)

# 多个参数的简化写法  每个会互相组合  char1的每一个字符与char2的每个字符组合
char1 = "helloworld"
char2 = "dlrowolleh"
l4 = [c1 + c2 for c1 in char1  for c2 in char2]
print(l4)

# 字典中生成列表 类似于 php 的foreach方法
d={
    "apple" : "11",
    "banana" : "12",
    "orange" : "7"
}
l5 = [k + "=>" + v for k,v in d.items()]
print(l5)


# 练习  L1 = ['Hello', 'World', 18, 'Apple', None] 转化为小写
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = []
for v in L1 :
    if isinstance(v, str):
        L2.append(v.lower())
    else :
        L2.append(v)
print(L2) 
        