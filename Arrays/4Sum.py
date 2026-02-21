# https://leetcode.com/problems/4sum/description/

# Brute Force
# Time: O(n^4)
# Space: O(1) without counting the space used for the output
def four_sum(nums, target):
    nums.sort()
    res = set() # to handle duplicates automatically
    for a in range(len(nums)):
        for b in range(a+1, len(nums)):
            for c in range(b+1, len(nums)):
                for d in range(c+1, len(nums)):
                    if nums[a] + nums[b] + nums[c] + nums[d] == target:
                        res.add((nums[a], nums[b], nums[c], nums[d]))
    return list(res)

nums = [3,2,3,-3,1,0]
print(four_sum(nums, 3))

# Two Pointers
# Time: O(n^3)
# Space: O(1) without counting the space used for the output
def four_sum(nums, target):
    n = len(nums)
    nums.sort()
    res = []
    for a in range(n):
        if a > 0 and nums[a] == nums[a-1]:
            continue
        for b in range(a+1, n):
            if b > a + 1 and nums[b] == nums[b-1]:
                continue

            c, d = b + 1, n - 1
            while c < d:
                total = nums[a] + nums[b] + nums[c] + nums[d]
                if total == target:
                    res.append([nums[a], nums[b], nums[c], nums[d]])
                    c += 1
                    d -= 1
                    while c < d and nums[c] == nums[c-1]:
                        c += 1
                    while c < d and nums[d] == nums[d+1]:
                        d -= 1
                
                elif total < target:
                    c += 1
                else:
                    d -= 1
    return res

nums = [3,2,3,-3,1,0]
print(four_sum(nums, 3))
