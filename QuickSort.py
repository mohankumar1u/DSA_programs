array =[7,9,3,0,2,5,4]
low =0
n=len(array)-1
def QuickSort(low,pivot,arr):
    if(low<pivot):
        i=low-1
        
        for j in range(low,pivot):
            if(arr[j]<arr[pivot]):
                i+=1
                arr[i],arr[j]=arr[j],arr[i]
        arr[i+1],arr[pivot]=arr[pivot],arr[i+1]
        QuickSort(low,i,arr)
        QuickSort(i+2,pivot,arr)
QuickSort(low,n,array)
print(array)