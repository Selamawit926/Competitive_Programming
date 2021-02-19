def quickSort(lst,start,end):
    if (start < end):
        mid = partition(A, start, end)
        quickSort(A, start, mid-1)
        quickSort(A, mid + 1, end)
