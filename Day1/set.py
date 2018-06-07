# 声明 set   

my_set = set(list(range(10)))
print(my_set)

# set 是一个无序且不重复的 集合 

my_set.add(20)  # 添加元素
print(my_set)

my_set.remove(20) # 删除元素 传入值为 set内部的值  如果不存在 会报错(KeyError:xx)
print(my_set)

# set 可用于处理 数学上  交集和并集问题 

a = set([1,2,3])
b = set([2,4,5])

print(a|b)
print(a&b)

# 对于字符串的replace方法

s = "abc" 
print(s)  # 值为 abc
print(s.replace("a","A")) # 值为 Abc 
print(s) # 值为 abc 

# 如果要修改 abc 的值 可用另一个变量承接  或者 将 string 转化为list 在通过list 修改 
a = s.replace("a", "A")
print(a)
c = list(s)
c[0] = 'A'
print("".join(c))

# 可以将 其转化为切片 在拼接
d = "A" + s[1:]
print(d)
 


