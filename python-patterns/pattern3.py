# Pattern : Print for n=3
# 1 2 3
# 4 5 6
# 7 8 9
n=int(input("Enter any no.\n"))
k = 1
for i in range(1,n+1):
    for j in range(1,n+1):
        print(k,end=" ");
        k+=1
    print()