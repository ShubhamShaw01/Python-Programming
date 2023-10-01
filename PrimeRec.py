#check no is prime or not
def is_prime(no, flag):
    if no <= 1:
        return False
    elif flag < no:
        if no % flag == 0:
            return False
        else:
            return is_prime(no, flag + 1)
    else:
        return True


if __name__ == "__main__":
    no = int(input("Enter the number to check if it's prime or not:"))
    if is_prime(no, 2):
        print(f"Entered number {no} is prime.")
    else:
        print(f"Entered number {no} is not prime.")
