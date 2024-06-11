from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseListIterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize two pointers: prev as None (end of the reversed list) 
        # and curr as head (start of the input list)
        prev, curr = None, head

        # Iterate through the linked list until curr becomes None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev =  curr
            curr = nxt

        # After the loop, prev will be pointing to the new head 
        # of the reversed list
        return prev

        #time: O(n)
        #space: O(1)

    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: if head is None, return None (end of list)
        if not head:
            return None
        
        # At the start, assume newHead is the current node
        newHead = head

        # If there's a next node, we need to reverse the rest of the list
        if head.next:
            # Recursively reverse the rest of the list starting from head.next
            newHead = self.reverseListRecursive(head.next)
            # Make the next node's next point to the current node (reverse the link)
            head.next.next = head

        # Set the current node's next to None to break the original link    
        head.next = None

        return newHead
    
        #time: O(n)
        #space: O(n)

# Helper function to convert a list to a linked list
def list_to_linkedlist(items):
    if not items:
        return None
    head = ListNode(items[0])
    current = head
    for item in items[1:]:
        current.next = ListNode(item)
        current = current.next
    return head

# Helper function to print linked list
def print_linkedlist(head):
    current = head
    while current:
        print(current.val, end=' ')
        current = current.next
    print()

# Create a linked list
head = list_to_linkedlist([1, 2, 3, 4, 5])
print("First linked list:")
print_linkedlist(head)

solution = Solution()
reversed_head = solution.reverseListIterative(head)

print("Reversed linked list iteratively:")
print_linkedlist(reversed_head)

head = list_to_linkedlist([1,2])
print("Second linked list:")
print_linkedlist(head)

solution = Solution()
reversed_head = solution.reverseListRecursive(head)

print("Reversed linked list recursively:")
print_linkedlist(reversed_head)