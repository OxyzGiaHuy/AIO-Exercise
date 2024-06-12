def calc_f1_score(tp, fp, fn):
    precision = tp/(tp+fp)
    recall = tp/(tp+fn)
    f1_score = 2*precision*recall/(precision+recall)
    return f1_score


def exercise1(tp, fp, fn):
    if not isinstance(tp, int) or not isinstance(fp, int) or not isinstance(fn, int):
        return "tp, fp and fn must be int"
    else:
        if tp > 0 and fp > 0 and fn > 0:
            precision = tp/(tp+fp)
            recall = tp/(tp+fn)
            f1_score = calc_f1_score(tp, fp, fn)
            print(f"precision is {precision}")
            print(f"recall is {recall}")
            return f"f-1 score is {f1_score}"
        else:
            return "tp and fp and fn must be greater than zero"
