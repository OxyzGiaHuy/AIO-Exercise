import random
import math


def cal_mae(y_i, y_i_hat, num_samples):
    differences = [abs(pred - target) for pred, target in zip(y_i, y_i_hat)]
    return sum(differences)/num_samples


def cal_mse(y_i, y_i_hat, num_samples):
    differences = [(pred - target)**2 for pred, target in zip(y_i, y_i_hat)]
    return sum(differences)/num_samples


def cal_rmse(y_i, y_i_hat, num_samples):
    return math.sqrt(cal_mse(y_i, y_i_hat, num_samples))


def exercise3():
    num_samples = input("Enter number of samples (integer number): ")
    if not num_samples.isnumeric():
        return "number of samples must be a number"
    num_samples = int(num_samples)

    for i in range(0, num_samples):
        y_i = y_i.append(y_i, random.uniform(0, 10))
        y_i_hat = y_i_hat.append(y_i_hat, random.uniform(0, 10))

    loss_name = input("Enter loss name: ")
    func_name = {
        "MSE": cal_mse,
        "MAE": cal_mae,
        "RMSE": cal_rmse
    }

    for i in range(0, num_samples):
        loss_func = func_name.get(loss_name.upper())
        print(f"loss name: {loss_name}, sample: {i}, pred: {y_i_hat[i]}, target: {y_i[i]}, loss: {loss_func(y_i[i], y_i_hat[i], 1)}")
    print(f"final {loss_name.upper()}: {loss_func(y_i, y_i_hat, num_samples)}")


# Trac nghiem cau 7
def calc_ae(y, y_hat):
    return abs(y - y_hat)


y = 1
y_hat = 6
assert calc_ae(y, y_hat) == 5
y = 2
y_hat = 9
print(calc_ae(y, y_hat))
# Output: 7


# Trac nghiem cau 8
def calc_se(y, y_hat):
    return abs(y - y_hat)**2


y = 4
y_hat = 2
assert calc_se(y, y_hat) == 4
print(calc_se(2, 1))
