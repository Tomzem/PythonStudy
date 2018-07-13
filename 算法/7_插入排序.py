# 插入排序的基本操作就是将一个数据插入到已经排好序的有序数据中，
# 从而得到一个新的、个数加一的有序数据，算法适用于少量数据的排序，
# 时间复杂度为O(n^2)。是稳定的排序方法。

def insert_sort(lists):
    for i in range(1, len(lists)):
        key = lists[i]
        j = i - 1
        while j >= 0:
            if lists[j] > key :
                lists[j+1] = lists[j]
                lists[j] = key
            j -= 1
    return lists

l = [1,2,3,4,6,9,5]
print(insert_sort(l))