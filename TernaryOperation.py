#implement Ternary operation in python take three no and find the biggest in it
n1=int(input("Enter the first no : "))
n2=int(input("Enter the Second no : "))
n3=int(input("Enter the third no : "))
max=n1 if n1 > n2 and n1 > n3 else (n2 if n2 > n3 else n3)
print(f"biggest is {max}")
