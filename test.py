from collections import defaultdict

freq = defaultdict(list)
data = [
    ("Python", 10),
    ("Java", 20),
    ("Python", 30),
    ("C++", 40),
    ("Java", 50),
    ("Python", 60)
]

for name ,points in data:
    freq[name].append(points)
print(freq)
d = dict(freq)
for name,points in freq.items():
    print(name,sum(points))
    