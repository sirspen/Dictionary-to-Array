import time

dic = open("Dictionary.txt", 'r') #opens our dictionary, you can change the filename
dicList = [] #this will be the list we export

for x in dic:
    dicList.append(x[:-1])#adds the new word to the list and removes new line

dic.close()

newDic = open("NewDictionary.txt", 'w') #creates new .txt file to store strings

for y in dicList: #writes each new word into the .txt followed by a , and a space
    newDic.write("\""+ y + "\", ")
