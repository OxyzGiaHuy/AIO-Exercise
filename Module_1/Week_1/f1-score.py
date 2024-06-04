def calc_f1_score(tp, fp, fn):
    precision = tp/(tp+fp);
    recall = tp/(tp+fn);
    f1_score = 2*precision*recall/(precision+recall)
    return f1_score

def exercise1(tp, fp, fn):
    if (type(tp) != int) or (type(fp) != int) or (type(fn) != int):
        if type(tp) != int: 
            return "tp must be int"
        if type(fp) != int: 
            return "fp must be int"
        if type(fn) != int: 
            return "fn must be int"
        return
    else:
        if tp > 0 and fp > 0 and fn > 0:
            precision = tp/(tp+fp);
            recall = tp/(tp+fn);
            f1_score = calc_f1_score(tp, fp, fn)
            print(f"precision is {precision}")
            print(f"recall is {recall}")
            return f"f-1 score is {f1_score}"
        else:
            return "tp and fp and fn must be greater than zero"
        
# Trac nghiem cau 1
assert round(calc_f1_score(tp =2, fp =3, fn =5), 2) == 0.33
print(round(calc_f1_score(tp =2, fp =4, fn =5), 2))
# output: 0.31