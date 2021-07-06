"""
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.
Example 1:
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: l1 = [], l2 = []
Output: []
Example 3:

Input: l1 = [], l2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both l1 and l2 are sorted in non-decreasing order.
"""
def merge(h1,h2):
    if h1==None:
        return h2
    if h2==None:
        return h1
    if h1.val<h2.val :
        h1.next=merge(h1.next,h2)
        return h1
    else:
        h2.next=merge(h2.next,h1)
        return h2
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        mergetwo=merge(l1,l2)
        return mergetwo