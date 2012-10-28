
def rotations(x):
    if not isinstance(x, str):
        x = str(x)
    for i in range(len(x)):
        yield x[i:] + x[:i]

