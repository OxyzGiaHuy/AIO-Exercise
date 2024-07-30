import numpy as np


def compute_vector_length(vector):
    len_of_vector = np.sqrt(np.sum(vector**2))
    return len_of_vector


def compute_dot_product(vector1, vector2):
    result = sum([v1*v2 for v1, v2 in zip(vector1, vector2)])
    return result


def matrix_multi_vector(matrix, vector):
    m = matrix.shape[0]
    c = np.zeros(m)
    for i in range(m):
        c[i] = compute_dot_product(matrix[i], vector)
    return c


def matrix_multi_matrix(matrix1, matrix2):
    m = matrix1.shape[0]
    k = matrix2.shape[1]
    c = np.zeros((m, k))
    for i in range(m):
        for j in range(k):
            c[i][j] = compute_dot_product(matrix1[i], matrix2[:, j])
    return c


def inverse_matrix(matrix):
    a = matrix[0, 0]
    b = matrix[0, 1]
    c = matrix[1, 0]
    d = matrix[1, 1]
    det = a*d - b*c
    if det == 0:
        return "Cant be invertible"
    else:
        inv_mat = (np.array([[d, -b],
                            [-c,  a]]))/det
        return inv_mat


# using np.linalg
def inv_mat(matrix):
    return np.linalg.inv(matrix)


def compute_eigenvalues_eigenvectors(matrix):
    return np.linalg.eig(matrix)


if __name__ == "__main__":
    # 1.1
    v1 = np.array([3, 4])
    print("\n1.1:")
    print(compute_vector_length(v1))
    # 1.2
    print("\n1.2:")
    v2 = np.array([5, 6])
    print(compute_dot_product(v1, v2))
    # 1.3
    m1 = np.array([[1, 2],
                   [3, 4],
                   [5, 6]])
    print("\n1.3:")
    print(matrix_multi_vector(m1, v1))
    # 1.4
    m2 = np.array([[2, 7, 10, 5],
                   [1, 4,  3, 6]])
    print("\n1.4:")
    print(matrix_multi_matrix(m1, m2))
    # 1.5
    mat = np.array([[1, 5],
                    [3, 9]])
    print("\n1.5:")
    print(inverse_matrix(mat))
    # 1.5 using np.linalg
    print("\n1.5-linalg:")
    mat1 = np.array([[1, 2, 3],
                     [2, 3, 1],
                     [3, 1, 2]])
    print(inv_mat(mat1))
    # 2
    print("\n2-eigen:")
    mat2 = np.array([[0.9, 0.2],
                     [0.1, 0.8]])
    eigenvalues, eigenvectors = compute_eigenvalues_eigenvectors(mat2)
    print("Eigenvalues:", eigenvalues)
    print("Eigenvectors:\n", eigenvectors)
