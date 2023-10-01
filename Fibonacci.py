#wap to print fibonacci series
def fibonacci(n):
    a, b = 0, 1
    cursor = 1

    if n <= 0:
        print("There is no Fibonacci series for this value")
    else:
        while cursor <= n:
            if cursor == 1:
                print("Fibonacci series is:")
                print(a, end='\t')
                cursor += 1
            elif cursor == 2:
                print(b, end='\t')
                cursor += 1
            else:
                c = a + b
                a, b = b, c
                print(c, end='\t')
                cursor += 1
        print()

if __name__ == "__main__":
    n = int(input("Enter the length of the Fibonacci series: "))
    fibonacci(n)
