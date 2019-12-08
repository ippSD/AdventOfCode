# --- Day 4: Secure Container ---
#
# You arrive at the Venus fuel depot only to discover it's protected by a
# password. The Elves had written the password on a sticky note, but someone
# threw it out.
#
# However, they do remember a few key facts about the password:
#
#     It is a six-digit number.
#     The value is within the range given in your puzzle input.
#     Two adjacent digits are the same (like 22 in 122345).
#     Going from left to right, the digits never decrease; they only ever
#     increase or stay the same (like 111123 or 135679).
#
# Other than the range rule, the following are true:
#
#     111111 meets these criteria (double 11, never decreases).
#     223450 does not meet these criteria (decreasing pair of digits 50).
#     123789 does not meet these criteria (no double).
#
# How many different passwords within the range given in your puzzle input
# meet these criteria?
#
# Your puzzle input is XXXXXX-XXXXXX.


def get_input():
    with open("input", 'r') as f:
        content = f.read()
        pass
    _lb, _ub = content.split('-', 2)
    return int(_lb), int(_ub)


def is_double(x):
    return any([x2 == x1 for x1, x2 in zip(x[0:-1], x[1:])])


def is_double_v2(x):
    return any([x.count(str(i)) == 2 for i in range(0, 10)])


def is_asc(x):
    return all([x2 >= x1 for x1, x2 in zip(x[0:-1], x[1:])])


def combinations(l, u):
    score = 0
    for i in range(l, u):
        n = list(str(i))
        cond = is_double(n) and is_asc(n)
        if cond:
            score = score + 1
            pass
        pass
    return score


def combinations_v2(l, u):
    score = 0
    for i in range(l, u):
        n = list(str(i))
        cond = is_double_v2(n) and is_asc(n)
        if cond:
            score = score + 1
            pass
        pass
    return score


if __name__ == "__main__":
    lb, ub = get_input()

    p1 = combinations(lb, ub)
    print("Part 1:", p1)

    p2 = combinations_v2(lb, ub)
    print("Part 2:", p2)

    with open("output", 'w') as f:
        f.write("{0}\n{1}".format(p1,  p2))
        pass
    pass
