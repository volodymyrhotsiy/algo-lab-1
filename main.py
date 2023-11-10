def binary_search(nums, val, find_left=True):
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] == val:
            return mid
        elif nums[mid] < val:
            l = mid + 1
        else:
            r = mid - 1

    
    if find_left:
        return l
    else:
        return l - 1 if l > 0 else 0


def solution(nums, reversed=False):
    if reversed:
        nums.reverse()
    if len(nums) <= 1:
        return(-1, -1)

    l, r = 0, len(nums) - 1

    while l < len(nums) - 1 and nums[l] <= nums[l + 1]:
        l += 1

    if l == len(nums) - 1:
        return (-1, -1)
    
    while r > 0 and nums[r] >= nums[r - 1]:
        r -= 1

    min_val = min(nums[l:r + 1])
    max_val = max(nums[l:r + 1]) 

    left_index, right_index = binary_search(nums[:l], min_val, find_left=True), binary_search(nums[r+1:], max_val) + r
    
    return (left_index, right_index) if not reversed else (len(nums) - right_index - 1, len(nums) - left_index - 1)


print(solution([8, 7, 6, 5, 4, 2, 3, 1], reversed=True))
print(solution([1, 3, 2, 4, 5, 6, 7, 8], reversed=False))

