# 建立字典 
# 使用 {key(鍵) : value(值)}
menu = {"大麥克餐":130, "麥香雞餐":100, "麥克雞塊餐":110}
# 使用dict(key(鍵)=value(值))
menu_eng = dict(big_mac =  130, mc_chicken = 100, mc_nuggets = 110)
menu_2D_list = ["大麥克餐",130], ["麥香雞餐",100], ["麥克雞塊餐",110]
menu = dict(menu_2D_list)

# 透過key取得value
# []
print(menu["大麥克餐"])
print(menu["麥克雞塊餐"])
print(menu_eng["mc_chicken"])
# get()
print(menu_eng.get("big_mac"))
print(menu.get("麥香雞餐"))

print("-"*10)
# 修改Value
menu["大麥克餐"] = 1000
print(menu["大麥克餐"])

print("-"*10)
# 刪除單一內容
del menu["大麥克餐"]
print(menu)

# 刪除整個字典
del menu




