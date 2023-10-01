#wap  to find the lcm of two given no
def gcd(no1, no2):
    if no2 == 0:
        return no1
    else:
        return gcd(no2, no1 % no2)
    
def lcm(no1,no2):
    result=gcd(no1,no2)
    return (no1*no2 // result)

if __name__=="__main__":
    no1=int((input("Enter the first no : ")))
    no2=int((input("Enter the first no : ")))
    result=lcm(no1,no2)
    print(f"The LCM of {no1} and {no2} is {result}.")