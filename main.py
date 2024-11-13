from random import choice
from math import floor


# 创建初始矩阵
def matrix_create():
    game_matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    matrix_element_create(game_matrix)
    return game_matrix


# 判断矩阵是否有“空”元素
def matrix_empty_judge(game_matrix):
    element_list = []
    for i, ii in zip(game_matrix, range(0, 4)):
        for j, jj in zip(i, range(0, 4)):
            if j:
                pass
            else:
                temp_mark = 4 * ii + jj
                element_list.append(temp_mark)
    return element_list


def matrix_element_create(game_matrix):
    if matrix_empty_judge(game_matrix):
        number_random = choice(matrix_empty_judge(game_matrix))

        row = floor(number_random / 4)
        col = number_random % 4

        temp_random = [2, 4]
        game_matrix[row][col] = choice(temp_random)
    return game_matrix


def matrix_check_row(game_matrix):
    for i in game_matrix:
        for jj in range(0, 3):
            if i[jj] == i[jj + 1]:
                return True
    return False


def martix_check_col(game_matrix):
    for ii in range(0, 3):
        for jj in range(0, 4):
            if game_matrix[ii][jj] == game_matrix[ii + 1][jj]:
                return True
    return False


def matrix_check(game_matrix):
    if matrix_empty_judge(game_matrix):
        return True
    else:
        if matrix_check_row(game_matrix) or martix_check_col(game_matrix):
            return True
        else:
            return False


def matrix_move_left(game_matrix):
    for ii in range(0, 4):
        for jj in range(1, 4, 1):
            for kk in range(1, 4, 1):
                if game_matrix[ii][kk - 1] == game_matrix[ii][kk]:
                    game_matrix[ii][kk - 1] *= 2
                    game_matrix[ii][kk] = 0
                if game_matrix[ii][kk - 1] == 0:
                    game_matrix[ii][kk - 1] = game_matrix[ii][kk]
                    game_matrix[ii][kk] = 0
    return game_matrix


def matrix_move_right(game_matrix):
    for ii in range(0, 4):
        for jj in range(2, -1, -1):
            for kk in range(2, -1, -1):
                if game_matrix[ii][kk + 1] == game_matrix[ii][kk]:
                    game_matrix[ii][kk + 1] *= 2
                    game_matrix[ii][kk] = 0
                if game_matrix[ii][kk + 1] == 0:
                    game_matrix[ii][kk + 1] = game_matrix[ii][kk]
                    game_matrix[ii][kk] = 0
    return game_matrix


def matrix_move_up(game_matrix):
    for ii in range(1, 4, 1):
        for jj in range(0, 4):
            for kk in range(1, 4, 1):
                if game_matrix[kk - 1][jj] == game_matrix[kk][jj]:
                    game_matrix[kk - 1][jj] *= 2
                    game_matrix[kk][jj] = 0
                if game_matrix[kk - 1][jj] == 0:
                    game_matrix[kk - 1][jj] = game_matrix[kk][jj]
                    game_matrix[kk][jj] = 0
    return game_matrix


def matrix_move_down(game_matrix):
    for ii in range(2, -1, -1):
        for jj in range(0, 4):
            for kk in range(2, -1, -1):
                if game_matrix[kk + 1][jj] == game_matrix[kk][jj]:
                    game_matrix[kk + 1][jj] *= 2
                    game_matrix[kk][jj] = 0
                if game_matrix[kk + 1][jj] == 0:
                    game_matrix[kk + 1][jj] = game_matrix[kk][jj]
                    game_matrix[kk][jj] = 0
    return game_matrix


def matrix_operate(game_matrix):
    matrix_operation = input("move with w-a-s-d"'\n')
    if matrix_operation == 'a':
        game_matrix = matrix_move_left(game_matrix)
    elif matrix_operation == 'w':
        game_matrix = matrix_move_up(game_matrix)
    elif matrix_operation == 's':
        game_matrix = matrix_move_down(game_matrix)
    elif matrix_operation == 'd':
        game_matrix = matrix_move_right(game_matrix)
    else:
        print("error,with w-a-s-d")
        matrix_operate(game_matrix)
    game_matrix = matrix_element_create(game_matrix)


def matrix_markup(game_matrix):
    matrix_max_element = 2
    for i in game_matrix:
        for j in i:
            if j > matrix_max_element:
                matrix_max_element = j
    return matrix_max_element


def matrix_disp(game_matrix):
    print("-" * 14)
    for i in game_matrix:
        print("|", end="")
        for j in i:
            if j:
                print("{:^3d}".format(j), end="")
            else:
                print(" " * 3, end="")
        print("|")
    print("-" * 14)


def matrix_2048():
    game_matrix = matrix_create()
    matrix_disp(game_matrix)
    print("")
    while matrix_check(game_matrix):
        matrix_operate(game_matrix)
        matrix_disp(game_matrix)
        print("")
    print("Game over.Best Grade:{}".format(matrix_markup(game_matrix)))
    temp_mark = input("Game Again?Enter *")
    if temp_mark == '*':
        matrix_2048()


def main():
    matrix_2048()


if __name__ == "__main__":
    main()
