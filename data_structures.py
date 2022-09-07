class Node:
    def __init__(self, state, path = [], cost = 0):
        self.state = state
        self.path = path
        self.cost = cost
    
    def __str__(self):
        return "State {} with path {} and cost {}.".format(self.state, self.path, self.cost)

    def __eq__(self, other):
        return self.state == other.state

class Frontier:
    def __init__(self):
        self.list = []
        self.generated_nodes = 0

    def __str__(self):
        n_print = 10
        printed_list = [n.state for n in self.list[-n_print:]]
        if len(self.list) > n_print:
            return "[ ..., " + str(printed_list)[1:]
        else:
            return str(printed_list)

    def __len__(self):
        return len(self.list)
    
    def __iter__(self):
        return FrontierIterator(self)

    def add(self, node_obj: Node):
        if not isinstance(node_obj, Node):
            raise TypeError("Can only add 'Node' object to frontier.")
        else:
            try:
                idx = self.list.index(node_obj) # ValueError is raised if 'node_obj' isn't present in frontier
                if self.list[idx].cost > node_obj.cost:
                    self.list[idx] = node_obj
                    self.generated_nodes += 1
                    return True
                return False
            except ValueError:
                self.list.append(node_obj)
                self.generated_nodes += 1
                return True
    
    def remove(self, node_obj: Node):
        if not isinstance(node_obj, Node):
            raise TypeError("Please specify a 'Node' object.")
        else:
            self.list.remove(node_obj)

class FrontierIterator:
    def __init__(self, frontier: Frontier):
        self._list = frontier.list
        self._L = len(frontier.list)
        self._index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self._index < self._L:
            self._index += 1
            return self._list[self._index - 1]
        raise StopIteration

# For debugging purposes
if __name__ == "__main__":
    n1 = Node(1, [3, 2], 12)
    n2 = Node(2, [3, 3, 1], 12)
    n3 = Node(3, [3, 1, 1], 10)
    n4 = Node(9, [3, 1], 4)
    f = Frontier()
    print(f.add(n1))
    print(f.add(n2))
    print(f.add(n3))
    print(f.add(n4))
    print(f.add(Node(2)))
    print(f.add(Node(2, [1, 2], 2)))
    print(f)
    f.remove(Node(9))
    print(f)