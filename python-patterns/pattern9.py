# Pattern : Print for n=4 without using third variable.
# 1 
# 2 1
# 3 2 1
# 4 3 2 1
n=int(input("Enter any no.\n"))
for i in range(1,n+1):
    for j in range(i,0,-1):
        print(j,end=" ");
        j+=1
    print()