# 最大子数组问题
import math

# 递归算法
def find_max_crossing_subarray(array, low, mid, high):
    left_sum = float('-Inf') #无穷小
    sum = 0
    for i in range(mid, low - 1, -1):
        sum += array[i]
        if sum > left_sum:
            left_sum = sum
            max_left_index = i
    right_sum = float('-Inf')
    sum = 0
    for j in range(mid + 1, high + 1):
        sum += array[j]
        if sum > right_sum:
            right_sum = sum
            max_right_index = j
    return (max_left_index, max_right_index, left_sum + right_sum)

def find_maximum_subarray(array, low, high):
    if high == low:
        return (low, high, array[low])
    else:
        mid = math.floor((low + high) / 2)
        (left_low, left_high, left_sum) = find_maximum_subarray(array, low, mid)
        (right_low, right_high, right_sum) = find_maximum_subarray(array, mid + 1, high)
        (cross_low, cross_high, cross_sum) = find_max_crossing_subarray(array, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)
        else:
            return (cross_low, cross_high, cross_sum)

# 暴力算法
def violence(array):
    left_index = 0
    right_index = 0
    sum_return = float('-Inf')
    sum_temp = 0
    for i in range(len(array)):
        for j in range(i, len(array)):
            sum_temp += array[j]
            if sum_temp >= sum_return:
                sum_return = sum_temp
                left_index = i
                right_index = j
        sum_temp = 0
    return (left_index, right_index, sum_return)



# 测试
testArray1 = [-9, -2, -3, -5, -3]
testArray2 = [0, -2, 3, 5, -1, 2]
print(find_maximum_subarray(testArray1, 0, len(testArray1) - 1))
print(violence(testArray1))
print(find_maximum_subarray(testArray2, 0, len(testArray2) - 1))
print(violence(testArray2))
