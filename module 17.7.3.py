money = int(input('Введите сумму вклада '))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
TKB = int(per_cent.get('ТКБ') * money/100)
SKB = int(per_cent.get('СКБ') * money/100)
VTB = int(per_cent.get('ВТБ') * money/100)
SBER = int(per_cent.get('СБЕР') * money/100)

diposit = [TKB, SKB, VTB, SBER]

print(diposit)
print('Максимальная сумма, которую вы можете заработать —', max(diposit), 'руб.')
