# https://leetcode.com/problems/car-fleet/description/


# Monotonic Stack
# time complexity: O(nlogn) due to sorting
# space complexity: O(n) for the stack
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse = True)
        stack = []

        for pos, spd in cars:
            TimeToTarget = (target - pos) / spd

            if not stack or TimeToTarget > stack[-1]:
                stack.append(TimeToTarget)
            else:
                continue
        
        return len(stack)