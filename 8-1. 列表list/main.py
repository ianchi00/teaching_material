# 建立列表
fruit = ['蘋果','香蕉','橘子']
lottery_num = [19,24,17,22,26]
random_objects = ["str", "int", 66, ["這是","另一個list"], {'這是','set'}]
print(type(fruit), "fruit: ", fruit)
print(type(lottery_num), "lottery_num: ", lottery_num)
print(type(random_objects), "random_objects: ", random_objects)

print('='*10)
# 打印列表
for i in fruit:
    print(i)

print('='*10)
# 檢查列表長度
print("lottery_num:", len(lottery_num))

print('='*10)

# 添加、修改列表元素
# 讀取列表元素
print("fruit的第1個元素", fruit[0])
print("fruit的第2個元素", fruit[1])
print("lottery_num的第2到第4個元素", lottery_num[1:4])

print('='*10)
# 修改列表元素
fruit[0] = "青蘋果"
print(fruit)

print('='*10)
# 使用內建函式append 添加單一元素至列表
print(lottery_num)
lottery_num.append(10)
print(lottery_num)

print('='*10)
# 使用內建函式insert 插入單一元素至列表
fruit.insert(1,"芭樂") # 在index為1的地方插入元素"芭樂"
print(fruit)

print('='*10)
# 使用內建函式expend 添加另一個列表至後方
lottery_num.extend(fruit)
print(lottery_num)

print('='*10)
# 刪除列表元素
# del 透過index指定要刪除的元素
nums = [0,1,2,3,4,5,6,7,8,9]
print(nums)
del nums[3]
print(nums)
del nums[3:6]
print(nums)

print('='*10)
# 內建函式remove 尋找要刪除的元素 注意：remove只會刪除第一個找到的項目
staff = ["員工1","員工2","員工3","員工4","員工3"]
print(staff)
staff.remove("員工3")
print(staff)

print('='*10)
# 內建函式clear 清空列表所有內容
staff.clear()
print(staff)





print('='*10)
# 注意：使用內建函式時，更改的元素為自身，所以不需要設定回傳的值；相對的使用運算子時，需要設定回傳的元素才能儲存資料
# 使用運算子添加單一、多個元素
lottery_num += [20]
print(lottery_num)
lottery_num += [30,40,50]
print(lottery_num)











