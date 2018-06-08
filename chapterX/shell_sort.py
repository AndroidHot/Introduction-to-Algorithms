def shell_sort(array):
    n = len(array)
    step = n // 2
    while step > 0:
        # insertion sort.
        for j in range(step, n):
            min = array[j]
            i = j - step
            while i >= 0 and array[i] > min:
                array[i + step] = array[i]
                i -= step
            array[i + step] = min
        # decrease step.
        step = step // 2
    return array


if __name__ == '__main__':
    array = [13, 14, 94, 33, 82, 25, 59, 94, 65, 23, 45, 27, 73, 25, 39, 10]
    print(shell_sort(array))
