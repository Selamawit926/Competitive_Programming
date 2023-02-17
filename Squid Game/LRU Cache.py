class ListNode:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.save={}
        self.head=ListNode(0,0)
        self.tail=ListNode(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head

    def get(self, key: int) -> int:
        if key not in self.save:
            return -1
        self.remove(self.save[key])
        self.addToBack(self.save[key])
        return self.save[key].val
        
    def put(self, key: int, value: int) -> None:
        if key in self.save:
            self.remove(self.save[key])
        newNode=ListNode(key,value)
        self.save[key]=newNode
        self.addToBack(newNode)
        if len(self.save)>self.capacity:
            leastNode=self.head.next
            self.remove(leastNode)
            del self.save[leastNode.key]

    def addToBack(self,node):
        prev=self.tail.prev
        prev.next=node
        self.tail.prev=node
        node.prev=prev
        node.next=self.tail
        
    def remove(self,node):
        prev=node.prev
        nxt=node.next
        prev.next=nxt
        nxt.prev=prev
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)