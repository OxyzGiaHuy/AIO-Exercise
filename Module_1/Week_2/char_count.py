def count_chars(string):
    dict_freq = {}
    for letter in string:
        if letter == " ":
            continue
        if letter not in dict_freq:
            dict_freq[letter] = 1
        else:
            dict_freq[letter] += 1
    return dict_freq


if __name__ == "__main__":
    string = "Thai Gia Huy hoc AI Viet Nam"
    print(count_chars(string))
