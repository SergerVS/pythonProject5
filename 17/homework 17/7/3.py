per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money_in=int(input('Введите сумму вклада'))
deposit=[]
deposit.append(per_cent['ТКБ']*money_in/100)
deposit.append(per_cent['СКБ']*money_in/100)
deposit.append(per_cent['ВТБ']*money_in/100)
deposit.append(money_in/100*per_cent['СБЕР'])
print(deposit)
print('максимальный депозит',max(deposit))
print('минимальный депозит',min(deposit))

