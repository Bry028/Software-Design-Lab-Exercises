def maximum_in_list(nums):
    l = len(nums)
    if l == 1:
        return nums[0]
    m1 = maximum_in_list(nums[0:l//2])
    m2 = maximum_in_list(nums[l//2:l])
    if m1 > m2:
        return m1
    else:
        return m2