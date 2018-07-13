def bubble_sort(lists):
    count = len(lists)
    for i in range(count):
        for j in range(i+1, count):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists

l = [1,2,3,4,6,9,5]
print(bubble_sort(l))