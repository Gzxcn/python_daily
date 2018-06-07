# python 的类
# 申明方式  class 类名（继承的类名）
# __init__  ： 类的初始化方法 自带一个参数self
# 变量如果带2个_下划线的  表示为private 参数。 外部不可访问，若要访问需要一个对外的接口方法。

class Student(object) : 
    def __init__(self,name,grade) :
        self.__name = name
        self.__grade = grade 
    
    def get_grade(self) :
        return self.__grade
    

lisi = Student("lisi","高三")

print(lisi.get_grade())

# python 的多态

# 父类

class Person(object) : 
    __slots__ = ["name","age"]  # 会合理分配内存  减少cpu 负担，告诉类只有这几个参数，不使用字典类型，而是采用固定集合分配内存空间
    def __init__(self,name,age):
        self.name = name
        self.age = age 
    
    def doing(self) :
        if self.age > 10 and self.age < 40: 
            return "doing study"
        elif self.age < 10 :
            return "playing"
        else :
            return "working"


class Worker(Person) :
     def doing(self):
        return "always working "

worker = Worker("王五",20)
print(worker.doing())
        

