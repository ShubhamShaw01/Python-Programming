''' write a program to print this pattern
*
* *
* * *
'''
def pattern(rows):
    for i in range(1,rows+1):
        print("* "*i)
if __name__=="__main__":
    rows=int(input("Enter how many rows you want : "))
    pattern(rows)
    
