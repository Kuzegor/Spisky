st = [int(i) for i in input().split()]
lst = [i for i in st if st.count(i) > 1]
print(*lst)
