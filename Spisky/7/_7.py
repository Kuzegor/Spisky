vowels = 'àèå¸îóûışÿ'
st = input().split()
lst1 = [i for i in st if i[0] in vowels]
lst2 = [i for i in st if i not in lst1]
print(*lst1)
print(*lst2)
