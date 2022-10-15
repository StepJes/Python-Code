# Pattern : Print for n=3
# 9 8 7
# 6 5 4
# 3 2 1
n=int(input("Enter any no.\n"))
k = n*n
for i in range(1,n+1):
    for j in range(1,n+1):
        print(k,end=" ");
        k-=1
    print()