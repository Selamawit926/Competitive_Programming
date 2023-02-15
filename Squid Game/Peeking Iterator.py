class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator=copy.deepcopy(iterator)
        self.prev=iterator.next()
        # print(self.prev)
        # self.prev=iterator.next()
        # print(self.prev)
    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        self.temp=copy.deepcopy(self.iterator)
        self.prev=self.temp.next()
        return self.prev

    def next(self):
        """
        :rtype: int
        """
        return self.iterator.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.iterator.hasNext()