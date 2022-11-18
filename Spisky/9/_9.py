lst = input().split(', ')
grades = [int(i) for i in lst[1].split()]
avg = sum(grades) / len(grades)
print(f'{lst[0]}, средний балл: {avg:.2f}')
