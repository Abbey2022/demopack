#open file in append mode
f=open("mydata.db" , "w")    
for i in range(3):
         name = input("enter name ")
         job = input("enter job")

         rec = name+ ","+job+"\n"
         f.write(rec)
print("content recorded")
f.close()