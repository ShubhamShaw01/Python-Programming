#wap a code to check the no is prime or not
def isprime(prime_no):
    if prime_no <= 1:
        return False
    for i in range(2, prime_no):
        if prime_no % i == 0:
            return False
    return True

if __name__ == "__main__":
    prime_no = int(input("Enter the number to check if it's prime or not: "))
    
    if isprime(prime_no):
        print(f"{prime_no} is a prime number.")
    else:
        print(f"{prime_no} is not a prime number.")
