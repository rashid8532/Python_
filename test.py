count = 0
string = "ABCDCDC"
sub_string = "CDC"
for i in range(len(string)):
    if string[i : len(sub_string)+i] == sub_string:
        count += 1
print(count)
for i in range(2,10,2):
    print(i)