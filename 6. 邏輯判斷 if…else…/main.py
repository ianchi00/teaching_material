# if
tea_price = 45
if tea_price < 60:
    print("買")

print("="*10)

# if...else...
tea_price = 70
if tea_price < 60:
    print("買")
else:
    print("不買")

print("="*10)

# if...elif...else...
tea_price = 65
if tea_price < 60:
    print("買")
elif tea_price < 70:
    print("考慮一下")
else:
    print("不買")


print("="*10)

# 使用pass不執行任何動作
tea_price = 65
if tea_price < 60:
    print("買")
elif tea_price < 70:
    pass
    print("pass")
else:
    print("不買")

print("="*10)

# 內含多個判斷式
tea_price = 55
cash_in_hand = 50
if tea_price < 60:
    print("想買...", end=" ")
    if cash_in_hand >= tea_price:
        print("購買成功！！")
    else:
        print("沒錢...")
elif tea_price < 70:
    pass
else:
    print("不想買...")

print("="*10)

# and & or  
cash_in_hand = 50
tea_price = 50
if tea_price <= 60 and cash_in_hand > tea_price:
    print("想買而且有錢買！")
elif tea_price > 60 or cash_in_hand < tea_price:
    print("太貴或是沒錢買...")
else:
    pass



