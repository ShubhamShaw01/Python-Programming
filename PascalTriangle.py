#wap a to print pascal triangle
def pattern(n):
    flag =1
    for i in range(1,n+1):
        print("  "*(n-i),end="")
        temp=flag
        while(temp>0):
            temp1=temp%10
            print(temp1," ",end=" ")
            temp//=10
        flag*=11
        print()
n=int(input("Enter the no : "))
pattern(n)