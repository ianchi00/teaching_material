# for 迴圈

# str
for i in '一二三':
    print(i)

print('='*10)
# list
for i in ['一','二','三']:
    print(i)

print('='*10)
# set
for i in {'一','二','三'}:
    print(i)

print('='*10)
# dict
for i in {'一':1,'二':2,'三':3}:
    print(i)

print('='*10)
# range()
for i in range(10):
    print(i, end='')

print('='*10)
# while 迴圈
index = 0
while index < 10:
    print(index)
    index+=1

print('='*10)
# break
for i in range(10):
    if i == 7:
        print(i, ":i==7, 終止迴圈")
        break
    if i % 2 == 0:
        print(i,  ":是偶數")

print('='*10)
# continue
for i in range(10):
    if i == 4:
        print()
        continue
    print("i:",  i)

    
