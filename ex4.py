f=open("mydata.db" , "w")    #open file in write mode
name = input("enter name ")
job = input("enter job")

rec = name+ ","+job+"\n"
f.write(rec)
f.close()