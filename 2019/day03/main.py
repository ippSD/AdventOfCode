import numpy as np


def get_input():
    with open("input", 'r') as f:
        content = f.read()
        pass
    wire1, wire2 = content.split('\n', 1)
    return wire1, wire2


def instructions_to_vertices(instr):
    x = np.zeros(2, dtype=int)
    ux = np.array([1, 0], dtype=int)
    uy = np.array([0, 1], dtype=int)
    xs = [x]
    for command in instr.split(','):
        direction = command[0]
        distance = int(command[1:])
        if direction == "R":
            x = x + distance * ux
        elif direction == "L":
            x = x - distance * ux
        elif direction == "U":
            x = x + distance * uy
        elif direction == "D":
            x = x - distance * uy
            pass
        xs.append(x)
        pass
    return xs


def manhattan_distance(x):
    return int(abs(x[0]) + abs(x[1]))


def intersection_point(x11, x12, x21, x22):
    u1, u2 = x12 - x11, x22 - x21
    d1 = int(np.linalg.norm(u1))
    d2 = int(np.linalg.norm(u2))
    u1 = u1 / d1
    u2 = u2 / d2
    u_mat = np.zeros((2, 2))
    u_mat[:, 0] = u1
    u_mat[:, 1] = -u2
    lambdas = np.linalg.solve(a=u_mat, b=x21 - x11)
    lamb1, lamb2 = int(lambdas[0]), int(lambdas[1])
    if 0 < lamb1 < d1 and 0 < lamb2 < d2:
        p = x11 + u1 * lamb1
        return p
    else:
        raise np.linalg.LinAlgError
    pass


def get_intersection_points(p1s, p2s):
    sols = list()
    sols_pos = list()
    sols_min = -1
    length = 0
    lens = list()
    for idx1, x1s in enumerate(zip(p1s[0:-1], p1s[1:])):
        x11, x12 = x1s
        for x21, x22 in zip(p2s[0:-1], p2s[1:]):
            try:
                p = intersection_point(x11, x12, x21, x22)
                dp = manhattan_distance(p - x11)
                lp = manhattan_distance(p)
                sols.append(p)
                sols_pos.append(idx1)
                sols_min = sols_min if 0 < sols_min < lp else lp
                length = length + dp
                lens.append(length)
                length = length - dp + manhattan_distance(x12 - x11)
                break
                pass
            except np.linalg.LinAlgError as e:
                continue
            pass
        else:
            length = length + manhattan_distance(x12 - x11)
        pass
    return sols, sols_min, sols_pos, lens


def intersection_lens(instr, intersecs):
    dic = dict()
    for key in range(0, len(intersecs)):
        dic[key] = 0
        pass
    x = np.zeros(2, dtype=int)
    ux = np.array([1, 0], dtype=int)
    uy = np.array([0, 1], dtype=int)
    lens = list()
    l = 0
    for command in instr.split(','):
        direction = command[0]
        distance = int(command[1:])
        if direction == "R":
            u = ux
        elif direction == "L":
            u = -ux
        elif direction == "U":
            u = uy
        elif direction == "D":
            u = -uy
            pass
        x_next = x + distance * u
        for dl in range(0, distance):
            xx = x + dl * u
            if any([np.sum(yy - xx) == 0 for yy in intersecs]):
                idx = np.where([np.sum(yy - xx) == 0 for yy in intersecs])
                l = l + dl
                lens.append(l)
                if dic[idx[0][0]] == 0:
                    dic[idx[0][0]] = l
                l = distance - dl
                x = x_next
                break
            pass
        else:
            l = l + distance
            x = x_next
            pass
        pass
    print(dic)
    return dic  # lens


def len_to_intersection(inters, ps, idxs):
    sols = list()
    sols_pos = list()
    sols_min = -1
    ids: list = idxs.copy()
    idx = ids[0]
    ids.pop(0)
    lens = dict()
    for idx1, xs in enumerate(zip(ps[0:-1], ps[1:])):
        x1, x2 = xs
        d = int(np.linalg.norm(x2 - x1))


if __name__ == "__main__":
    w1, w2 = get_input()
    points1 = instructions_to_vertices(w1)
    points2 = instructions_to_vertices(w2)

    solutions1, sol1, positions1, lens1 = get_intersection_points(
        points1,
        points2
    )
    solutions2, sol2, positions2, lens2 = get_intersection_points(
        points2,
        points1
    )
    print("Part 1:", sol1)
    print(len(solutions1), lens1)
    print(len(solutions2), lens2)

    ll = list()

    for idx1, sol1 in enumerate(solutions1):
        print("Sol1: ", sol1)
        for idx2, sol2 in enumerate(solutions2):
            if np.linalg.norm(sol1 - sol2) == 0:
                print("Sol2: ", sol2)
                ll.append(lens1[idx1] + lens2[idx2])
                pass
            pass
        pass

    print(ll)
    print("Part 2:", min(ll))
    pass
