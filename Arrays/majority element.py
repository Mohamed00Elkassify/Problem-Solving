# https://leetcode.com/problems/majority-element/

# solution 1
# Time complexity: O(n)
# Space complexity: O(n)
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
       cnt = Counter(nums)
       return cnt.most_common(1)[0][0]


# solution 2 boyer-moore voting algorithm
# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = 0
        cnt = 0
        for num in nums:
            if cnt == 0:
                candidate = num
            if candidate == num:
                cnt += 1
            else:
                cnt -= 1
        return candidate
#! explanation of boyer-moore voting algorithm
'''Theoretical Idea
The majority element is defined as the element that appears more than ⌊n/2⌋ times in the array.
This means:

If you pair each occurrence of the majority element with a different element,
some majority elements will remain unpaired because it appears more than all others combined.
Key Insight
The algorithm works like a vote counting system:

Candidate selection:
If the counter is 0, we pick the current number as the new candidate.
Vote counting:
If the current number is the same as the candidate, we increment the count (vote for it).
If it’s different, we decrement the count (vote against it).
Why It Works
Imagine the array as a sequence of votes:

Majority element votes: More than half of the total votes.
Minority element votes: Less than half.
When we decrement the count for different elements, we are canceling out one majority vote with one minority vote.

Since the majority element has more votes than all others combined, it will survive all cancellations and remain as the candidate at the end.'''