sp = input().split()
sp = [i for i in sp if i.isalpha()]
sp.sort(key=len)
print(*sp, sep='\n')
