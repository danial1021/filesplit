import sys

f = open("./source/a.txt", "r")
res = bytes(f.read(), 'utf-8')
print(res)
print(sys.getsizeof(res))

for i in (len(sys.getsizeof(res)), 77//4):
    print(res[:i])
