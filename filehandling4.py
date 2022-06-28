file=open(r"C:\Users\JATIN\OneDrive\Documents\python programs\file1.txt")
u=file.readline()
print(u)
i=1
count=0
while i<len(u):
    x=u[i]
    if x=="I":
        input=input("Denote a character you want to replace I with")
        y=file.write(input)
        i=i+1
        count=count+1
    else:
        i=i+1
