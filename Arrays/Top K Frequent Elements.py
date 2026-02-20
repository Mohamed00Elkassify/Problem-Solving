# https://leetcode.com/problems/top-k-frequent-elements/description/

# Solution 1 : Collections.Counter
# time complexity : O(n log k)
# space complexity : O(n)
from collections import Counter

def topKFrequent(nums, k):
    return [item[0] for item in Counter(nums).most_common(k)]
    #return [i for i, j in Counter(nums).most_common(k)] 

nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums, k))


# solution 2 : Hashmap
# time complexity : O(n log n)
# space complexity : O(n)
def topKFrequent(nums, k):
    cnt = {}
    for num in nums:
        cnt[num] = cnt.get(num, 0) + 1
    return sorted(cnt.keys(), key=lambda x: cnt[x], reverse=True)[:k] 
    # return the first k elements, reverse=True is for descending order
    # lambda x: cnt[x] is a function that takes x as input and returns cnt[x], it means sort the keys based on their values

nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums, k))