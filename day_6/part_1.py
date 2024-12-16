from numpy import array
import numpy as np


class Player:
    def __init__(self, x: int, y: int, map):
        self.x = x
        self.y = y
        self.cur_dir = "up"
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

    def give_new_dir(self):
        if self.cur_dir == "up":
            self.cur_dir = "right"
        elif self.cur_dir == "right":
            self.cur_dir = "down"
        elif self.cur_dir == "down":
            self.cur_dir = "left"
        elif self.cur_dir == "left":
            self.cur_dir = "up"
        else:
            raise ValueError(f"Invalid direction: {self.cur_dir}")

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
        if self.is_in_bounds(*new_pos):
            char = self.map[new_pos]

            if char == "#":
                self.give_new_dir()

    def is_in_bounds(self, x, y) -> bool:
        return 0 <= x < self.max_x and 0 <= y < self.max_y

    def cur_char(self) -> bool:
        return self.map[self.x][self.y]


def solution(input: str) -> int:
    input_list: list[str] = input.splitlines()

    matrix = array([list(row) for row in input_list])

    player_pos_x, player_pos_y = np.where(matrix == "^")
    player_pos_x, player_pos_y = int(player_pos_x[0]), int(player_pos_y[0])

    player = Player(player_pos_x, player_pos_y, matrix)

    while player.is_in_bounds(player.x, player.y):
        player.visited.add((player.x, player.y))

        player.calc_next_direction()
        player.move()

    print(len(player.visited))

    return len(player.visited)


if __name__ == "__main__":
    with open("input.txt") as f:
        input_str = f.read()
        print(solution(input_str))
