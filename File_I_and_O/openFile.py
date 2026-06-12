# f = open("D:\python 2\File_I_and_O\docx.txt","r")
# data = f.read()
# data = f.read(5)#this will print the 5 charecters from the file 
# data = f.readline()#this will read only a line 
# data = f.read()
# print(data)
# print(type(data))
# f.close()


j = open("D:\python 2\File_I_and_O\docx.txt",'w')#this w is for writing 
file = j.write("Than i move to the javascript\n")
j.close()

j = open("D:\python 2\File_I_and_O\docx.txt",'a')#this a is for appending a line in at the end of the file 
file = j.write("Than i move to the javascript")
j.close()

e = open("D:\python 2\File_I_and_O\Sample.txr",'a')
newfile = e.write("this is a new file made by python")
e.close()
