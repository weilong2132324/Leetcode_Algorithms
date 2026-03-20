def binary_search(nums: list[int], target: int) -> int:
    """
    Returns the index of target in a sorted array, or -1 if not found.
    Time:  O(log n)
    Space: O(1)
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":
    nums = [1, 3, 5, 7, 9, 11, 13]
    print(binary_search(nums, 7))   # 3
    print(binary_search(nums, 6))   # -1
