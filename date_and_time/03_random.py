import random

print(random.randint(1,8))


names = ["Ali", "Ahmed", "Sara"]

print(random.choice(names))

print(round(random.random()*10))

num = [1,2,3,4,5]
random.shuffle(num)
print(num)

for i in range(5):
    print(random.randint(1,100))