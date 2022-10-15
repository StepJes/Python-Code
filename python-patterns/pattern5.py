# Pattern : Print for n=4
# * 
# * *
# * * *
# * * * *
n=int(input("Enter any no.\n"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ");
    print()