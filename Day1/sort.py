from itertools import chain
# sort 

# list里都是数字排序

number_list = [5,1,7,8,-10,50,-90,-5]
# print(sorted(number_list))

# 比较绝对值
# print(sorted(number_list,key=abs))

# 疑问  sorted 是否会改变原number_list顺序 
number_list.sort()
print(number_list)

sorted(number_list)
print(number_list)
# 输出的是  [5,1,7,8,-10,50,-90,-5] 说明 不改变 而是创建一个新的list   
# sort 方法会对原list 进行排序

# 对字符串排序 
string_list = ["Abs","Banana","Orange","cat","Cat"]
print(sorted(string_list)) # ['Abs', 'Banana', 'Cat', 'Orange', 'cat']

# 根据大小写排序
print(sorted(string_list,key=str.lower)) # ['Abs', 'Banana', 'cat', 'Cat', 'Orange']

# 疑问 混合list 如何排序
mix_list = [123,"abc",367,"dfe"]
# print(sorted(mix_list))  '<' not supported between instances of 'str' and 'int' 无法排序

#  可以对混合list 进行排序
def my_sort(list,number_key="",string_key=str.lower,reverse=False,first="number") :
    string = []
    number = []
    for value in list :
        print(value)
        if isinstance(value,str) :
            string.append(value)
        elif isinstance(value,int) :
            number.append(value)

    if number_key == "":
        sorted(number)
    else :
        sorted(number,key=number_key)

    sorted(string,key=string_key,reverse=reverse)
    l = []
    if first == "number" : 
        l = number + string
    else :
        l = string + number
    return l 
        

print(my_sort(mix_list,first="string"))