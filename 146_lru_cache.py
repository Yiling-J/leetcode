"""
Using double linked list and hash map.

"""

class LRUCache(object):
    
    class Node(object):
        def __init__(self, k, v):
            self.key = k
            self.value = v
            self.previous = None
            self.next = None

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.c = capacity
        self.t = dict()
        self.counter = 0
        
    def extract(self, node):
        node_p = node.previous
        node_n = node.next
        node_p.next = node_n
        node_n.previous = node_p
        
        node_l = self.end.previous
        node_l.next = node
        node.previous = node_l
        node.next = self.end
        self.end.previous = node
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.t:
            node = self.t[key]
            self.extract(node)
            return node.value
        return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.t:
            node = self.t[key]
            node.value = value
            self.extract(node)
            return

        if self.counter == 0:
            self.start = self.Node('start', None)
            self.end = self.Node('end', None)
            node = self.Node(key, value)
            node.previous = self.start
            self.start.next = node
            node.next = self.end
            self.end.previous = node
            self.t[key] = node
            self.counter += 1
            return

        if self.counter >= self.c:
            node = self.start.next
            node_n = node.next
            self.start.next = node_n
            node_n.previous = self.start
            self.t.pop(node.key)
        else:
            self.counter += 1
        node = self.Node(key, value)
        self.t[key] = node
        node_p = self.end.previous
        node_p.next = node
        node.previous = node_p
        node.next = self.end
        self.end.previous = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)