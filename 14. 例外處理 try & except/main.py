# 使用try以及except避免程式終止
user_input = input("輸入一個數字")
try:
    print(int(user_input)**2)
except:
    print("輸入內容無法轉換成數字")

# 套用except類型
num_list = [0, 1, 2]
user_input = input("輸入一個數字")
list_index = input("輸入一個list欄位(數字)")
try:
    num_list[int(list_index)] = int(user_input)
except ValueError:
    print("輸入內容無法轉換成數字")
except IndexError:
    print("要修改的List欄位不存在")
print(num_list)

# 使用else
num_list = [0, 1, 2]
user_input = input("輸入一個數字")
list_index = input("輸入一個list欄位(數字)")
try:
    num_list[int(list_index)] = int(user_input)
except ValueError:
    print("輸入內容無法轉換成數字")
except IndexError:
    print("要修改的List欄位不存在")
else:
    print(num_list)
