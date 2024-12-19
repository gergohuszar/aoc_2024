from numpy import array
import numpy as np


class Player:
    def __init__(self, x: int, y: int, map, dir):
        self.x = x
        self.y = y
        self.first_x = x
        self.first_y = y
        self.first_dir = dir
        self.cur_dir = dir
        self.visited = set()
        self.map = map
        self.max_x, self.max_y = map.shape

    def move(self):
        if self.cur_dir == "up":
            self.x -= 1
        elif self.cur_dir == "right":
            self.y += 1
        elif self.cur_dir == "down":
            self.x += 1
        elif self.cur_dir == "left":
            self.y -= 1
        else:
            raise ValueError(f"Invalid direction: {self.cur_dir}")

    def state(self):
        return (self.x, self.y, self.cur_dir)

    def next_dir(dir):
        if dir == "up":
            return "right"
        elif dir == "right":
            return "down"
        elif dir == "down":
            return "left"
        elif dir == "left":
            return "up"
        else:
            raise ValueError(f"Invalid direction: {dir}")

    def give_new_dir(self):
        self.cur_dir = Player.next_dir(self.cur_dir)

    def calc_next_direction(
        self,
    ) -> str:
        if self.cur_dir == "up":
            new_pos = (self.x - 1, self.y)
        elif self.cur_dir == "right":
            new_pos = (self.x, self.y + 1)
        elif self.cur_dir == "down":
            new_pos = (self.x + 1, self.y)
        elif self.cur_dir == "left":
            new_pos = (self.x, self.y - 1)
        else:
            raise ValueError(f"Invalid direction: {self.cur_dir}")

        if self.is_in_bounds(new_pos[0], new_pos[1]):
            char = self.map[new_pos]

            if char == "#":
                self.give_new_dir()

    def is_in_bounds(self, x, y) -> bool:
        return 0 <= x < self.max_x and 0 <= y < self.max_y

    def save_visited(self):
        while self.is_in_bounds(self.x, self.y):
            self.visited.add((self.x, self.y))

            self.calc_next_direction()
            self.move()

    def player_reset(self):
        self.x = self.first_x
        self.y = self.first_y
        self.cur_dir = self.first_dir


def is_loop(x, y, player):
    if player.map[x][y] == "#":
        return False
    player.map[x][y] = "#"

    states = set()

    while player.is_in_bounds(player.x, player.y):
        state = player.state()

        if state in states:
            player.map[x][y] = "."
            return True

        states.add(state)

        player.calc_next_direction()
        player.move()

    player.map[x][y] = "."
    return False


def solution(input: str) -> int:
    input_list: list[str] = input.splitlines()

    matrix = array([list(row) for row in input_list])

    player_pos_x, player_pos_y = np.where(matrix == "^")
    player_pos_x, player_pos_y = int(player_pos_x[0]), int(player_pos_y[0])

    player = Player(player_pos_x, player_pos_y, matrix, "up")

    count = 0

    player.save_visited()

    player.player_reset()

    for i, cordinates in enumerate(player.visited):
        x, y = cordinates

        loop = is_loop(x, y, player)
        player.player_reset()
        if loop:
            count += 1

    print(count)
    return count


if __name__ == "__main__":
    np.set_printoptions(threshold=np.inf, linewidth=np.inf)
    with open("input.txt") as f:
        input_str = f.read()
        solution(input_str)


