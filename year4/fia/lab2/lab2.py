import pygame
import sys
import random
import math
import logging
from collections import deque

# Set up logging for debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

pygame.init()

WIDTH, HEIGHT = 28 * 20, 31 * 20 + 50  # Adjusted height for larger maze
FPS = 10  # Adjusted for better visibility of movements

BLACK = (0, 0, 0)
BLUE = (33, 33, 255)
PACMAN_COLOR = (255, 255, 0)
GHOST_COLORS = [(255, 0, 0), (255, 184, 255), (0, 255, 255), (255, 184, 82)]
WALL_COLOR = (33, 33, 255)
PALLET_COLOR = (255, 184, 151)
TEXT_COLOR = (255, 255, 255)

ROWS, COLS = 31, 28  # Updated for larger maze
CELL_SIZE = 20

font = pygame.font.SysFont('Arial', 24)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man AI")
clock = pygame.time.Clock()

score = 0
lives = 3

# Updated maze layout resembling the classic Pac-Man maze
maze = [
    "1111111111111111111111111111",
    "1000000000000000000000000001",
    "1011111110101101101111111101",
    "1000000000100000100000000001",
    "1011111110111010101111111101",
    "1000000000000000000000000001",
    "1011111111110111111110101101",
    "1000000000000110000000000001",
    "1011111110110110111111111101",
    "1000000000110000100000000001",
    "1111111110111111101111111111",
    "1000000000000000000000000001",
    "1011111111110111011110111101",
    "1000000000110111000000000001",
    "1011111110110111101111111101",
    "1000000000000000000000000001",
    "1111111111110111111111111111",
    "1000000000000110000000000001",
    "1011110110110110111111101101",
    "1011110000110000111111101101",
    "1011111110111110111111101101",
    "1000000000111110000000000001",
    "1011111110111111101111111101",
    "1011111000111100000111111101",
    "1010000010000001110111000001",
    "1000111000111100000110011101",
    "1011111110111111101110111101",
    "1011100000111111100000111101",
    "1011101110111111101011111101",
    "1000000000000000000000000001",
    "1111111111111111111111111111",
]

# Ensure the maze has the correct number of rows
while len(maze) < ROWS:
    maze.append(maze[-1])

maze = [list(row) for row in maze]

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

directions = [UP, DOWN, LEFT, RIGHT]

OPPOSITE_DIRECTION = {
    UP: DOWN,
    DOWN: UP,
    LEFT: RIGHT,
    RIGHT: LEFT
}

class Node:
    def __init__(self, x, y, direction=None, parent=None):
        self.x = x
        self.y = y
        self.direction = direction
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

class Pacman:
    def __init__(self, x, y):
        self.start_pos = (x, y)
        self.x = x
        self.y = y
        self.previous_positions = deque(maxlen=4)  # Store last 4 positions

    def move(self, direction):
        if self.can_move(direction):
            self.x = (self.x + direction[0]) % COLS
            self.y = (self.y + direction[1]) % ROWS
            self.previous_positions.append((self.x, self.y))
            logging.debug(f'Pacman moved to ({self.x}, {self.y})')

    def can_move(self, direction):
        next_x = (self.x + direction[0]) % COLS
        next_y = (self.y + direction[1]) % ROWS
        if maze[next_y][next_x] != '1':
            return True
        return False

    def reset(self):
        self.x, self.y = self.start_pos
        self.previous_positions.clear()
        logging.debug('Pacman reset to start position')

class Ghost:
    def __init__(self, x, y, color):
        self.start_pos = (x, y)
        self.x = x
        self.y = y
        self.color = color
        self.previous_positions = deque(maxlen=4)  # Store last 4 positions

    def move(self, pacman):
        # Use A* to predict Pacman's future position
        predicted_pacman_pos = self.predict_pacman(pacman)
        path = self.a_star(predicted_pacman_pos[0], predicted_pacman_pos[1])
        if path and len(path) > 1:
            next_node = path[1]
            self.x = next_node.x
            self.y = next_node.y
            self.x %= COLS
            self.y %= ROWS
            self.previous_positions.append((self.x, self.y))
            logging.debug(f'Ghost moved to ({self.x}, {self.y}) using A* path')
        else:
            self.random_move()

    def predict_pacman(self, pacman):
        if len(pacman.previous_positions) >= 2:
            dx = pacman.previous_positions[-1][0] - pacman.previous_positions[-2][0]
            dy = pacman.previous_positions[-1][1] - pacman.previous_positions[-2][1]
            predicted_x = (pacman.x + dx) % COLS
            predicted_y = (pacman.y + dy) % ROWS
            if maze[predicted_y][predicted_x] != '1':
                return (predicted_x, predicted_y)
        return (pacman.x, pacman.y)

    def random_move(self):
        possible_directions = directions.copy()
        random.shuffle(possible_directions)
        for direction in possible_directions:
            if self.can_move(direction):
                self.x = (self.x + direction[0]) % COLS
                self.y = (self.y + direction[1]) % ROWS
                self.previous_positions.append((self.x, self.y))
                logging.debug(f'Ghost randomly moved to ({self.x}, {self.y})')
                break

    def can_move(self, direction):
        next_x = (self.x + direction[0]) % COLS
        next_y = (self.y + direction[1]) % ROWS
        if maze[next_y][next_x] != '1':
            return True
        return False

    def reset(self):
        self.x, self.y = self.start_pos
        self.previous_positions.clear()
        logging.debug('Ghost reset to start position')

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

def draw_maze():
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == '1':
                pygame.draw.rect(screen, WALL_COLOR, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif cell == '0':
                pygame.draw.circle(screen, PALLET_COLOR,
                                   (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2), 3)

def draw_pacman(pacman):
    pygame.draw.rect(screen, PACMAN_COLOR,
                     (pacman.x * CELL_SIZE + 3, pacman.y * CELL_SIZE + 3, CELL_SIZE - 6, CELL_SIZE - 6))

def draw_ghost(ghost):
    pygame.draw.circle(screen, ghost.color,
                       (ghost.x * CELL_SIZE + CELL_SIZE // 2, ghost.y * CELL_SIZE + CELL_SIZE // 2),
                       CELL_SIZE // 2 - 2)

def display_score():
    score_text = font.render(f'Score: {int(score)}', True, TEXT_COLOR)
    screen.blit(score_text, (10, HEIGHT - 40))

def display_lives():
    lives_text = font.render(f'Lives: {lives}', True, TEXT_COLOR)
    screen.blit(lives_text, (WIDTH - 100, HEIGHT - 40))

def game_over_screen():
    screen.fill(BLACK)
    game_over_text = font.render('Game Over', True, TEXT_COLOR)
    restart_text = font.render('Press R to Restart', True, TEXT_COLOR)
    screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 50))
    screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2))
    pygame.display.update()

def distance(p1, p2):
    dx = min(abs(p1[0] - p2[0]), COLS - abs(p1[0] - p2[0]))
    dy = min(abs(p1[1] - p2[1]), ROWS - abs(p1[1] - p2[1]))
    return dx + dy

def count_remaining_pallets():
    return sum(row.count('0') for row in maze)

def get_valid_moves(x, y):
    valid_moves = []
    for direction in directions:
        next_x = (x + direction[0]) % COLS
        next_y = (y + direction[1]) % ROWS
        if maze[next_y][next_x] != '1':
            valid_moves.append(direction)
    return valid_moves

def is_dead_end(x, y):
    moves = get_valid_moves(x, y)
    return len(moves) <= 1

def get_random_spawn():
    while True:
        x = random.randint(0, COLS - 1)
        y = random.randint(0, ROWS - 1)
        if maze[y][x] != '1':
            return x, y

def minimax(position, depth, alpha, beta, max_player, pacman_pos, ghost_positions, visited_states):
    if depth == 0 or game_over():
        return evaluate(pacman_pos, ghost_positions)

    state_key = (pacman_pos, tuple(ghost_positions))
    if state_key in visited_states:
        return visited_states[state_key]

    if max_player:
        max_eval = -math.inf
        for move in sorted(get_valid_moves(pacman_pos[0], pacman_pos[1]), key=lambda m: move_ordering(m, pacman_pos, ghost_positions), reverse=True):
            next_x = (pacman_pos[0] + move[0]) % COLS
            next_y = (pacman_pos[1] + move[1]) % ROWS
            if is_dead_end(next_x, next_y) and any(distance((next_x, next_y), ghost_pos) <= 2 for ghost_pos in ghost_positions):
                continue  # Avoid dead ends when ghosts are near
            new_pacman_pos = (next_x, next_y)
            eval = minimax(position + 1, depth - 1, alpha, beta, False, new_pacman_pos, ghost_positions, visited_states)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        visited_states[state_key] = max_eval
        return max_eval
    else:
        min_eval = math.inf
        for ghost_index, ghost_pos in enumerate(ghost_positions):
            for move in get_valid_moves(ghost_pos[0], ghost_pos[1]):
                new_ghost_pos = ((ghost_pos[0] + move[0]) % COLS, (ghost_pos[1] + move[1]) % ROWS)
                new_ghost_positions = list(ghost_positions)
                new_ghost_positions[ghost_index] = new_ghost_pos
                eval = minimax(position + 1, depth - 1, alpha, beta, True, pacman_pos, tuple(new_ghost_positions), visited_states)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        visited_states[state_key] = min_eval
        return min_eval

def move_ordering(move, pacman_pos, ghost_positions):
    next_pos = ((pacman_pos[0] + move[0]) % COLS, (pacman_pos[1] + move[1]) % ROWS)
    ghost_distances = [distance(next_pos, ghost_pos) for ghost_pos in ghost_positions]
    min_ghost_distance = min(ghost_distances)
    return min_ghost_distance

def evaluate(pacman_pos, ghost_positions):
    ghost_distances = [distance(pacman_pos, ghost_pos) for ghost_pos in ghost_positions]
    min_ghost_distance = min(ghost_distances)
    pallet_distance = distance_to_nearest_pallet(pacman_pos)
    remaining_pallets = count_remaining_pallets()
    score = (10 / (pallet_distance + 1)) - remaining_pallets * 0.5

    # Encourage Pacman to stay at least 4 blocks away from ghosts
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

def distance_to_nearest_pallet(pacman_pos):
    visited = set()
    queue = deque()
    queue.append((pacman_pos[0], pacman_pos[1], 0))
    while queue:
        x, y, dist = queue.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        if maze[y][x] == '0':
            return dist
        for direction in directions:
            next_x = (x + direction[0]) % COLS
            next_y = (y + direction[1]) % ROWS
            if maze[next_y][next_x] != '1':
                queue.append((next_x, next_y, dist + 1))
    return 0

def game_over():
    return lives <= 0 or count_remaining_pallets() == 0

def main():
    global score, lives, pacman
    running = True
    game_over_flag = False

    # Initialize pallets
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == '0' or cell == ' ':
                maze[y][x] = '0'

    # Randomize Pacman's starting position
    pacman_x, pacman_y = get_random_spawn()
    pacman = Pacman(pacman_x, pacman_y)

    # Randomize ghosts' starting positions
    ghosts = []
    for color in GHOST_COLORS:
        while True:
            ghost_x, ghost_y = get_random_spawn()
            # Ensure ghosts don't spawn on Pacman's position
            if (ghost_x, ghost_y) != (pacman.x, pacman.y) and distance((ghost_x, ghost_y), (pacman.x, pacman.y)) >= 5:
                break
        ghosts.append(Ghost(ghost_x, ghost_y, color))

    while running:
        clock.tick(FPS)
        screen.fill(BLACK)
        draw_maze()
        draw_pacman(pacman)
        for ghost in ghosts:
            draw_ghost(ghost)
        display_score()
        display_lives()
        pygame.display.update()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and game_over_flag:
                    score = 0
                    lives = 3
                    # Reset maze pallets
                    for y, row in enumerate(maze):
                        for x, cell in enumerate(row):
                            if cell == ' ':
                                maze[y][x] = '0'
                    # Randomize Pacman's starting position
                    pacman_x, pacman_y = get_random_spawn()
                    pacman = Pacman(pacman_x, pacman_y)
                    # Randomize ghosts' starting positions
                    ghosts = []
                    for color in GHOST_COLORS:
                        while True:
                            ghost_x, ghost_y = get_random_spawn()
                            if (ghost_x, ghost_y) != (pacman.x, pacman.y) and distance((ghost_x, ghost_y), (pacman.x, pacman.y)) >= 5:
                                break
                        ghosts.append(Ghost(ghost_x, ghost_y, color))
                    game_over_flag = False

        if game_over_flag:
            game_over_screen()
            continue

        # AI decision-making for Pacman
        visited_states = {}
        best_score = -math.inf
        best_move = None
        ghost_positions = [(ghost.x, ghost.y) for ghost in ghosts]
        for move in get_valid_moves(pacman.x, pacman.y):
            next_x = (pacman.x + move[0]) % COLS
            next_y = (pacman.y + move[1]) % ROWS
            # Avoid dead ends when ghosts are near
            if is_dead_end(next_x, next_y) and any(distance((next_x, next_y), ghost_pos) <= 2 for ghost_pos in ghost_positions):
                continue
            new_pacman_pos = (next_x, next_y)
            eval = minimax(0, 3, -math.inf, math.inf, False, new_pacman_pos, tuple(ghost_positions), visited_states)
            if eval > best_score:
                best_score = eval
                best_move = move

        if best_move:
            pacman.move(best_move)

        for ghost in ghosts:
            ghost.move(pacman)

        for ghost in ghosts:
            if distance((pacman.x, pacman.y), (ghost.x, ghost.y)) < 1:
                lives -= 1
                logging.warning(f'Pacman collided with a ghost at ({ghost.x}, {ghost.y})')
                # Reset Pacman's position
                pacman_x, pacman_y = get_random_spawn()
                pacman = Pacman(pacman_x, pacman_y)
                # Reset ghosts' positions
                ghosts = []
                for color in GHOST_COLORS:
                    while True:
                        ghost_x, ghost_y = get_random_spawn()
                        if (ghost_x, ghost_y) != (pacman.x, pacman.y) and distance((ghost_x, ghost_y), (pacman.x, pacman.y)) >= 5:
                            break
                    ghosts.append(Ghost(ghost_x, ghost_y, color))
                if lives == 0:
                    game_over_flag = True
                    logging.error('Game Over: Pacman has no lives left.')
                break  # Break to avoid multiple collisions in one frame

        if maze[pacman.y][pacman.x] == '0':
            maze[pacman.y][pacman.x] = ' '
            score += 10
            logging.info(f'Pacman collected a pallet at ({pacman.x}, {pacman.y}). New score: {score}')

        if count_remaining_pallets() == 0:
            game_over_flag = True
            logging.info('All pallets collected. Game Over.')

    pygame.quit()

if __name__ == '__main__':
    main()
