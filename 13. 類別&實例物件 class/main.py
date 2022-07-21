# 定義類別
class Student:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def introduce_self(self):
        print("哈囉，我是", self.name,"!\n我的身高", self.height, "公分，體重是",self.weight,"公斤。", sep="")
    
    def cal_BMI(self):
        return self.weight / (self.height/100)**2

# 建立物件
stu_lin = Student("小林", 175, 65)

# 取得現有物件參數
print(stu_lin.name)

# 使用物件內函式
stu_lin.introduce_self()
lin_bmi = stu_lin.cal_BMI()
print("我的BMI是:" , "{:.2f}".format(lin_bmi))

# 修改現有物件參數
stu_lin.weight = 80




