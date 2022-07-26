from sys import argv

f= open(file:'prueba.txt','r')
copy= open('prueva1.txt','w')

for line in f :
    copy.write(line)


    f.close()
    copy.close()