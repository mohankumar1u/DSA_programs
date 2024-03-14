class Solution:
    def merge(arr, left, mid, right):
        n1 = mid - left + 1
        n2 = right - mid

        left_half = [0] * n1
        right_half = [0] * n2

        for i in range(n1):
            left_half[i] = arr[left + i]

        for j in range(n2):
            right_half[j] = arr[mid + 1 + j]

        i = j = 0
        k = left

        while i < n1 and j < n2:
            if left_half[i] <= right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < n1:
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < n2:
            arr[k] = right_half[j]
            j += 1
            k += 1


    def merge_sort(self, arr, left, right):
      if(left<right):
        mid=(left+right)//2
        Solution.merge_sort(self,arr,left,mid)
        Solution.merge_sort(self,arr,mid+1,right)
        return Solution.merge(arr, left, mid, right)