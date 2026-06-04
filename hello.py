# a = int(input("Enter the first no. : "))
# b = int(input("Enter the second no. : "))
# operator = input("Enter the operator +, -, *, / : ")
# if operator == "+" : 
#     print(a+b)
# elif operator == "-" :
#     print(a-b)
# elif operator == "*":
#     print(a*b)
# elif operator == "/" :
#     print(a/b)

# ## Second problem

# num = int(input("Enter the input "))
# if num % 2 == 0:
#     print("No. is even",num)
# else :
#     print(num,"No. is odd")

# ## Third problem
# str = "Rashid"
# cout = 0
# vowel = "aeiouAEIOU"
# for i in range(0, len(str)):
#     for j in range(0, len(vowel)):
#         if str[i] == vowel[j]:
#             cout += 1
# print(cout)

## fourth 
arr = [88, 29, 90, 94, 64]
largest = arr[0]
second_largest = arr[0]
for i in range(len(arr)) :
    if arr[i] > largest :
        second_largest = largest
        largest = arr[i]
        
            
print(largest, "Is the largest in array")
print(second_largest, "Is the largest in array")

        