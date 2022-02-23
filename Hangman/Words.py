File=open("Dictionary.txt","r")
word_list=[]
for line in File:
    word=line.split()
    word_list.append(word)
File.close()
w="WXYZ"
print(w.capitalize())
