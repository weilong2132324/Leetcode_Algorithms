def binary_search(arr: list[int], target: int) -> int:
    length = len(arr) - 1
    lower = 0
    upper = length - 1

    while lower <= upper:
        middle = lower + ((upper - lower) // 2)

        if arr[middle] == target:
            return middle
        elif target > arr[middle]:
            lower = middle + 1
        else:
            upper = middle - 1
    
    return -1

if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7,8]
    v = 5
    index_point = binary_search(nums, v)
    print(index_point)
