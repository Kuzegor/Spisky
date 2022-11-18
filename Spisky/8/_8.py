keys = ['модель', 'цена', 'количество', 'размер', 'цвет', 'скидка']
values = ['XXLDude', 5678.55, 57, 'XXL', 'черный', '12%']
res = [key + ': ' + str(value) for key, value in zip(keys, values)]
print(*res, sep='\n')
