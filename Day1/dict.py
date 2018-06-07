# dict  字典   
score = {
    "John" : 100,
    "Jack" : 85 ,
    "Rose" : 70
}

print(score["John"])

# # 修改 dict 值
score["John"] = 1
print(score)

# 获取dict 值
print(score.get("John"))  
print(score["John"])
print(score.get("John"),1) # 如果存在 score['John'] 返回 1（可自定）
# dict 删除元素  类似于 list 
score.pop("John")
print(score)

# 注 ： dict 与 list 相比 ： 插入和查询速度较快。 不像list 会根据list的长度 效率变低 