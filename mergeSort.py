array =[7,9,3,0,2,5,4]
def merge1(r1,r2):
    result =[]
    i=0
    j=0
    while(i<len(r1)and j<len(r2)):
                if(r1[i]<r2[j]):
                    result.append(r1[i])
                    i+=1
                else:
                    result.append(r2[j])
                    j+=1
    result.extend(r1[i:])
    result.extend(r2[j:])
    return result
def merge(arr1, arr2):
    result = []
    i = j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    # Append the remaining elements from arr1 and arr2
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    

    return result

def mergeSort(low,high,arr):
    if(low<high):
        mid =(low+high)//2
        print(mid,"mid",low,high)
        r1=mergeSort(low,mid,arr)
        r2=mergeSort(mid+1,high,arr)
        result = merge1(r1, r2)
        return result
        
    else:
        return [arr[low]]
    


array1 =mergeSort(0,len(array)-1,array)
print(array1)