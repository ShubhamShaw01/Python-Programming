#wap to find the gdc of the two no
def gcd(no1, no2):
    if no2 == 0:
        return no1
    else:
        return gcd(no2, no1 % no2)

if __name__ == "__main__":
    no1 = int(input("Enter the first number to find its GCD: "))
    no2 = int(input("Enter the second number to find its GCD: "))
    result = gcd(no1, no2)
    print(f"GCD of {no1} and {no2} is {result}")
