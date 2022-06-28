file=open(r"C:\Users\JATIN\OneDrive\Documents\python programs\file1.txt")
j=0
sum=0
while j<4:
    u=file.readline()
    print(u)
    z=len(u)
    print(z)
    
    i=1
    count=0
    while i<z:
        x=u[i]
        if x=="e" or x=="a" or x=="i" or x=="o" or x=="u" or x=="A" or x=="E" or x=="I" or x=="O" or x=="U":
            count=count+1
            i=i+1
        else:
            i=i+1
    print("the number of vowels in this str is ",count)
    j=j+1
    sum=sum+count
print("Overall number of vowels ",sum)

