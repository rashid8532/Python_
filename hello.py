# # a = int(input("Enter the first no. : "))
# # b = int(input("Enter the second no. : "))
# # operator = input("Enter the operator +, -, *, / : ")
# # if operator == "+" : 
# #     print(a+b)
# # elif operator == "-" :
# #     print(a-b)
# # elif operator == "*":
# #     print(a*b)

# # elif operator == "/" :
# #     print(a/b)

# # ## Second problem

# # num = int(input("Enter the input "))
# # if num % 2 == 0:
# #     print("No. is even",num)
# # else :
# #     print(num,"No. is odd")

# # ## Third problem
# # str = "Rashid"
# # cout = 0
# # vowel = "aeiouAEIOU"
# # for i in range(0, len(str)):
# #     for j in range(0, len(vowel)):
# #         if str[i] == vowel[j]:
# #             cout += 1
# # print(cout)

# # ## fourth 
# # arr = [88, 29, 90, 94, 64]
# # largest = arr[0]
# # second_largest = arr[0]
# # for num in arr :
# #     if num > largest :
# #         second_largest = largest
# #         largest = num
# #     elif num > second_largest and num != largest :
# #         second_largest = num
            
# # print(largest, "Is the largest in array")
# # print(second_largest, "Is the largest in array")

# # ## sixth problem 
# # positive = 0
# # negative = 0
# # zeros = 0

# # arr2 = [5, -2, 0, 8, -1, 0, 3]
# # for num in arr2 :
# #     if num < 0 :
# #         negative += 1
# #     elif num > 0 :
# #         positive += 1
# #     else :
# #         zeros += 1
# # print(zeros)
# # print(positive)
# # print(negative)

# # ## seven problem 
# # arr3 = [1,2,22,33,43,44,54,38,94]
# # odd = 0
# # even = 0
# # for num in arr3:
# #     if num % 2 == 0 :
# #         even += 1
# #     else : 
# #         odd += 1 
# # print(odd)
# # print(even)

# ## 8th problem
# arr = [2,12,23,44,56]
# total = 0
# for num in arr :
#     total += num
# average = total/len(arr)
# print(average)

# ## 9th 

# count = 0
# name = "RaSHi64d AnW8593ar"
# for i in name:
#     if i.isdigit():
#         count += 1
# print(count)

# ## 10th

# nA = "level"
# reverse = ""
# for n in nA:
#     reverse = n + reverse
# if reverse == nA :
#     print("This is a palindrome")
# else :
#     print("This is not a palindrome")

# ## 15
# freq = {}
# count1 = 0
# str = "banana"
# for n in str:
#     if n in freq:
#         freq[n] += 1
#     else :
#         freq[n] = 1
        

# print(freq)
    
# st = "rashid anwar"
# # rev = ""
# # for j in st:
# #     if j == j.upper():
# #         rev += j.lower() 
# #     else :
# #         rev += j.upper()
# # print(rev)

# # he = ['rashid','anwar','usmani']
# # print(he.capitalize())

# print(st.titel())

name = "hello   world  lol"
ans = ""

for i in name.split("") :
    if i:
        ans += i.capitalize()
    ans += " "
# name2 = name.split()

# ans = []

# for i in name2 :
#     ans.append(i.capitalize())
# print(" ".join(ans))


