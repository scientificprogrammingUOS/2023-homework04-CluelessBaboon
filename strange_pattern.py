import numpy as np

# implement the function strange pattern

def strange_pattern(shape):

    n = shape[0]
    m = shape [1]
    if n==0 and m==0:
        return np.empty((0,))
    if not isinstance(n, int):
        n = 10
    if not isinstance(m, int):
        m = 10

    new_array = np.zeros((n, m), dtype=bool)
    new_array[::3, ::3] = True
    new_array[1::3, 2::3] = True
    new_array[2::3, 1::3] = True

    return new_array

if __name__ == "__main__":
    pass
