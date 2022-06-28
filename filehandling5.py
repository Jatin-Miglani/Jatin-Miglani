file1=open(r"C:\Users\JATIN\OneDrive\Documents\python programs\file1.txt")
stri=""
i=0
while i<10:
    file2=file1.readline()
    print(file2)
    file3=file2.replace("i","e")
    print(file3)
    stri=stri+file3
    i=i+1
file4=print(stri)
file4=str(file4)
print(type(file4))
file1=open(r"C:\Users\JATIN\OneDrive\Documents\python programs\file1.txt","a")
file5=file1.write(file4)
file1.close()
