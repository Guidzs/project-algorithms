def find_duplicate(nums):
    if not all(
        isinstance(n, int) for n in nums
    ) or len(nums) <= 1:
        return False

    for n in nums:
        if n < 0:
            return False
        if list.count(nums, n) > 1:
            return n

    return False
