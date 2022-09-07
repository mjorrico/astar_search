import numpy as np

from data_structures import Node, Frontier

def heuristic_cost(state: np.ndarray, goal_state: np.ndarray) -> float:
    return np.sum(np.abs(state - goal_state))

def select_best_node(env, frontier: Frontier, w: float) -> Node:
    fbest = np.inf
    for n in frontier:
        h = heuristic_cost(env.coordinate(n.state), env.coordinate(env.goal_state))
        f = w*n.cost + (1-w)*h
        if f < fbest:
            fbest = f
            best_node = n
    frontier.remove(best_node)
    return best_node

def expand_tree_search(env, node: Node) -> list[Node]:
    child_list = []
    for a in env.action_list(node.state):
        new_state = a[0]
        new_path = node.path + [a[0]]
        new_cost = node.cost + a[1]
        child_list.append(Node(new_state, new_path, new_cost))
    return child_list

def astar_tree_search(env, w: float, show_info: bool = False):
    f = Frontier()
    f.add(Node(env.start_state, [env.start_state]))
    while f.list: # while f isn't empty
        if show_info: print_info(f)
        node = select_best_node(env, f, w)
        if show_info: print(". Best node: " + str(node.state))
        if node.state == env.goal_state: return node
        for child in expand_tree_search(env, node):
            f.add(child) # The rules are implemented in Frontier.add() method.
    return None

def print_info(f: Frontier) -> None:
    print(  "Frontier: " + str(f) + 
            ". Frontier size: " + str(len(f)) + 
            ". Generated nodes: " + str(f.generated_nodes), end = "")