import math
def equation(x):
    return x ** 3 - 8 * x + 1 + 12 * math.sin(x) + 10 * math.cos(x)

def bisection_method(a, b, epsilon):
    steps = 0
    while (b - a) >= epsilon:
        midpoint = (a + b) / 2.0
        if equation(midpoint) == 0.0:
            return midpoint, steps
        elif equation(midpoint) * equation(a) < 0:
            b = midpoint
        else:
            a = midpoint
        steps += 1
    return (a + b) / 2.0, steps

def find_roots_on_interval(start, end, epsilon):
    roots = []
    current = start
    while current <= end:
        x1 = current
        x2 = current + 0.1
        if equation(x1) * equation(x2) < 0:
            root, steps = bisection_method(x1, x2, epsilon)
            roots.append((root, steps))
        current += 0.1
    return roots

roots = find_roots_on_interval(-5, 5, 0.001)

for idx, (root, steps) in enumerate(roots):
    interval_start = round(idx * 0.1 - 5, 1)
    interval_end = round((idx + 1) * 0.1 - 5, 1)
    print(f"Интервал [{interval_start:.1f};{interval_end:.1f}]")
    print(f"Решение: {round(root, 3)}")
    print(f"Число шагов: {steps}")
