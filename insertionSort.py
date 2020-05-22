def insertion_sort(arr):
    for i in range(len(arr)):
        cursor=arr[i]
        pos=i

        while pos > 0 and arr[pos-1] > cursor:
            arr[pos]=arr[pos-1]
            pos -= 1

        arr[pos] = cursor
    return(arr)

lst=[ 4,2,6,3,5,1]
print(insertion_sort(lst))
