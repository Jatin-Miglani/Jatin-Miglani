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
        if x=="A" or x=="B" or x=="C" or x=="D" or x=="E" or x=="F" or x=="G" or x=="H" or  x=="I" or x=="J" or x=="K" or x=="L" or x=="M" or x=="N" or x=="O" or x=="P" or x=="Q" or x=="R" or x=="S" or x=="T" or x=="U" or x=="V" or x=="W" or x=="X" or x=="Y" or x=="Z":
         count=count+1
         i=i+1
        else:
         i=i+1

    print("The number of uppercase letters in this String is",count+1)

    j=j+1
    sum=sum+count+1
print("the overall number of uppercase letters are",sum)
        
