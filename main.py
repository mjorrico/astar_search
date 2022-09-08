import argparse
import a_star_search as search
from environments import gridEnvP1

parser = argparse.ArgumentParser(prog = 'python3 main.py',
                                 description = 'Implements A* search on a specified dataset.')
parser.add_argument('-d', '--data',
                    default = "./data/100 nodes.csv",
                    dest = "path_to_data",
                    required = True,
                    help = "path to states/environment data.")
parser.add_argument('-s', '--start-state',
                    type = int,
                    required = True,
                    help = "an integer that indicates the starting state.")
parser.add_argument('-g', '--goal-state',
                    type = int,
                    required = True,
                    help = "an integer that indicates the goal state.")
parser.add_argument('-w', '--weight',
                    type = float,
                    required = True,
                    help = "the weight parameter for A* search\
                            to calculate f = w*g + (1-w)*h.\
                            must be between 0 and 1.")
parser.add_argument('-v', '--verbose',
                    action = 'store_true',
                    help = "prints information such as frontier details and best node for every iteration.")
                            
args = vars(parser.parse_args())
filepath = args["path_to_data"]
start = args["start_state"]
goal = args["goal_state"]
w = args["weight"]
v = args["verbose"]

env = gridEnvP1()
env.load(filepath)
env.initialize(start, goal)
result = search.astar_tree_search(env, w, v)

if result:
	result_node = result[0]
	result_frontier = result[1]
	print("Path length: " + str(len(result_node.path)))
	print("Path cost: " + str(result_node.cost))
	print("Path: " + str(result_node.path))
	print("Nodes generated: " + str(result_frontier.generated_nodes))
else:
	print("There is no path")