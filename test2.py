def sum1(m):
    if m == 0:
        return 0

    return sum1(m - 1) + m

sum2 = sum1(10)
print(sum2)