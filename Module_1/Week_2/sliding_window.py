def sliding_window(num_list, k):
    if k < 1:
        return []
    else:
        return [max(num_list[i: i+k]) for i in range(len(num_list) - k + 1)]


if __name__ == "__main__":
    num_list = list(map(int, input("Enter an integer list: ").split()))
    k = int(input("k = "))
    print(sliding_window(num_list, k))
