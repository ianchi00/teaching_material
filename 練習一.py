# 現階段我們掌握了字串、數字、運算、邏輯判斷以及迴圈的用法
# 可以開始寫一個基本的應用程式

# 麥當勞販售系統

# 需求
# 在最一開始顯示菜單
# 在文字提示後接受顧客輸入想要的餐的號碼 或是餐點名稱
# 每份餐點設有庫存數量（eg.3）
# 每點一份餐點就要回覆顧客該餐點是否有剩餘，若有則提示點餐成功，並從庫存扣除一份餐點
# 若輸入的數字或是餐點名稱不存在，則要告知該餐點不存在
# 輸入 “結束點餐” 販售系統終止，並計算最終應付金額

# 參考菜單 (不用一樣 可自行決定名稱價錢)
# 1. 大麥克餐 130
# 2. 麥香雞餐 100
# 3. 麥克雞塊餐 110
# 4. 雙層牛肉堡餐 120



# 程式內容

# 定義金額
big_mac_price = 130
mc_chicken_price = 100
mc_nuggets_price = 110
double_beef_price = 120
# 定義數量
big_mac_num = 3
mc_chicken_num = 3
mc_nuggets_num = 3
double_beef_num = 3

menu = """-----菜單-----
1. 大麥克餐 130
2. 麥香雞餐 100
3. 麥克雞塊餐 110
4. 雙層牛肉堡餐 120
-------------"""

# 互動部分
user_input = ""
cost = 0
print(menu)
while user_input != "結束":
    user_input = input("請輸入想要的餐點，若想結束點餐輸入結束: ")
    if user_input=="1" or user_input=="大麥克餐":
        if big_mac_num > 0:
            big_mac_num-=1
            cost+= big_mac_price
            print("點餐成功")
        else:
            print("此餐點無庫存")
    elif user_input=="2" or user_input=="麥香雞餐":
        if mc_chicken_num > 0:
            mc_chicken_num-=1
            cost+= mc_chicken_price
            print("點餐成功")
        else:
            print("此餐點無庫存")
    elif user_input=="3" or user_input=="麥克雞塊餐":
        if mc_nuggets_num > 0:
            mc_nuggets_num-=1
            cost+= mc_nuggets_price
            print("點餐成功")
        else:
            print("此餐點無庫存")
    elif user_input=="4" or user_input=="雙層牛肉堡餐":
        if double_beef_num > 0:
            double_beef_num-=1
            cost+= double_beef_price
            print("點餐成功")
        else:
            print("此餐點無庫存")
    else:
        if user_input == "結束點餐":
            break
        print("輸入錯誤 此餐點不存在")
# 結束點餐 計算金額
print("共計金額為:", cost)











