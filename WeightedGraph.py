from GraphNode import GraphNode
from LinkedList import LinkedList


class WeightedGraph:
    def __init__(self, _adjlist):
        self.adjlist = _adjlist

    def add_edge(self, vsrc, vdst, weight):
        if (vsrc.get_key() <= len(self._adjlist)) and vdst.get_key() <= len(self._adjlist):
            self.adjlist[vsrc.get_key()].add_last((vdst, weight))
