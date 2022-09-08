class Node:
    def __init__(self, state, parent = None, cost = 0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.path = self._backtrack()
    
    def __str__(self):
        return "State {} with path {} and cost {}.".format(self.state, self.path, self.cost)

    def __eq__(self, other):
        return self.state == other.state

    def _backtrack(self):
        return [self.state] if self.parent is None else self.parent._backtrack() + [self.state]

class Frontier:
    def __init__(self):
        self.frontier_list = []
        self.reached_list = []
        self.generated_nodes = 0

    def __str__(self):
        n_print = 10
        printed_list = [n.state for n in self.frontier_list[-n_print:]]
        return "[ ..., " + str(printed_list)[1:] if len(self.frontier_list) > n_print else str(printed_list)

    def __len__(self):
        return len(self.frontier_list)
    
    def __iter__(self):
        return FrontierIterator(self)

    def add(self, node_obj: Node):
        if not isinstance(node_obj, Node):
            raise TypeError("Can only add 'Node' object to frontier.")
        else:
            try: # check if 'node_obj' is in reached list
                idx_reached = self.reached_list.index(node_obj)
                if self.reached_list[idx_reached].cost > node_obj.cost:
                    self.reached_list[idx_reached] = node_obj
                    self.generated_nodes += 1
                    try: # check if 'node_obj' is in frontier list
                        idx_frontier = self.frontier_list.index(node_obj)
                        self.frontier_list[idx_frontier] = node_obj
                    except ValueError:
                        pass
            except ValueError:
                self.frontier_list.append(node_obj)
                self.reached_list.append(node_obj)
                self.generated_nodes += 1
    
    def remove(self, node_obj: Node):
        if not isinstance(node_obj, Node):
            raise TypeError("Please specify a 'Node' object.")
        else:
            self.frontier_list.remove(node_obj)

class FrontierIterator:
    def __init__(self, frontier: Frontier):
        self._list = frontier.frontier_list
        self._L = len(frontier.frontier_list)
        self._index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self._index < self._L:
            self._index += 1
            return self._list[self._index - 1]
        raise StopIteration