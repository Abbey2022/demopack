#open file in append mode
f=open("mydata.db" , "r") 
text=f.readlines()  
print("number of records:",len(text))

recordno =int(input("enter the record number:"))

if recordno ==0 or recordno > len(text):
    print("out of order")

else:
    print(text[recordno -1])
      
f.close()