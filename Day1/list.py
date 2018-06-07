
print("hello world\n")

# 计算list序列长度
l = [1,2,4,5]
print(len(l),"\n")

# 按下标获取值
print(l[1],"\n")

# 遍历
for key in l :
   print(key)

# list 添加数据和移出数据 
l.append(10)  # 从list 尾部添加数据
print(l)

l.insert(7,5) # 从list 指定位置添加数据
print(l)

l.pop() # 移出指定位置数据 默认 最后一项

l[2] = 1  # 修改指定位置 值 且下标不能超出现有长度（IndexError: list assignment index out of range）







