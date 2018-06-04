def selection_sort(array):
    n = len(array)
    for i in range(n):
        min = i
        for j in range(i + 1, n):
            if array[j] < array[min]:
                min = j
        array[i], array[min] = array[min], array[i]
    return array


if __name__ == "__main__":
    print(selection_sort([23, 42, 13, 49, -5]))
