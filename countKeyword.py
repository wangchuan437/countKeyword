import os

path=input('path:')
path=fr'{path}'

fileType=input('fileType:')
str1=input('str:')


def txtRead(file):
    with open(file,'r') as f1:
        txt1=f1.read()
    return txt1

os.chdir(path)
fileList=[i for i in os.listdir() if fileType in i]

contentList=[i+txtRead(i) for i in fileList]

count=[i.count(str1) for i in contentList]

print(str1)
for i,j in zip(fileList,count):
    print(i,j)
    
input('回车键退出')