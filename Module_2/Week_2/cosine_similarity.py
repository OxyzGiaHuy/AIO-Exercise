import numpy as np


def compute_cosine(v1, v2):
    norm_1 = np.linalg.norm(v1)
    norm_2 = np.linalg.norm(v2)
    return np.dot(v1, v2)/(norm_1*norm_2)


if __name__ == "__main__":
    x = np.array([1, 2, 3, 4])
    y = np.array([1, 0, 3, 0])
    print(compute_cosine(x, y))
