n = int(input('Введите количество монет '))
orel = 0
reshka = 0
for i in range(n):
    c = int(input())
    if c == 1:
        orel+=1
    elif c == 0:
        reshka+=1
if orel > reshka:
    print('Нужно перевернуть',orel, 'монет')
else:
    print('Нужно перевернуть',reshka, 'монет')  
