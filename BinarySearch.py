#wap to implement Binary Search
def binarySearch(l,h,key):
    mid=(l+h)//2
    if(l>h):
        return -1
    elif(arr[mid]>key):
        return binarySearch(mid+1,h,key)
    elif(arr[mid]==key):
        return mid
    else:
        return binarySearch(l,mid-1,key)
    
if __name__=="__main__":
    global arr
    arr=[]
    size=int(input("Enter the size of the array : "))
    for i in range(size):
        arr.append(int(input(f"Enter the {i+1} element : ")))
    print(" .. Your entered array is ..")
    print(arr)
    key=int(input("Enter the element to search : "))
    result=binarySearch(0,size,key)
    if(result>0):
        print(f"{key} found in  {result} position ")
    else:
        print(f"{key} is not present in the array")