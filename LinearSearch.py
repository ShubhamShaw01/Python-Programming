#wap for linear Search
def search(arr,key):
    for i in range(len(arr)):
        if(arr[i]==key):
            print(f"{key} is present in position {i}")
            break
    else:
        print(f"{key} is not present in the array")

if __name__=="__main__":
    arr=[]  
    size=int(input("Enter the size of the array : "))
    for i in range(size):
        arr.append(int(input(f"Enter the {i+1} element : ")))
    print(" .. Your entered array is ..")
    print(arr)
    key=int(input("Enter the element to search : "))
    search(arr,key)