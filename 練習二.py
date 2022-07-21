# 麥當勞點餐系統

# 介紹
# 此練習有基礎版本以及進階版本，進階版本包含了帳號系統以及付款確認

# 需求
# 帳號系統（進階）
# 顧客需要登入帳號才能點餐
# 主選單可以選擇登入或註冊帳號
# 帳號資料包含ID、姓名、稱呼(先生/小姐)、剩餘金額(點餐付款用)
# 帳號資料存放於文件檔案中(帳戶資料.csv)，須即時更新帳戶資料(新註冊帳戶、存款等)
# 登入後才可以進行點餐

# 點餐系統（基礎）
# 餐點內容部分以讀取文檔的方式取得資料(位於菜單資料夾中)
# 顯示主餐選項
# 點餐時詢問需要的主餐，使用者可以輸入主餐全名或是編號
# 接著詢問配餐
# 接著詢問是否要替換飲料（預設為可樂）
# 接著詢問是否要繼續點餐 
# 若結束點餐則計算金額並且告知顧客餐點內容物（每個品項）

# 付款（進階）
# 提示顧客帳戶剩餘金額並詢問是否充值
# 扣除剩餘金額

class MainDish:
    def __init__(self, name , price):
        self.name = name
        self.price = price

    def getName(self):
        return self.name 

    def getPrice(self):
        return int(self.price)

class Beverage:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def getName(self):
        return self.name 

    def getPrice(self):
        return int(self.price)
    
class Side:
    def __init__(self, name, items, price):
        self.name = name
        self.items = items
        self.price = price

    def getName(self):
        return self.name

    def getItems(self):
        return self.items

    def getPrice(self):
        return int(self.price)

class Meal:
    def __init__(self, mainDish, side, beverage):
        self.mainDish = mainDish
        self.side = side
        self.beverage = beverage
    
    def getPrice(self):
        return self.mainDish.getPrice() + self.side.getPrice() +self.beverage.getPrice()

    # 餐點名稱以及項目的描述
    def toString(self):
        sideItems = self.side.getItems()
        try:
            sideItemsStr = sideItems[0] + " " + sideItems[1]
        except:
            sideItemsStr = sideItems[0]
        return str("主餐:"+ self.mainDish.getName() + "\n" + "副餐:" + sideItemsStr + " 飲料:" + self.beverage.getName() + "\n" + "金額:$" + str(self.getPrice()))

# 這個函式要讀取菜單資料，格式化後回傳2D-list
def readCSVFile(filePath):
    resultList = []
    with open(filePath, 'r') as f:
        for line in f.readlines():
            cols = line.split(',')
            for i in range(len(cols)):
                cols[i] = cols[i].strip('$')
                cols[i] = cols[i].strip('\n')
            resultList.append(cols)
    return resultList


# 建立以字典為元素組合成的list(主餐、配餐、飲料), 回傳這三個list時按照主餐、配餐、飲料的順序
def buildMenuDict(mainDishList, sideDishList, beverageList):
    mainDishDicts = []
    sideDishDicts = []
    beverageDicts = []

    for row in mainDishList:
        pair = {
            "編號":row[0],
            "名稱":row[1],
            "金額":row[2]
        }
        mainDishDicts.append(pair)

    for row in sideDishList:
        pair = {
            "編號":row[0],
            "名稱":row[1],
            "金額":row[2],
            "配餐1":row[3],
            "配餐2":row[4],
        }
        sideDishDicts.append(pair)

    for row in beverageList:
        pair = {
            "名稱":row[0],
            "金額":row[1]
        }
        beverageDicts.append(pair)

    return mainDishDicts, sideDishDicts, beverageDicts

def comboOrder(mainDishDicts, sideDishDicts, beverageDicts):
    incorrectInput = True
    # 選擇主餐
    for i in mainDishDicts:
        print(i["編號"], i["名稱"], "$" + i["金額"])

    while incorrectInput:
        userInput = input("請選擇主餐: ")
        for i in mainDishDicts:
            if userInput == i["編號"] or userInput == i["名稱"]:
                mainDishOrdered = MainDish(i["名稱"], i["金額"])
                incorrectInput = False
                break

    # 選擇配餐
    incorrectInput = True
    for i in sideDishDicts:
        if i["配餐2"] == "N/A":
            print(i["編號"], i["名稱"], i["配餐1"], "$"+i["金額"])
        else:
            print(i["編號"], i["名稱"], i["配餐1"], i["配餐2"], "$"+i["金額"])
    while incorrectInput:
        userInput = input("請選擇配餐: ")
        for i in sideDishDicts:
            if userInput == i["編號"] or userInput == i["名稱"]:
                if i["配餐2"] != "N/A":
                    sideOrdered = Side(i["名稱"], [i["配餐1"], i["配餐2"]], i["金額"])
                else:
                    sideOrdered = Side(i["名稱"], [i["配餐1"]], i["金額"])
                incorrectInput = False
                break

    # 選擇飲料
    incorrectInput = True
    for i in beverageDicts:
        print(i["名稱"], "$"+i["金額"])
    while incorrectInput:
        userInput = input("請選擇飲料: ")
        for i in beverageDicts:
            if userInput == i["名稱"]:
                beverageOrdered = Beverage(i["名稱"], i["金額"])
                incorrectInput = False
                break

    # 組合成餐
    combo = Meal(mainDishOrdered,sideOrdered,beverageOrdered)
    return combo


# 點餐循環, 回傳餐點內容(Meal物件)組成的list
def ordering(mainDishDicts, sideDishDicts, beverageDicts):
    legalInput = True
    continueOrdering = True
    orderList = []
    while continueOrdering:

        if legalInput:
            orderList.append(comboOrder(mainDishDicts, sideDishDicts, beverageDicts))

        userInput = input("繼續點餐嗎？(是 y /否 n)")
        if userInput == "否" or userInput == "n":
            legalInput = True
            continueOrdering = False
        elif userInput == "是" or userInput == "y":
            legalInput = True
            continueOrdering = True
        else:
            legalInput = False

    return orderList

# 結帳, 計算金額, 告知餐點及內容物
def checkout(orderList):
    print('-'*20)
    print()
    # 告知目前餐點
    for i in orderList:
        print(i.toString())
        print()
    
    # 計算金額
    cost = 0
    for i in orderList:
        cost += i.getPrice()
    print('-'*20)
    # 告知金額
    print("總計: $",cost)

# 主程式
def main():
    # 1. 建構菜單
    # 讀取菜單資料並存入2D-list
    mainDishList = readCSVFile("./菜單資料/主餐.csv")
    sideDishList = readCSVFile("./菜單資料/配餐.csv")
    beverageList = readCSVFile("./菜單資料/飲料.csv")
    # 建構成菜單字典
    mainDishDicts, sideDishDicts, beverageDicts = buildMenuDict(mainDishList, sideDishList, beverageList)
    
    
    # 2. 點餐
    orderList = ordering(mainDishDicts, sideDishDicts, beverageDicts)
    

    # 3.結帳
    checkout(orderList)



if __name__ == "__main__":
    main()



