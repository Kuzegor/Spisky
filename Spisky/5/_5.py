st = list(input())
err = st.index('#')
del st[err]
sp = ''.join(st)
word = max(sp.split(), key=len)
print(sp, word, sep='\n')
