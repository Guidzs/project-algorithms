def find_duplicate(nums):
    if not all(
        isinstance(n, int) for n in nums
    ) or len(nums) <= 1:
        return False
    nums.sort()
    for i, n in enumerate(nums):
        if n < 0:
            return False
        if i <= (len(nums) - 2) and n == nums[i + 1]:
            return n

    return False
