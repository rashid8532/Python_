from collections import Counter
# Enter your code here. Read input from STDIN. Print output to STDOUT
d = {"a":1}
f = {"b":2}
d.update(Counter(f))
print(d)
d.update(Counter({"a":2}))
print(d)
