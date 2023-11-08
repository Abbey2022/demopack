f =open("myfile.txt","r")
print("read operation on the file first 10 characters:", f.read(11))
print("the file pointer is in ::", f.tell(),"position")
print(f.readline())

f.seek(2)
print(f.readline())

f.close()