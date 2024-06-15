def levenshtein(source, target):
    m = len(source) + 1
    n = len(target) + 1
    D = [[0 for _ in range(n)] for _ in range(m)]

    D[0] = [i for i in range(n)]
    for i in range(m):
        D[i][0] = i

    for i in range(1, m):
        for j in range(1, n):
            if source[i-1] == target[j-1]:
                D[i][j] = D[i-1][j-1]
            else:
                D[i][j] = min(D[i-1][j-1], D[i-1][j], D[i][j-1]) + 1

    print("D =")
    for i in range(len(D)):
        print(D[i])

    return D[m-1][n-1]


if __name__ == "__main__":
    source = "intention"
    target = "execution"
    distance = levenshtein(source, target)
    print(f"Levenshstein distance of '{source}' and '{target}' is {distance}.")
