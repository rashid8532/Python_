# with open("D:\python 2\File_I_and_O\Sample.txr",'r')as f:
#     data = f.read()
#     print(data)
#     f.close()
    
# with open("D:\python 2\File_I_and_O\Sample.txr",'w')as f :
#     data = f.write("my name is rashid ")
#     f.close()

# with open("D:\python 2\File_I_and_O\Sample.txr",'a')as f:
#     data = f.write("Now i change something ")

# with open("D:\python 2\File_I_and_O\Sample.txr",'r+')as f:
#     f.write("Hi!!! ")
#     data = f.read()
#     print(data)
#     f.close()

with open("D:\python 2\File_I_and_O\Sample.txr",'w+')as f:
    f.write("Hi!!! ")
    data = f.read()
    print(data)
    f.close()

# with open("D:\python 2\File_I_and_O\Sample.txr",'r')as f:
#     data = f.read()
#     print(data)
#     f.close()