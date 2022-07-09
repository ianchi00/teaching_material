# 數字資料格式 int, float
# int 整數 (包含正整數、負整數)
print("----- int 整數 -----")
student_number = 30
age = 18
minus_int = -18
print(student_number, age, minus_int)

# float 浮點數 (包含正、負)
print("----- float 浮點數 -----")
height = 174.5
weight = 65.3
loan = -51234.20
print(height, weight, loan)

# 運算
# 運算規則
# 如果整數的運算會產生小數點，結果就會轉換成浮點數
# 四則運算
print("----- 四則運算 -----")
add = age + 10
minus = age - 20
multiple = age * 10
divide = age / 10
print(add, minus, multiple, divide)

# 浮點數的運算即便沒有小數點，結果還是會是浮點數
loan+=0.2
print(loan)

# 特殊運算
print("----- 特殊運算 -----")
power = 10**3 # 次方
mod = 10%3  # 除法取餘數
takes_only_int = 10//3 # 除法取整數(無條件捨去)
print(power, mod, takes_only_int)

# 類型轉換
print("----- 類型轉換 -----")
# int()可以將資料轉成 int 類型
float_to_int = int(18.2993)
print(type(float_to_int), float_to_int)
int_to_float = float(18)
print(type(int_to_float), int_to_float)


