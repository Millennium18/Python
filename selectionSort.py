def selection_sort(lst):        
    for i in range(len(lst)):
        minimum = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[minimum]:
                minimum = j
        lst[minimum], lst[i] = lst[i], lst[minimum]
            
    return lst
lists=[3,5,8,2,4]
print(selection_sort(lists))
