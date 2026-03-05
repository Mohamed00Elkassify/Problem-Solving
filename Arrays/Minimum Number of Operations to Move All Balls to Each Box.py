# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description

# prefix and postfix approach
# Time: O(n) and Space: O(n)
def minOperations(boxes):
        n = len(boxes)
        res = [0] * n
        # Left-to-right pass: accumulate cost to bring balls from the left
        Left_Balls_cnt = 0
        Left_Operations = 0
        for i in range(n):
            res[i] += Left_Operations
            if boxes[i] == '1':
                Left_Balls_cnt += 1 # if there is a ball in the current box, then we need to bring it to the next box, so we increment the count of balls on the left
            Left_Operations += Left_Balls_cnt # the cost to bring the balls from the left to the current box is equal to the number of balls on the left, so we add that to the total operations for the next box
        # Right-to-left pass: accumulate cost to bring balls from the right
        Right_Balls_cnt = 0
        Right_Operations = 0
        for i in range(n-1, -1, -1):
            res[i] += Right_Operations
            if boxes[i] == '1':
                Right_Balls_cnt += 1
            Right_Operations += Right_Balls_cnt
        return res