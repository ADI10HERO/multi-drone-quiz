import time
from result import *

inf = 10e9 + 7


def get_dt(n, vec, dt_vec):

    v = np.zeros(n, dtype=int)
    z = np.full(n + 1, np.inf)

    k = 0
    z[0] = -inf
    z[1] = inf

    for q in range(1, n):
        if vec[q] == inf:
            continue

        s = ((vec[q] + q**2) - (vec[v[k]] + v[k] ** 2)) / (2 * (q - v[k]))
        while s <= z[k]:
            k -= 1
            s = (vec[q] + q**2 - (vec[v[k]] + v[k] ** 2)) / (2 * (q - v[k]))

        k += 1
        v[k] = q
        z[k] = s
        z[k + 1] = np.inf

    k = 0
    for q in range(n):
        while k + 1 <= (n - 1) and z[k + 1] < q:
            k += 1
        dt_vec[q] = (q - v[k]) ** 2 + vec[v[k]]
    return dt_vec


def calculate_distance_row(m, n, grid):
    dist_transform = np.zeros_like(grid)
    for i in range(m):
        dist_transform[i, :] = get_dt(n, grid[i, :], np.zeros(n))
    return dist_transform


def calculate_distance_col(m, n, dist_transform):
    for i in range(n):
        dist_transform[:, i] = get_dt(m, dist_transform[:, i], np.zeros(m))
    return dist_transform


def esdf(M, N, obstacle_list):
    """
    :param M: Row number
    :param N: Column number
    :param obstacle_list: Obstacle list
    :return: An array. The value of each cell means the closest distance to the obstacle
    """

    # preparing grids
    grid = np.full((M, N), inf)
    for (i, j) in obstacle_list:
        grid[i, j] = 0

    dist_transform = calculate_distance_row(M, N, grid)
    dist_transform = calculate_distance_col(M, N, dist_transform)

    dist_transform = np.sqrt(dist_transform)
    return dist_transform


if __name__ == "__main__":
    st = time.time()
    for _ in range(int(2e4)):
        assert np.array_equal(esdf(M=3, N=3, obstacle_list=[[0, 1], [2, 2]]), res_1)
        assert np.array_equal(
            esdf(M=4, N=5, obstacle_list=[[0, 1], [2, 2], [3, 1]]), res_2
        )

    et = time.time()
    print(et - st)
