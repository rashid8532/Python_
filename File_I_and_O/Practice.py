with open("practice.txt",'w') as f:
    f.write("Hi everyone \nwe are learning file I/O/n")
    f.write("By using java \nand i love java ")
with open("practice.txt",'r') as f:
    data = f.read().replace("java","python")
    print(data)
with open("practice.txt",'w') as f:
    f.write(data)
    f.close()
with open("practice.txt",'r') as f:
    data = f.read().find("python")
    print(data)