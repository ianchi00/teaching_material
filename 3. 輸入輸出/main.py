# 輸出
print("---------- 輸出 ----------")
print("用print()輸出文字")
# sep 預設為「一個空白」，表示每個分隔的對象，在印出時中間的間隔符號
print("預設", "sep", "是一個空白格的話")
print("自訂", "sep", "是「 ＿ 」的話", sep="＿")
# end 預設為「換行符號 \n」，會於結尾時添加的字符
print("end預設為換行符號\\n，就會換行。")
print("更改end為「～」，就不會換行，而是在結尾會添加「～」。", end="～")
print("第二個print()。")
print("更改end為空", end="")
print("第二個print()。")

# 反斜線輸出特殊字元
# 換行
print("換\n行")
# 顯示單、雙引號
print("單引號\', 雙引號\"")

# 輸入
print("---------- 輸入 ----------")
# 使用input()接收使用者輸入
# 透過input()輸入的字符格式是str
input()
input_num = input("請輸入一個數字：")
print("你輸入的數字是：", input_num, "  類型：" ,type(input_num))
input_str = input("請輸入一個字串：")
print("你輸入的字串是：", input_str, "  類型：" ,type(input_str))



