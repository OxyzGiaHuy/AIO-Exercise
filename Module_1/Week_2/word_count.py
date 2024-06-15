import os


def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()


def word_count(file_path):
    sentences = read_file(file_path)
    text = sorted(sentences.lower().split())
    dict_freq = {}
    for word in text:
        if word not in dict_freq:
            dict_freq[word] = 1
        else:
            dict_freq[word] += 1
    return dict_freq


if __name__ == "__main__":
    file_path = os.path.dirname(__file__) + "/P1_data.txt"
    print(word_count(file_path))
