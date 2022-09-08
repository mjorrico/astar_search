import csv
import numpy as np

class gridEnvP1:
    def __init__(self):
        self.state_coordinate = {} # {state: (x_coordinate, y_coordinate)}
        self.state_actions = {} # {state: [(state_1, cost_1), (state_2, cost_2), ...]}
        self.start_state = None
        self.goal_state = None

    def load(self, path_to_csv):
        with open(path_to_csv, newline='') as r:
            reader = csv.reader(r)
            data = np.array(list(reader)[1:], dtype = np.int64)
        
        states = data[:, 0]
        coordinates = data[:, 1:3]
        costs = data[:, 3:]

        del data
        L = len(states)

        self.state_coordinate = dict(zip(states, coordinates))
        self.state_actions = {states[i]: [(states[j], costs[i, j]) for j in range(L) if costs[i, j] != 0] for i in range(L)}

        del states, coordinates, costs
    
    def initialize(self, start_state: int, goal_state: int) -> None:
        self.start_state = start_state
        self.goal_state = goal_state

    def coordinate(self, state: int) -> np.ndarray:
        return self.state_coordinate[state]
    
    def action_list(self, state: int) -> list[tuple]:
        return self.state_actions[state]