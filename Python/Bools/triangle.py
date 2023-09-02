def is_triangle(sides):
    return all(side > 0 for side in sides) and sum(sides) - max(sides) > max(sides)


def equilateral(sides):
    return is_triangle(sides) and all(sides[0] == side for side in sides)


def isosceles(sides):
    return is_triangle(sides) and any(sides[i] == sides[j] for i in range(3) for j in range(i+1, 3))


def scalene(sides):
    return is_triangle(sides) and not(equilateral(sides) or isosceles(sides))