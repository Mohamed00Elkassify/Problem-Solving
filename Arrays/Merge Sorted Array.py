# https://leetcode.com/problems/merge-sorted-array/
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
res = []
a, b = 0, 1
for i in range(m):
    res.append(nums1[i])
for j in range(n):
    res.append(nums2[j])
while a < b:
    if res[b] < res[a]:
        res[a], res[b] = res[b], res[a]

print(res)