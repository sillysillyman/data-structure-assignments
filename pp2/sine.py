#
# Compute sine and cosine
#

import math


def sine(x):
    # raise NotImplementedError
    if -0.01 < x < 0.01:
        return x - x**3 / 6
    return 2 * sine(x / 2) * cosine(x / 2)


def cosine(x):
    # raise NotImplementedError
    if -0.01 < x < 0.01:
        return 1 - x**2 / 2
    return 1 - 2 * sine(x / 2) ** 2


def tabulate(a, b, step):
    print(
        "%5s : %-10s %-10s %-10s %-10s"
        % ("x", "sine(x)", "cosine(x)", "math.sin(x)", "math.cos(x)")
    )
    for i in range(a, b + 1):
        x = step * i
        print(
            "%5g : %-10g %-10g %-10g %-10g"
            % (x, sine(x), cosine(x), math.sin(x), math.cos(x))
        )


if __name__ == "__main__":
    tabulate(-20, 20, 0.1)
