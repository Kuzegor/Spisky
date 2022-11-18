st = list(input())
err = [st.index(i) for i in st if st.count(i) > 2]
letter = st[err[0]]
st.remove(letter)
print(f'Bukva "{letter}" oshibochno povtoryaetsya {len(err) - 2} raz(a)')
print(f'Ispravlennoe slovo: {"".join(st)}' if len(err) == 3 else 'Ne mogy ispravit')
