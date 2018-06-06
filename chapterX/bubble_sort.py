def bubble_sort(array):
    n = len(array)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

if __name__ == '__main__':
    print(bubble_sort([45, 32, 8, 33, 12, 22, 19, 97]))
