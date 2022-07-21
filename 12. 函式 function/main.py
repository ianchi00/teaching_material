# 定義函式 def
def print_line():
    print("----------------------")

# ()內填入參數
def print_line_with_length(len):
    print("-"*len)
# 參數預設值
def print_line_with_ten_or_else(len=10):
    print("-"*len)

# 給定參數名稱 (給定名稱的話會照名稱設定參數，不指定的話就是照順序)
def print_symbol_in_len(symbol, len):
    for i in range(len):
        print(symbol,end='')
    print()
print_symbol_in_len(len=10, symbol="^")

# 函數回傳值 return (終止函式程式並回傳)
def cal_sum(list_of_price):
    cost = 0
    for i in list_of_price:
        cost += i
    return cost

buy_list = [10,25,300,55]
cost = cal_sum(buy_list)
print(cost)

# 注意
# 函數傳入的參數是原本變數的 「複製」
# 所以改變他的複製版本不能改變原先的變數







