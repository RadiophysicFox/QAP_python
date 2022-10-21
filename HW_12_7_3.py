money = int(input("Введите сумму, которую планируете положить под проценты:"))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
per_cent_values = list(per_cent.values())
deposit = []
for i in range(0, len(per_cent_values)):
    deposit.append(int(per_cent_values[i] * money / 100))
print("deposit =", deposit)
print("Максимальная сумма, которую вы можете заработать —", max(deposit))
