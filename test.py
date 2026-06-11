for i in range(1,6):
    for l in range(i,6):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    for k in range(i-1):
        print("*",end="")
    
    print()
for i in range(2,6):
    for l in range(i):
        print(" ",end="")
    for j in range(i,6):
        print("*",end="")
    for k in range(i+1,6):
        print("*",end="")
    
    print()
li = [3,45,3,36,6,42,67,4]
li.sort()
print(li)
lis = []
lis.append("j")
print(lis)

for _ in range(int(input())):
    name = input()
    score = float(input())
    s = [name,score]
    lis = []
    lis.append(s)
lis.sort()

print(lis)
for i in lis:
    if i[1][1] == i[2][1]:
        print(i[1][1])
        print(i[2][1])

d = {"name":"rashid","age":21}
print(d.keys())