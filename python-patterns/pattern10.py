# Pattern : Print for n=4 without using third variable.
A a
A B C
A B C
n=int(input("Enter any no.\n"))
k=1
for i in range(1,n+1):
    j = i
    for j in range(j,j*2):
        print(j,end=" ");
        j+=1
    print()