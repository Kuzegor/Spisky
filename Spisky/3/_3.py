st = [int(i) for i in input().split(',')]
lst_odd = [i for i in st if i % 2 != 0]
lst_even = [i for i in st if i % 2 == 0]
print(*lst_odd)
print(*lst_even)
