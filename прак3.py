h = open("D:\ICS-14\my_file\my_file.txt", 'w+')
i = 1
for i in range(10):
    
    h.write(str(i) + " строка\n")
    
    i + 1
    
h.close()

b = open("D:\ICS-14\my_file\my_file.txt", 'r')
slist = []
k = 0
for k in range (5):
    stroka = b.readlines(k)
    slist.append(stroka)
    print(slist[k])
    k+1
b.close()

print('___________________________________')

with open("D:\ICS-14\my_file\my_file.txt") as sf:
    file = sf.readlines()
print(file)
