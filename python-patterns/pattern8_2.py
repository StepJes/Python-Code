# Pattern : Print for n=4 without using third variable.
# 1 
# 2 3
# 3 4 5
# 4 5 6 7
n=int(input("Enter any no.\n"))
for i in range(1,n+1):
    j = i
    for j in range(j,j*2):
        print(j,end=" ");
        j+=1
    print()