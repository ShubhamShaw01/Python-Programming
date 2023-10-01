#wap for insertion sort
def sorting(arr,len):
    for i in range(1,len):
        key=arr[i]
        j=i-1
        while(j>=0 and arr[j]>key):
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    print(" .. The sorted array is ..")
    print(arr)
    
if __name__=="__main__":
    arr=[]
    size=int(input("Enter the size of the array : "))
    for i in range(size):
        arr.append(int(input(f"Enter the {i+1} element : ")))
    print(" .. Your entered array is ..")
    print(arr)
    sorting(arr,size)