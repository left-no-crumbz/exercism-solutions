# x y
# inner circle = (0,1), (1,0), (-1,0), (0,-1)
# middle circle = (0,5), (5,0), (-5,0), (0,-5)
# outer circle = (0,10), (10,0), (-10,0), (0,-10)

def score(x, y):
    hypotenuse = (x ** 2 + y ** 2) ** 0.5
    if hypotenuse <= 1:
        return 10
    if hypotenuse <= 5:
        return 5
    if hypotenuse <= 10:
        return 1
    return 0

print(score(-3.5, 3.5))