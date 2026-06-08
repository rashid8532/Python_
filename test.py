n = int(input())
s = set(map(int,input().split()))
N = int(input())
for i in range(N):
    x = input()
    y = x.split()
    if y[0] == "pop":
        s.pop()
    elif y[0] == "remove":
        if int(y[1]) in s:
            s.remove(int(y[1]))
    elif y[0] == "discard" :
        s.discard(int(y[1]))

print(sum(s))

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
s = set(map(int,input().split()))
N = int(input())
for i in range(N):
    x = input()
    y = x.split()
    if y[0] == "pop":
        s.pop()
    elif y[0] == "remove":
        if int(y[1]) in s:
            s.remove(int(y[1]))
    elif y[0] == "discard" :
        s.discard(int(y[1]))

print(sum(s))  
