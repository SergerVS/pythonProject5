clients =int( input('Введите число участников :'))
S = 0 # заводим счетчик суммы
for client in range(clients) :
    age = int(input('Возраст :'))
    if age < 18 :
        S = S
    elif 18 <= age < 25 :
        S = S + 990
    elif age >= 25 :
        S = S + 1390
print('Стоимость билетов' ,S)
if clients >= 3 :
    S = S-(S / 100 * 10)
print('Стоимость билетов со скидкой : ' ,S)

