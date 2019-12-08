import numpy as np

with open("input", 'r') as f:
    content = f.read()
    pass

wire1, wire2, _ = tuple(content.split('\n', 3))

def instruction2points(instr):
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

points1 = instruction2points(wire1)
points2 = instruction2points(wire2)

with open("out1.dat", 'w') as f:
    for point in points1:
        f.write(f"{','.join([str(xx) for xx in point.tolist()])}\n")
        pass
    pass
with open("out2.dat", 'w') as f:
    for point in points2:
        f.write(f"{','.join([str(xx) for xx in point.tolist()])}\n")
        pass
    pass


sols = list()
sols_min = -1
for x11, x12 in zip(points1[0:-1], points1[1:]):
    for x21, x22 in zip(points2[0:-1], points2[1:]):
        u1, u2 = x12 - x11, x22 - x21
        d1 = np.linalg.norm(u1)
        d2 = np.linalg.norm(u2)
        u1 = u1 / d1
        u2 = u2 / d2
        u_mat = np.zeros((2,2))
        u_mat[:, 0] = u1
        u_mat[:, 1] = -u2
        try:
            lambdas = np.linalg.solve(a=u_mat, b=x21-x11)
            if 0e0 <= lambdas[0] <= d1 and 0e0 <= lambdas[1] <= d2:
                p = x11 + u1 * lambdas[0]
                p = p.astype(int)
                print(x11, x12, x21, x22, p)
                sols.append(p)
                distance = np.sum(np.abs(p))
                sols_min = sols_min if sols_min > 0 and sols_min < distance else distance
                pass
            pass
        except Exception:
            continue
        pass
    pass
# print(sols)


print("Part 1:", sols_min)


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

l1 = intersection_lens(wire1, sols)
l2 = intersection_lens(wire2, sols)
dd = dict()
for k in l1.keys():
    dd[k] = l1[k] + l2[k]
    pass

print(dd)
#print(len(l2), l2)
print("Part 2:", min(dd.values()))

