#wap to implement bubble sort
def bubbleSort(l):
    for i in range(size-1):
        for j in range(size-i-1):
            if l[j]>l[j+1] :
                l[j],l[j+1]=l[j+1],l[j]
    print(" .... sorted list is .... ")
    print(l)
    
if __name__=="__main__":
    l=[]
    size=int(input("Enter the size of the array/list : "))
    for i in range(size):
        l.append(int(input(f"Enter the {i+1} element :")))
    print("Your entered List is ")
    print(l)
    bubbleSort(l)