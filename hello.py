n = int(input())
j = None
if n < 1 or n > 150 :
        print("Invalid")
else :
        for i in range(n):
            j += str(i)
print(j)