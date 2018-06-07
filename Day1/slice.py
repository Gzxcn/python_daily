# 切片

s = ["milk","banana","apple","orange"]

# 取上面前3个数据

# 方法1 
s1 = [s[0],s[1],s[2]]
print(s1)

# 方法2 
n = 3
s2 = []
for i in range(n):
    s2.append(s[i])
print(s2)

# 方法3 利用切片

s3 = s[0:3]  # 从下标0开始 往右算3个 为0 1 2 
s4 = s[:3]   # 若从0开始 省略0

ss = list(range(100))

ss1 = ss[:10:2] # 前10个每2个取1个

ss2 = ss[::5] # 每5个取1个
ss3 = ss[::-1] # 倒叙
print("ss3",ss3) 

# 针对string做切片
string = "Hello World"
slice_string = string[:5]
print(slice_string)

# 切片： list切片后为list  tuple切片后仍是tuple  string切片后是string