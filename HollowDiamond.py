#wap a program to print hollow diamond
def pattern(n):
    for i in range(1,n+1):
        print(" "*(n-i),end="")
        for j in range(1,i+1):
            if j==1 or j==i :
                print("* ",end="")
            else:
                print("  ",end="")
        print()
    for i in range(n-1,0,-1):
        print(" "*(n-i),end="")
        for j in range(i,0,-1):
            if j==1 or j==i:
                print("* ",end="")
            else:
                print("  ",end="")
        print()
n=int(input("Enter the no : "))
pattern(n)