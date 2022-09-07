# A* Search

An implementation of A* search on generalized gridworld environment.


## Run Locally

Clone the project

```bash
  $ git clone https://github.com/mjorrico/astar_search.git
```

Go to the project directory

```bash
  $ cd astar_search
```

Install dependencies

```bash
  $ pip install -r requirements.txt
```

Start A* search

```bash
  $ python3 main.py -d PATH_TO_DATA -s START_STATE -g GOAL_STATE -w WEIGHT [-v] 
```

Show help

```bash
  $ python3 main.py -h
```

## Example

The following command will use environment provided in `100 nodes.csv` and run A* search from state `12` to reach state `89` using weight parameter `0.4`.

```bash
  $ python3 main.py -d data/100\ nodes.csv -s 12 -g 89 -w 0.4
```
