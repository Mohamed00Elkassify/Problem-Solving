# https://leetcode.com/problems/reorder-list/description/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Approach : store all the nodes in a list and then reorder them using two pointers. 
# O(n) time and O(n) space.
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodes = []
        curr = head

        while curr:
            nodes.append(curr)
            curr = curr.next

        i, j = 0, len(nodes) - 1
        while i < j:
            nodes[i].next = nodes[j] # point the next of the current node to the last node
            i += 1

            if i >= j:
                break

            nodes[j].next = nodes[i] # point the next of the last node to the current node
            j -= 1

        nodes[i].next = None # point the next of the last node to None to mark the end of the list