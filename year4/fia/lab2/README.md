# Gosted in Luna City


## Code Workflow
### Initialization:

- Import necessary modules (`pygame`, `sys`, `random`, `math`, `logging`, `deque`).
- Set up logging for debugging purposes.
- Initialize Pygame and define `screen dimensions`, `colors`, `maze dimensions`, and `font`.
- Define global variables for `score` and `lives`.
- Define the `maze layout` as a 2D list.

### Define Constants and Directions:

- Define movement directions `(UP, DOWN, LEFT, RIGHT)` and a list of all possible directions.
- Create a mapping for opposite directions `(OPPOSITE_DIRECTION)`.

### Define Classes:

- **Node**: Used in the `A* algorithm` for pathfinding.
- **Pacman/Agent**:
  - Handles Pac-Man's/Agent position and movement.
  - Stores previous positions to avoid loops.
- **Ghost**:
  - Handles ghost positions and movement.
  - Uses `A* algorithm` to predict and chase Pac-Man.
  - Can also move `randomly` if no path is found.

<hr/>

**Explanation:**

The `A* algorithm` is one of the most popular pathfinding algorithms used in AI, especially in games, because it efficiently finds the shortest path between a start and a goal while considering obstacles. `A*` combines the advantages of `Dijkstra's Algorithm` and `Greedy Best-First Search` by using both the actual distance from the start and an estimated distance to the goal.

The Basic Steps of `A* Algorithm`:
- **Start** with the initial node (Pac-Man’s position, for example) and put it in the open list.
- **Choose the node** from the open list that has the lowest F value (F = G + H).
- **Check if the node is the goal**:
  - If yes, you found the path!
  - If no, move it to the closed list and explore its neighbors (up, down, left, right).
- **For each neighbor**, calculate:
  - The G (actual cost from start to this neighbor).
  - The H (estimated cost to the goal from this neighbor).
  - The F (total cost).
- If the neighbor **is not in the open list** (not yet explored), add it to the open list.
- **Repeat** the process until you reach the goal or the open list is empty (which means no path was found). 


#### Advantages of A*
- **Optimal Path**: Finds the shortest path efficiently.
- **Efficient Search**: The heuristic ensures that A* doesn’t waste time exploring unnecessary paths.
- **Combines Best Features**: Uses both the actual distance (G) and the estimated distance to the goal (H).


- The `A* algorithm` is perfect for pathfinding in games like Pac-Man, where you need to navigate a maze efficiently.
- `A*` balances between finding the shortest path and not wasting time on unnecessary nodes by using the `F = G + H` formula.

<hr/>

### Define Helper Functions:

- `draw_maze()`: Draws the maze on the screen.
- `draw_pacman()`: Draws Pac-Man as a square.
- `draw_ghost()`: Draws ghosts as circles.
- `display_score()`: Displays the current score.
- `display_lives()`: Displays the remaining lives.
- `game_over_screen()`: Displays the game over screen.
- `distance()`: Calculates the distance between two points.
- `count_remaining_pallets()`: Counts the remaining pallets in the maze.
- `get_valid_moves()`: Returns valid moves from a given position.
- `is_dead_end()`: Checks if a position is a dead end.
- `get_random_spawn()`: Finds a random spawn position in the maze.
- `minimax()`: Implements the MiniMax algorithm with Alpha-Beta pruning.
- `move_ordering()`: Orders moves to improve MiniMax efficiency.
- `evaluate()`: Evaluation function for MiniMax.
- `distance_to_nearest_pallet()`: Finds the distance to the nearest pallet.
- `game_over()`: Checks if the game is over.


### Main Game Loop:

- Initialize Pac-Man and ghosts with random positions.
  - Run the game `loop`, which includes:
  - Handling events (`quit`, `restart`).
  - Updating the display.
  - AI decision-making for Pac-Man using `MinMax`.
  - Moving ghosts using `A*` pathfinding.
  - Collision detection between Pac-Man and ghosts.
  - Pallet collection and score updating.
  - Checking for game over conditions.

  ### Game Termination:
- Exit the game loop and quit Pygame when the game is over.


## Task Implementations
### Task 1: Implement the MiniMax Algorithm
#### MiniMax Algorithm with Basic Scoring Function

The `MiniMax algorithm` is implemented in the `minimax()` function. The scoring function used is:

``` python
Score = Pallet Score - Ghost Danger
```

- **Pallet Score**: The reciprocal of the distance to the nearest pallet `(1 / (pallet_distance + 1))`.
- **Ghost Danger**: The minimum distance to the nearest ghost.

#### Implementation Details:

- **Function**: `minimax(position, depth, alpha, beta, max_player, pacman_pos, ghost_positions, visited_states)`
  - **Parameters**:
    - `position`: Current position in the game tree (unused, can be omitted).
    - `depth`: Depth of the search tree.
    - `alpha`: Alpha value for Alpha-Beta pruning.
    - `beta`: Beta value for Alpha-Beta pruning.
    - `max_player`: Boolean indicating if it's the maximizing player's turn.
    - `pacman_pos`: Current position of Pac-Man.
    - `ghost_positions`: Tuple of current positions of the ghosts.
    - `visited_states`: Dictionary for memoization to avoid recalculations.
- **Base Case**: If `zdepth == 0` or `game_over()`, return the evaluation score.
- **Recursive Case**:
  - **Maximizing Player** (Pac-Man):
    - Iterate over valid moves for Pac-Man.
    - Calculate the new position and recursively call `minimax()` for the minimizing player.
    - Keep track of the maximum evaluation score.
    - Implement `Alpha-Beta pruning` to cut off unnecessary branches.
  - **Minimizing Player** (Ghosts):
    - Iterate over valid moves for each ghost.
    - Calculate new positions for ghosts and recursively call `minimax()` for the maximizing player.
    - Keep track of the minimum evaluation score.
    - Implement `Alpha-Beta pruning`.

- Code Snippet:
``` python
def minimax(position, depth, alpha, beta, max_player, pacman_pos, ghost_positions, visited_states):
    if depth == 0 or game_over():
        return evaluate(pacman_pos, ghost_positions)

    state_key = (pacman_pos, tuple(ghost_positions))
    if state_key in visited_states:
        return visited_states[state_key]

    if max_player:
        max_eval = -math.inf
        for move in get_valid_moves(pacman_pos[0], pacman_pos[1]):
            new_pacman_pos = ((pacman_pos[0] + move[0]) % COLS, (pacman_pos[1] + move[1]) % ROWS)
            eval = minimax(position + 1, depth - 1, alpha, beta, False, new_pacman_pos, ghost_positions, visited_states)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        visited_states[state_key] = max_eval
        return max_eval
    else:
        min_eval = math.inf
        # Similar implementation for ghosts
```


### Task 2: Implement Alpha-Beta Pruning
#### Alpha-Beta pruning is integrated into the `minimax()` function to optimize the search by pruning branches that won't affect the final decision.

- `Alpha`: The best already explored option along the path to the root for the maximizer.
- `Beta`: The best already explored option along the path to the root for the minimizer.

#### Implementation Details:

- `Alpha` and `Beta` values are updated during recursion.
- If `beta <= alpha`, the branch is pruned.

**Code Snippet:**

``` python
if max_player:
    # ...
    alpha = max(alpha, eval)
    if beta <= alpha:
        break  # Beta cut-off
else:
    # ...
    beta = min(beta, eval)
    if beta <= alpha:
        break  # Alpha cut-off
```

### Task 3: Implement an Improved Scoring (Evaluation) Method
#### The evaluation function is enhanced by incorporating additional factors:

- **Remaining Pallets**: The number of pallets left in the maze.
- **Safe Distance**: Pac-Man is encouraged to maintain a safe distance from ghosts.
- **Loop Penalty**: Penalizes repetitive movements to avoid loops.
- **Ghost Proximity Penalty**: Heavy penalty if a ghost is too close.

#### Implementation Details:

- **Function**: `evaluate(pacman_pos, ghost_positions)`
- **Variables**:
  - `min_ghost_distance`: Minimum distance to the nearest ghost.
  - `pallet_distance`: Distance to the nearest pallet.
  - `remaining_pallets`: Number of remaining pallets.
- **Scoring**:
  - **Pallet Score**: `(10 / (pallet_distance + 1))`
    - Ghost Distance Reward/Penalty:
    - Penalize `if min_ghost_distance < SAFE_DISTANCE`.
    - Reward `if min_ghost_distance >= SAFE_DISTANCE`.
  - Remaining `Pallets Penalty: - remaining_pallets * 0.5`
- **Loop Penalty**: `-50` if Pac-Man is looping.
- **Collision Penalty**: `-1000` if Pac-Man is caught.

**Code Snippet:**
``` python
def evaluate(pacman_pos, ghost_positions):
    ghost_distances = [distance(pacman_pos, ghost_pos) for ghost_pos in ghost_positions]
    min_ghost_distance = min(ghost_distances)
    pallet_distance = distance_to_nearest_pallet(pacman_pos)
    remaining_pallets = count_remaining_pallets()
    score = (10 / (pallet_distance + 1)) - remaining_pallets * 0.5

    SAFE_DISTANCE = 5  # Minimum safe distance from ghosts
    if min_ghost_distance < SAFE_DISTANCE:
        score -= (SAFE_DISTANCE - min_ghost_distance) * 100  # Heavy penalty for being too close
    else:
        score += min_ghost_distance * 10  # Reward for maintaining safe distance

    # Penalize repetitive movements
    if len(pacman.previous_positions) >= 4 and len(set(pacman.previous_positions)) <= 2:
        score -= 50

    if min_ghost_distance == 0:
        score -= 1000  # Heavy penalty for being caught
    return score
```

### Task 4: Add Improvements to the MiniMax Algorithm
#### Implemented Improvement: Move Ordering

Move ordering is implemented to enhance the efficiency of the MiniMax algorithm by exploring the most promising moves first. This increases the chances of pruning branches earlier due to Alpha-Beta pruning.

#### Implementation Details:

- Moves are sorted based on their heuristic value before being explored.
- `The move_ordering()` function orders moves based on the minimum distance to ghosts after the move.

**Code Snippet:**
``` python
def move_ordering(move, pacman_pos, ghost_positions):
    next_pos = ((pacman_pos[0] + move[0]) % COLS, (pacman_pos[1] + move[1]) % ROWS)
    ghost_distances = [distance(next_pos, ghost_pos) for ghost_pos in ghost_positions]
    min_ghost_distance = min(ghost_distances)
    return min_ghost_distance

# Usage in minimax function
for move in sorted(get_valid_moves(pacman_pos[0], pacman_pos[1]), key=lambda m: move_ordering(m, pacman_pos, ghost_positions), reverse=True):
    # Explore moves
```

### Task 5: Improve Path Finding with A-Star Algorithm

The ghosts use the A-Star (A*) algorithm for pathfinding to chase Pac-Man efficiently.

#### Implementation Details:

- **Function**: `a_star(goal_x, goal_y)`
- **Heuristics**:
  - `G` (Cost from Start): Number of steps from the starting position.
  - `H` (Heuristic Estimate to Goal): Euclidean distance squared to the goal.
- **Algorithm**:
  - Maintain an open list of nodes to explore and a closed set of explored nodes.
  - At each step, select the node with the lowest F score (F = G + H).
  - Reconstruct the path when the goal is reached.

**Code Snippet:**

``` python
def a_star(self, goal_x, goal_y):
    open_list = []
    closed_list = set()

    start_node = Node(self.x, self.y)
    goal_node = Node(goal_x, goal_y)

    open_list.append(start_node)

    while open_list:
        current_node = min(open_list, key=lambda node: node.f)
        open_list.remove(current_node)
        closed_list.add((current_node.x, current_node.y))

        if current_node == goal_node:
            path = []
            while current_node:
                path.append(current_node)
                current_node = current_node.parent
            return path[::-1]

        for direction in directions:
            node_x = (current_node.x + direction[0]) % COLS
            node_y = (current_node.y + direction[1]) % ROWS

            if maze[node_y][node_x] == '1' or (node_x, node_y) in closed_list:
                continue

            new_node = Node(node_x, node_y, parent=current_node)
            new_node.g = current_node.g + 1
            new_node.h = (node_x - goal_node.x) ** 2 + (node_y - goal_node.y) ** 2
            new_node.f = new_node.g + new_node.h

            if any(open_node for open_node in open_list if open_node == new_node and open_node.g <= new_node.g):
                continue

            open_list.append(new_node)

    return None
```

### Task 6: Combine A-Star with Alpha-Beta Pruning

Alpha-Beta pruning is already integrated within the MiniMax algorithm, and the A-Star algorithm is used by the ghosts for pathfinding. While the two algorithms serve different purposes, they collectively enhance the game's AI:

- **Pac-Man's/Agent AI**: Uses MiniMax with Alpha-Beta pruning to decide the best move considering the ghosts' positions.
- **Ghosts' AI**: Use A-Star to efficiently find paths towards Pac-Man.

Integration:
- The evaluation function considers the distances calculated by both algorithms.
- The MiniMax algorithm evaluates potential moves by Pac-Man, considering the paths the ghosts might take.


## Definitions and Explanations
### MiniMax Algorithm
The `MiniMax algorithm` is a recursive decision-making algorithm used in game theory and AI to minimize the possible loss in a worst-case scenario. It is commonly applied in two-player turn-based games to determine the optimal move for a player, assuming that the opponent also plays optimally.
- **Maximizing Player**: Pac-Man, who tries to maximize the evaluation score.
- **Minimizing Player**: Ghosts, who try to minimize Pac-Man's score.

The algorithm explores possible moves up to a certain depth and evaluates the end states using the evaluation function.

The `minimax()` function implements the MiniMax algorithm with Alpha-Beta pruning:
``` python
def minimax(position, depth, alpha, beta, max_player, pacman_pos, ghost_positions, visited_states):
    if depth == 0 or game_over():
        return evaluate(pacman_pos, ghost_positions)

    state_key = (pacman_pos, tuple(ghost_positions))
    if state_key in visited_states:
        return visited_states[state_key]

    if max_player:
        max_eval = -math.inf
        for move in sorted(get_valid_moves(pacman_pos[0], pacman_pos[1]), 
                           key=lambda m: move_ordering(m, pacman_pos, ghost_positions), reverse=True):
            next_x = (pacman_pos[0] + move[0]) % COLS
            next_y = (pacman_pos[1] + move[1]) % ROWS
            if is_dead_end(next_x, next_y) and any(distance((next_x, next_y), ghost_pos) <= 2 
                                                   for ghost_pos in ghost_positions):
                continue  # Avoid dead ends when ghosts are near
            new_pacman_pos = (next_x, next_y)
            eval = minimax(position + 1, depth - 1, alpha, beta, False, new_pacman_pos, 
                           ghost_positions, visited_states)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Beta cut-off
        visited_states[state_key] = max_eval
        return max_eval
    else:
        min_eval = math.inf
        for ghost_index, ghost_pos in enumerate(ghost_positions):
            for move in get_valid_moves(ghost_pos[0], ghost_pos[1]):
                new_ghost_pos = ((ghost_pos[0] + move[0]) % COLS, (ghost_pos[1] + move[1]) % ROWS)
                new_ghost_positions = list(ghost_positions)
                new_ghost_positions[ghost_index] = new_ghost_pos
                eval = minimax(position + 1, depth - 1, alpha, beta, True, pacman_pos, 
                               tuple(new_ghost_positions), visited_states)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break  # Alpha cut-off
        visited_states[state_key] = min_eval
        return min_eval

```

#### Explanation:

- **Base Case**: The recursion stops when the maximum depth is reached or the game is over.
- **Maximizing Player** `(max_player is True)`:
  - Pac-Man considers all valid moves.
  - Uses zmove_ordering()` to prioritize moves that increase the distance from ghosts.
  - Applies Alpha-Beta pruning to eliminate branches that won't yield better results.
- **Minimizing Player** `(max_player is False)`:
  - Each ghost considers all valid moves.
  - Simulates the ghosts' optimal strategy to minimize Pac-Man's score.

### Alpha-Beta Pruning

Alpha-Beta pruning is an optimization technique for the MiniMax algorithm that reduces the number of nodes evaluated by pruning branches that won't influence the final decision. It keeps track of two values:

- `Alpha`: The best (highest) score that the maximizer currently can guarantee.
- `Beta`: The best (lowest) score that the minimizer currently can guarantee.

If the maximizer realizes that a move leads to a position worse than the current alpha value, it stops exploring that branch.

By updating these values during the recursion, branches that cannot possibly affect the final decision are pruned, enhancing performance.

`Alpha-Beta` pruning is integrated within the `minimax()` function:

``` python
# For Maximizing Player (Pac-Man)
alpha = max(alpha, eval)
if beta <= alpha:
    break  # Beta cut-off

# For Minimizing Player (Ghosts)
beta = min(beta, eval)
if beta <= alpha:
    break  # Alpha cut-off

```

#### Explanation:

- When the maximizer's best option (`alpha`) is greater than or equal to the minimizer's best option (`beta`), further exploration of that branch won't yield a better outcome, so it can be pruned.
- This significantly reduces the number of nodes evaluated, improving efficiency.

### Evaluation Function

The evaluation function estimates the desirability of a game state. It helps the MiniMax algorithm decide which moves are better. In your code, the evaluation function considers:

- Distance to the nearest pallet.
- Remaining number of pallets.
- Distance to the nearest ghost.
- Whether Pac-Man is maintaining a safe distance from ghosts.
- Penalizes repetitive movements to avoid loops.

#### Factors Considered:
- **Distance to the Nearest Pallet**: Encourages Pac-Man to collect food.
- **Remaining Number of Pallets**: Motivates Pac-Man to finish the level quickly.
- **Distance to the Nearest Ghost**: Encourages Pac-Man to maintain a safe distance from ghosts.
- **Safe Distance Maintenance**: Penalizes Pac-Man for being too close to ghosts.
- **Loop Avoidance**: Discourages repetitive movements that could lead to being trapped.
- **Collision Penalty**: Applies a heavy penalty if Pac-Man is caught by a ghost.

#### Implementation in Code:

``` python
def evaluate(pacman_pos, ghost_positions):
    ghost_distances = [distance(pacman_pos, ghost_pos) for ghost_pos in ghost_positions]
    min_ghost_distance = min(ghost_distances)
    pallet_distance = distance_to_nearest_pallet(pacman_pos)
    remaining_pallets = count_remaining_pallets()
    score = (10 / (pallet_distance + 1)) - remaining_pallets * 0.5

    SAFE_DISTANCE = 5  # Minimum safe distance from ghosts
    if min_ghost_distance < SAFE_DISTANCE:
        score -= (SAFE_DISTANCE - min_ghost_distance) * 100  # Heavy penalty for being too close
    else:
        score += min_ghost_distance * 10  # Reward for maintaining safe distance

    # Penalize repetitive movements
    if len(pacman.previous_positions) >= 4 and len(set(pacman.previous_positions)) <= 2:
        score -= 50

    if min_ghost_distance == 0:
        score -= 1000  # Heavy penalty for being caught
    return score
```

#### Explanation:

- **Pallet Score**: The term (10 / (pallet_distance + 1)) incentivizes Pac-Man to move towards the nearest pallet.
- **Remaining Pallets Penalty**: - remaining_pallets * 0.5 encourages Pac-Man to clear the level efficiently.
- **Ghost Danger Penalty**:
  - If the ghost is too close, Pac-Man receives a heavy penalty.
  - If Pac-Man maintains a safe distance, he is rewarded.
- **Loop Penalty**: Penalizes repetitive positions to prevent Pac-Man from getting stuck.
- **Collision Penalty**: A severe penalty if Pac-Man is caught, reflecting an undesirable game state.





## Additional Explanations and Anticipated Questions

### Move Ordering in MiniMax Algorithm
- `Question`: How does move ordering improve the efficiency of the MiniMax algorithm in your implementation?

- `Answer`: Move ordering sorts the possible moves based on a heuristic before exploring them. In our implementation, we prioritize moves that increase the distance from the nearest ghost. By exploring these promising moves first, Alpha-Beta pruning is more likely to occur early, as suboptimal branches can be pruned sooner. This reduces the number of nodes evaluated and enhances the efficiency of the algorithm.

**Implementation in Code:**

``` python
def move_ordering(move, pacman_pos, ghost_positions):
    next_pos = ((pacman_pos[0] + move[0]) % COLS, (pacman_pos[1] + move[1]) % ROWS)
    ghost_distances = [distance(next_pos, ghost_pos) for ghost_pos in ghost_positions]
    min_ghost_distance = min(ghost_distances)
    return min_ghost_distance  # Prioritize moves that increase distance from ghosts
```

### Ghosts' A Pathfinding Algorithm*
- `Question`: Can you explain how the ghosts' A* pathfinding works and how it affects Pac-Man's strategy?
- `Answer`: The ghosts use the A* algorithm to find the shortest path to Pac-Man's predicted position. The A* algorithm combines the actual cost from the start node and a heuristic estimate to the goal to determine the most efficient path.

**Implementation in Code:**
``` python
def a_star(self, goal_x, goal_y):
    open_list = []
    closed_list = set()

    start_node = Node(self.x, self.y)
    goal_node = Node(goal_x, goal_y)

    open_list.append(start_node)

    while open_list:
        current_node = min(open_list, key=lambda node: node.f)
        open_list.remove(current_node)
        closed_list.add((current_node.x, current_node.y))

        if current_node == goal_node:
            path = []
            while current_node:
                path.append(current_node)
                current_node = current_node.parent
            return path[::-1]

        for direction in directions:
            node_x = (current_node.x + direction[0]) % COLS
            node_y = (current_node.y + direction[1]) % ROWS

            if maze[node_y][node_x] == '1' or (node_x, node_y) in closed_list:
                continue

            new_node = Node(node_x, node_y, parent=current_node)
            new_node.g = current_node.g + 1
            new_node.h = (node_x - goal_node.x) ** 2 + (node_y - goal_node.y) ** 2
            new_node.f = new_node.g + new_node.h

            if any(open_node for open_node in open_list if open_node == new_node and open_node.g <= new_node.g):
                continue

            open_list.append(new_node)

    return None
```

#### Impact on Pac-Man's Strategy:

- Pac-Man's AI considers the ghosts' potential movements when evaluating its own moves.
- Knowing that ghosts are using A* to chase him, Pac-Man can anticipate their paths and avoid them.
- This interaction makes the game more dynamic and challenging.

### Loop Avoidance Mechanism
- `Question`: How does your code prevent Pac-Man from getting stuck in loops?
- `Answer`: We track Pac-Man's previous positions using a deque (previous_positions) with a maximum length. If Pac-Man repeatedly visits the same positions, we detect this pattern and apply a penalty in the evaluation function to discourage such behavior.

**Implementation in Code:**

``` python
# In Pacman's move method
self.previous_positions.append((self.x, self.y))

# In the evaluation function
if len(pacman.previous_positions) >= 4 and len(set(pacman.previous_positions)) <= 2:
    score -= 50  # Penalize repetitive movements

```

### Safe Distance from Ghosts
- `Question`: Why did you choose a safe distance of 5 blocks, and how does it affect Pac-Man's decisions?
- `Answer`: A safe distance of 5 blocks is chosen to provide Pac-Man with enough buffer to react to approaching ghosts while still allowing him to navigate the maze effectively. This distance ensures that Pac-Man prioritizes safety without being overly cautious, which could hinder his ability to collect pallets.

#### Effect on Decisions:
- Pac-Man is encouraged to maintain at least this distance from ghosts.
- If a ghost gets too close, Pac-Man's evaluation score decreases sharply, prompting him to move away.
- This balancing act between collecting pallets and avoiding ghosts creates a more strategic gameplay.

### Handling of Game Over Conditions
- `Question`: How does your program determine when the game is over?
- `Answer`: The game over condition is checked in the `game_over()` function. The game ends when either:

- Pac-Man?agen has no lives left (`lives <= 0`).
- All pallets have been collected (`count_remaining_pallets() == 0`).

**Implementation in Code:**
``` python
def game_over():
    return lives <= 0 or count_remaining_pallets() == 0
```
When the game is over, the `game_over_flag` is set to `True`, and the game over screen is displayed.


### Potential Improvements and Limitations
- `Question`: What are the limitations of your AI, and how could it be further improved?
- `Answer`:
  - **Limitations**:
    - Depth of MiniMax Search: Limited by computational resources; deeper searches provide better decision-making but require more processing time.
    - Ghosts' Predictability: Ghosts use deterministic algorithms, which can be exploited by Pac-Man if patterns are recognized.
    - Static Evaluation Function: The evaluation function uses predefined weights, which may not adapt to different game situations dynamically.
  - **Potential Improvements**:
    - Iterative Deepening: Implementing iterative deepening in MiniMax to allow the AI to search deeper when time allows.
    - Dynamic Ghost Behaviors: Introducing varied behaviors or randomness to ghosts to make them less predictable.
    - Machine Learning: Using reinforcement learning to allow Pac-Man to learn from experience and improve over time.
    - Power-Ups and Special Items: Incorporating additional game elements to make the evaluation function and game mechanics more complex and interesting.