open_file=open('przyklad.txt','r')
line=open_file.readline()
while line:
    print(line)
    line=open_file.readline()
