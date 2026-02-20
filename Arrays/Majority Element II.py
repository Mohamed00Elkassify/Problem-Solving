# https://leetcode.com/problems/majority-element-ii/description/

# Time: O(n) and Space: O(n)

def majorityElement(nums):
    cnt = {}
    for num in nums:
        cnt[num] = cnt.get(num, 0) + 1
    
    res = []
    for key in cnt:
        if cnt[key] > len(nums) / 3:
            res.append(key)

    return res

nums = [3,2,3]
print(majorityElement(nums))

nums = [1,2]
print(majorityElement(nums))

nums = [1]
print(majorityElement(nums))

nums = [1,2,3,3,2,1,1]
print(majorityElement(nums))
