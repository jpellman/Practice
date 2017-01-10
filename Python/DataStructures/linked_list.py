#!/usr/bin/env python
from collections import Iterable

class Node:
    def __init__(self, data, nextnode=None):
        self.data = data
        if isinstance(nextnode, Node) or not nextnode:
            self.nextnode = nextnode
        else:
            raise TypeError('Not pointing to another node.')
    def getData(self):
        return self.data
    def setNext(self, nextnode):
        if isinstance(nextnode, Node) or not nextnode:
            self.nextnode = nextnode
        else:
            raise TypeError('This is not a node.')
    def getNext(self):
        return self.nextnode

class LinkedList:
    def __init__(self, data):
        if isinstance(data, Iterable):
            self.firstnode = Node(data[0])
            if len(data) > 1:
                self.firstnode.setNext(Node(data[1]))
                n = self.firstnode.getNext()
                for e in range(2, len(data)):
                    n.setNext(Node(data[e]))
                    n = n.getNext()
        else:
            self.firstnode = Node(data)
    def get(self, idx):
        if not isinstance(idx, int):
            raise TypeError('Indexing must be done with ints.')
        n = self.firstnode
        for i in range(idx):
            n = n.getNext()
            if not n:
                raise IndexError('Index %d out of range' % idx)
        return n.getData()
    #def append(self, data):
