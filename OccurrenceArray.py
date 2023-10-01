#wap to find the occurrence of element
#wap for linear Search
def search(arr,key):
    count=0
    for i in range(len(arr)):
        if(arr[i]==key):
            count+=1
    return count

if __name__=="__main__":
    arr=[]  
    size=int(input("Enter the size of the array : "))
    for i in range(size):
        arr.append(int(input(f"Enter the {i+1} element : ")))
    print(" .. Your entered array is ..")
    print(arr)
    key=int(input("Enter the element to search : "))
    result=search(arr,key)
    if(result>0):
        print(f"{key} occures {result} times ")
    else:
        print(f"{key} is not present in the array")