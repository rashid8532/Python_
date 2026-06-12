from collections import OrderedDict
d = OrderedDict()
d["A"] = 1
d["B"] = 2
d["C"] = 3

print(d)
for i , j in d.items():
    print(i , j)

d.move_to_end("A")
print(d)
lis = [1,2,3,4,5]
print(lis[0 : -1])

from collections import OrderedDict
# Enter your code here. Read input from STDIN. Print output to STDOUT
d = OrderedDict()
N = int(input())
for i in range(N):
    parts = input().split()
    item = parts[0:-1]
    price = parts[-1]
    d[item] = price
print(d)
