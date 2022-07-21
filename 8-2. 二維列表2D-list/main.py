# 二維列表
# 訣竅：操作時可以想像成表格的樣子

# 建立二維列表
staff_info = [
    ["s38619", "宋世傑", 25, 25000],
    ["s38620", "林常威", 27, 26000],
    ["s38621", "陳來福", 29, 26500]
]
print(staff_info)

# 取得二維列表
print(staff_info[0][1])

print('='*10)
# 打印二維列表
# 注意：取得二維列表時，第一個取得的元素會是最外圈取進來的元素(每一筆資料)
for row in staff_info:
    for col in row:
        print(col, end=' ')
    print()

print('='*10)
# 使用index取得並且打印資料
for i in range(len(staff_info)):
    id = staff_info[i][0]
    name = staff_info[i][1]
    age = staff_info[i][2]
    wage = staff_info[i][3]
    print("ID:", id, "| 名字:", name,"| 年齡:", age, "| 薪水:", wage)


