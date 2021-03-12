"""
    @ LeetCode 0024. Swap Nodes in Pairs
    @ Prob. https://leetcode.com/problems/swap-nodes-in-pairs/
     Ref.
    @ Algo: LinkedList
    @ Start day: 20. 10. 05.
    @ End day: 20. 10. 05.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None:
            return head

        currentNode = head
        while currentNode and currentNode.next:
            currentNode.val, currentNode.next.val = currentNode.next.val, currentNode.val
            
            nextNode = currentNode.next
            if nextNode.next == None: break
            currentNode = nextNode.next
        
        return head
        

if __name__ == "__main__":
    node4 = ListNode(4, None)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)
    
    solution = Solution()
    swapHead = solution.swapPairs(node1)
    
    while swapHead != None:
        print(swapHead.val, end=" ")
        swapHead = swapHead.next
        
        