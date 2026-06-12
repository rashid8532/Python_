lis = [1,22,34,23,552,112,453,904]
def listfunction(lis,index):
    if index == len(lis):
        return
    print(lis[index])
    return listfunction(lis,index +1)

listfunction(lis,0)