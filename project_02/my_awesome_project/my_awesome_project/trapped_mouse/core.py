import numpy as np
from pprint import pprint
from random import randint
import copy


class Maze:
    def __init__(self, row, column):

        self.maze = np.random.rand(row,column).tolist()
        self.history_maze = []
        self.history_stack = []
        self.history_current_position = []

        for er, i in enumerate(self.maze):
            for ec, j in enumerate(i):
                self.maze[er][ec] = 1 if j > 0.5 else 0

        self.stack = []
        self.currentCell = None

        """
            0 - top
            1 - left
            2 - bottom
            3 - right
        """
        areas = {
            "top": {
                "row": 0,
                "column": randint(1, column - 2)
            },
            "left": {
                "row": randint(1, row - 2),
                "column": column - 1
            },
            "bottom": {
                "row": row - 1,
                "column": randint(1, column - 2)
            },
            "right": {
                "row": randint(1, row - 2),
                "column": 0
            }
        }

        exit_area = self.generate_area()

        mouse_row = randint(1, row - 2)
        mouse_column = randint(1, column - 2)
        exit_row = areas[list(areas.keys())[exit_area]]['row']
        exit_column = areas[list(areas.keys())[exit_area]]['column']

        self.maze[mouse_row][mouse_column] = "m"
        self.maze[exit_row][exit_column] = "e"

        self.currentCell = {
            "row": mouse_row,
            "column": mouse_column
        }

        print("E>",(exit_row, exit_column))
        print("M>",(mouse_row, mouse_column))

        # Preencher com 1 nas bordas onde não for saída - e
        for em, list_ in enumerate(self.maze):

            for e, j in enumerate(list_):
                if (e == 0 or e == column - 1) and j != "e":
                    list_[e] = 1
                if ((row - row) == em) and j != "e":
                    list_[e] = 1
                if (row - 1 == em) and j != "e":
                    list_[e] = 1

        # generate path valid
        for e_row, r in enumerate(self.maze):

            # top and bottom
            if exit_area in [0, 2]:

                # top
                if exit_row < mouse_row:
                    # print('top')

                    if e_row < mouse_row:

                        if e_row > exit_row:
                            r[mouse_column] = 0

                            if exit_column > mouse_column and e_row == exit_row + 1:
                                for j in range(mouse_column + 1, exit_column + 1):
                                    r[j] = 0

                            if exit_column < mouse_column and e_row == exit_row + 1:
                                for j in range(exit_column, mouse_column):
                                    r[j] = 0

                    # para quando o mouse estiver uma linha depois do exit
                    elif e_row == exit_row + 1:
                        # print(r)
                        for j in range(mouse_column + 1, exit_column+1):
                            r[j] = 0

                        for j in range(exit_column, mouse_column):
                            r[j] = 0

                # bottom
                elif exit_row > mouse_row:
                    # print('bottom')
                    if e_row > mouse_row:

                        if e_row < exit_row:
                            # Descendo com uma reta até a linha da saida - 1
                            r[mouse_column] = 0



                            if exit_column > mouse_column and e_row == exit_row - 1:
                                print(r)
                                for j in range(mouse_column + 1, exit_column + 1):
                                    r[j] = 0

                            if exit_column < mouse_column and e_row == exit_row - 1:
                                for j in range(exit_column, mouse_column):
                                    r[j] = 0

                    # para quando o mouse estiver uma linha antes do exit
                    elif e_row == exit_row - 1:
                        # print(r)
                        for j in range(mouse_column + 1, exit_column + 1):
                            r[j] = 0

                        for j in range(exit_column, mouse_column):
                            r[j] = 0

            # left and right
            else:
                # left
                if exit_column < mouse_column:
                    # print('left')

                    if e_row == mouse_row:
                        for j in range(exit_column + 1, mouse_column):
                            r[j] = 0

                    if e_row >= exit_row and e_row < mouse_row:
                        r[exit_column + 1] = 0

                    if e_row <= exit_row and e_row > mouse_row:
                        """
                            [   [1,   1,  1, 1, 1],
                                [1,   1,  1, 1, 1],
                                [1,  'm', 1, 1, 1],
                                ['e', 1,  1, 1, 1],
                                [1,   1,  1, 1, 1]
                            ]
                        """
                        r[exit_column + 1] = 0

                # right
                elif exit_column > mouse_column:
                    # print('right')

                    if e_row == mouse_row:
                        for j in range(mouse_column + 1, exit_column):
                            r[j] = 0


                    if e_row >= exit_row and e_row < mouse_row:
                        r[exit_column - 1] = 0

                    if e_row <= exit_row and e_row > mouse_row:
                        """
                            [   [1,   1,  1, 1, 1],
                                [1,   1,  1, 1, 1],
                                [1,  'm', 1, 1, 1],
                                ['e', 1,  1, 1, 1],
                                [1,   1,  1, 1, 1]
                            ]
                        """
                        r[exit_column - 1] = 0

    # left, right, top, bottom
    def generate_area(self):
        return randint(0, 3)

    def move_mouse(self, current_row, current_column, direction):
        row = current_row
        column = current_column

        if direction == 'top':
            row -= 1

        elif direction == 'bottom':
            row += 1

        elif direction == 'left':
            column -= 1

        elif direction == 'right':
            column += 1

        if row < 0 or column < 0:
            return False

        if row >= len(self.maze) or column >= len(self.maze[0]):
            return False

        if self.maze[row][column] in [0, 'e']:
            return True, (row, column)

        return False

    def run(self):

        # Pegando a posição inicial do mouse
        self.stack.append((self.currentCell['row'], self.currentCell['column']))

        while len(self.stack) > 0:
            current = self.stack.pop()

            current_row = current[0]
            current_column = current[1]

            print("Posição atual", current_row, current_column)

            # Encontrou a saida
            if self.maze[current_row][current_column] == 'e':
                self.history_stack.append([self.stack.copy(), (current_row, current_column)])
                return True

            # Já passou por aqui
            if self.maze[current_row][current_column] == '.':
                continue

            # Marcando . por onde passou
            for er, r in enumerate(self.maze):
                for ec, c in enumerate(r):
                    if c == 'm':
                        self.maze[er][ec] = '.'

            # mouse
            self.maze[current_row][current_column]  = 'm'


            top = self.move_mouse(current_row, current_column, "top")

            if not top:
                pass
            else:
                self.stack.append(top[1])

            bottom = self.move_mouse(current_row, current_column, "bottom")

            if not bottom:
                pass
            else:
                self.stack.append(bottom[1])

            left = self.move_mouse(current_row, current_column, "left")


            if not left:
                pass
            else:
                self.stack.append(left[1])

            right = self.move_mouse(current_row, current_column, "right")

            if not right:
                pass
            else:
                self.stack.append(right[1])

            self.history_maze.append(copy.deepcopy(self.maze))
            self.history_stack.append([self.stack.copy(), (current_row, current_column)])

        return False
