import math


def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True


def sigmoid(x):
    return 1/(1 + math.e**(-x))


def relu(x):
    if x > 0:
        return x
    else:
        return 0


def elu(alpha, x):
    if x > 0:
        return x
    else:
        return alpha*(math.exp(x) - 1)


def exercise2():
    x = input("Enter x: ")
    if not is_number(x):
        return "x must be a number"
    func_name = input("Enter the activation function (sigmoid, relu, elu): ")
    activation_name = ["sigmoid", "relu", "elu"]
    if func_name.lower() not in activation_name:
        return f"{func_name} is not supported"
    x = float(x)
    alpha = 0.01
    match func_name:
        case "sigmoid":
            return f"sigmoid({x}) = {sigmoid(x)}"
        case "relu":
            return f"relu({x}) = {relu(x)}"
        case "elu":
            return f"elu({x}) = {elu(alpha, x)}"

# Trac nghiem cau 6


def calc_activation_func(x, act_name):
    x = float(x)
    alpha = 0.01
    match act_name:
        case "sigmoid":
            return sigmoid(x)
        case "relu":
            return relu(x)
        case "elu":
            return elu(alpha, x)
