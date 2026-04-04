# 2095. Delete the Middle Node of a Linked List
# see the quetion on leetcode this inlcude digram that will help you to get better idea


from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        slow = head
        fast = head
        prev = None
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        prev.next = slow.next
        return head


# 🔽 Helper functions for testing
def build_list(arr):
    dummy = ListNode()
    cur = dummy
    for x in arr:
        cur.next = ListNode(x)
        cur = cur.next
    return dummy.next


def print_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)


