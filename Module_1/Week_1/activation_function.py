import math

def is_number (n):
    try:
        float (n)
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

# Trac nghiem cau 2
assert is_number(3) == 1.0
assert is_number('-2a') == 0.0
print(is_number(1))
print(is_number('n'))
# Output:   True
#           False

#Trac nghiem cau 4
assert round(sigmoid(3), 2) == 0.95
print(round(sigmoid(2), 2))
# Output: 0.88

# Trac nghiem cau 5
assert round(elu(0.01, 1)) == 1
print(round(elu(0.01, -1), 2))
# Output: -0.01

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
        
assert calc_activation_func(x = 1, act_name = 'relu') == 1
print(round(calc_activation_func(x = 3, act_name = 'sigmoid'), 2))
# Output: 0.95