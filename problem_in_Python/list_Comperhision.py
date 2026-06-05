lis = [x*x for x in range(1,6) ]
print(lis)

num = [x for x in range(1,7) if x % 2 == 0]
print(num)

words = ["apple","banana","lichy"]
woed = [x.upper() for x in words ]
print(woed)

odd_even = [i*i for i in range(1,10) if i % 2 != 0]
print(odd_even)
