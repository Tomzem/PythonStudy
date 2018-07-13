def binary_search(num_list, key):
    start = 0
    end = len(num_list) - 1
    while start <= end:
        mid = int((start + end) / 2)
        if key is num_list[mid]:
            return "find {}".format(mid + 1)
        elif key > num_list[mid]:
            start = mid + 1
        else:
            end = mid
    return "no find {}".format(key)


list = range(0, 22)
print(binary_search(list, 1))

