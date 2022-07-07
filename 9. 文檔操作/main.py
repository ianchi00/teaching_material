# 單行讀取/寫入
from cmath import e


with open('./7. 文檔操作/單行讀寫測試.txt','w') as f:
    f.write('如果可以')

with open('./7. 文檔操作/單行讀寫測試.txt', 'r') as f:
    file_str = f.read()
    
print(file_str)

print('='*10)
# 多行讀取/寫入
lyrics = [
'妳的聲音 解開了故事的謎語',
'落下一萬年的約定',
'大樹下的妳 紅色圍巾 手心裡捧的雨',
'哭了笑了 除了妳還是妳',
'',
'我們 如果又一次錯過 不敢牽起妳的手',
'我會多麼寂寞 等待紅線來的時候',
'',
'如果可以 我想和妳回到那天相遇',
'讓時間停止 那一場雨',
'只想擁抱 妳在身邊的證據 吻妳的呼吸',
'一眨眼 一瞬間 妳說好就是永遠',
'不會變'
]


with open('./7. 文檔操作/多行讀寫測試.txt', 'w') as f:
    for line in lyrics:
        f.writelines(line+'\n')

with open('./7. 文檔操作/多行讀寫測試.txt', 'r') as f:
    list_of_lyrics = f.readlines()

for i in list_of_lyrics:
    print(i, end='')









