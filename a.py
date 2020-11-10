import sys

f = open("./source/a.txt", "r")
res = bytes(f.read(), 'utf-8')

# res = '나는반딧불'.encode()
print(sys.getsizeof(res))

print(len(res))
a = round((len(res)//4))

c1 = res[:a]
c2 = res[a:a*2]
c3 = res[a*2:a*3]
c4 = res[a*3:]

print(c1, c2, c3, c4)
print(sys.getsizeof(c1),sys.getsizeof(c2),sys.getsizeof(c3),sys.getsizeof(c4))

print((c1+c2+c3+c4).decode())