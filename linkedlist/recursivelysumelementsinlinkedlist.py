"""
Q. Given a linked list, sum all elements in the list.
Examples:
• Given a linked list: 1 ➞ 4 ➞ 5 // returns 10
• Given a linked list: 1 // returns 1
"""


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def sum(node: ListNode) -> int:
    if node is None:
        return 0
    return node.value + sum(node.next)

# Test Cases
LL1 = ListNode(1, ListNode(4, ListNode(5)))
print(sum(None))  # 0
print(sum(LL1))  # 10
print(sum(ListNode(1)))  # 1
