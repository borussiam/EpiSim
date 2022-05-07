# Simulation 1

import numpy as np
import random


# 임의 크기의 공간(grid)를 생성하고 Susceptible 상태의 사람을 배치
def create_grid(rows, columns, boundary=True):
    if boundary:
        grid_init = np.zeros([rows + 2, columns + 2])
        grids_init = np.array(grid_init)
        # 경계(3으로 표현) 설정
        for i in range(rows):
            grids_init[i + 1][0] = 3
            grids_init[i + 1][columns + 1] = 3
        for i in range(columns + 2):
            grids_init[0][i] = 3
            grids_init[rows + 1][i] = 3
    else:
        grid_init = np.zeros([rows, columns])
        grids_init = np.array(grid_init)
    return grids_init


# (i, j)의 사람과 인접한 사람들 중 Susceptible 상태인 사람을 리스트에 저장
def find_susceptible(grid, i, j):
    susceptible = []
    if grid[i + 1][j] == 0:
        susceptible.append((i + 1, j))
    if grid[i - 1][j] == 0:
        susceptible.append((i - 1, j))
    if grid[i][j + 1] == 0:
        susceptible.append((i, j + 1))
    if grid[i][j - 1] == 0:
        susceptible.append((i, j - 1))
    return susceptible


def infected(grid):
    infected_list = []
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):
            if grid[i][j] == 1:
                infected_list.append((i, j))
    return infected_list


def recovered(grid):
    recovered_list = []
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):
            if grid[i][j] == 2:
                recovered_list.append((i, j))
    return recovered_list


# 감염된 사람의 이웃이 alpha의 확률로 감염된다
def infect_individual(grid, i, j, alpha):
    for person in find_susceptible(grid, i, j):
        if random.uniform(0, 1) <= alpha:
            grid[person[0]][person[1]] = 1


def infect_all(grid, alpha):
    for person in infected(grid):
        # infect_individual(grid, person[0], person[1], alpha)
        for p in find_susceptible(grid, person[0], person[1]):
            if random.uniform(0, 1) <= alpha:
                grid[p[0]][p[1]] = 1


def recover_all(grid, beta):
    for person in infected(grid):
        if random.uniform(0, 1) <= beta:
            grid[person[0]][person[1]] = 2
