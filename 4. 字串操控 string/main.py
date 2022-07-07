# 字串由''或是""包覆
print('這是字串')
print("這是字串")
# 單引號雙引號可交互使用
print("這是'字串'")
print('這是"字串"')
# 多行字串 三個單引號或雙引號包覆
multiple_lines_of_str = """這裡是
很多行
字串"""
print(multiple_lines_of_str)

print("="*10)
# 取得字元char
cafe = "LOUISA Coffee"
print("index 5: " , cafe[5])
print("index 6: ",  cafe[6])
print("index -1: ", cafe[-1]) # 最後一個字元

print("="*10)
# 取得字串
print(cafe[:])
print(cafe[:5])
print(cafe[6:])
print(cafe[3:10])

print("="*10)
# 取得字串長度 str.len()
print(len(cafe))

print("="*10)
# 替換字串內容 str.replace()
name = "安＿妮雅"
print(name.replace("＿", " "))

print("="*10)
# 去除頭尾字符 str.strip()
name = " &&&" + name + " "
print(name)
name = name.strip()
print(name)
name = name.strip("&")
print(name)

print("="*10)
# 搜尋字串 str.find()
script = """Python 設計哲學：
優美優於醜陋。明瞭優於隱晦。
簡單優於複雜。複雜優於凌亂。
扁平優於巢狀。稀疏優於稠密。
可讀性很重要。"""
print("複雜: ", script.find("複雜"))
print("優於: ", script.find("優於"))

print("="*10)
# 判斷開頭或結尾字串 str.startswith()
print("start with \"Python\": ", script.startswith("Python"))

print("="*10)
# 字母大小寫轉換
script = 'A "HELLO WORLD!" program is generally a Computer Program that outputs or displays the message'
print(script)
print(script.upper())
print(script.lower())
print(script.title())

print("="*10)
# 分割字串成列表 split()
name = "LOUISA Coffee"
name_list = name.split(' ')
print(name_list)
menu = "Americano|Latte|Cappuccino|Caramel|Hazelnut"
menu_list = menu.split()
print(menu_list)







