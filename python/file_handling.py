//read
file=open('1.txt','r')
content=file.read()
print(content)
//write
file=open('1.txt','w')
file.write('byeeeee')
//append
file=open('1.txt','a')
file.write(' good day')