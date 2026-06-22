a = "geeks"
b = "seegk"
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            a = a[:i-1] + a[i+1:]
print(a)
