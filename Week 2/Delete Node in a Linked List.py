class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        actualNode.next=None
        previousNode.next=actualNode
        while actualNode.val != node.val:
            actualNode=previousNode
            previousNode.next=actualNode

        previousNode.next=actualNode.next



        