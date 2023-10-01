#Wap a program to reverse a array without build in function
def reverseArray(arr):
    size=len(arr)
    for i in range(size//2):
        arr[i],arr[size-i-1]=arr[size-i-1],arr[i]
    print("Reverse of the array is")
    print(arr)
arr=[]
size=int(input("Enter the size of the array : "))
for i in range(size):
    arr.append(int(input(f" Enter the {i+1} element : ")))
print("Your entered array is ")
print(arr)
reverseArray(arr)

