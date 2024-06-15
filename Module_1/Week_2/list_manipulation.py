# Trac nghiem 5
def check_the_number(n):
    list_of_numbers = []
    results = ""
    for i in range(1, 5):
        list_of_numbers.append(i)
    if n in list_of_numbers:
        results = " True "
    if n not in list_of_numbers:
        results = " False "
    return results


print("---Trac nghiem 5---")
n = 7
assert check_the_number(n) == " False "
n = 2
results = check_the_number(n)
print(results)


# Trac nghiem 6
def my_function6(data, max, min):
    result = []
    for i in data:
        if i < min:
            result.append(min)
        elif i > max:
            result.append(max)
        else:
            result.append(i)
    return result


print("---Trac nghiem 6---")
my_list = [5, 2, 5, 0, 1]
max = 1
min = 0
assert my_function6(max=max, min=min, data=my_list) == [1, 1, 1, 0, 1]
my_list = [10, 2, 5, 0, 1]
max = 2
min = 1
print(my_function6(max=max, min=min, data=my_list))


# Trac nghiem 7
def my_function7(x, y):
    x.extend(y)
    return x


print("---Trac nghiem 7---")
list_num1 = ['a', 2, 5]
list_num2 = [1, 1]
list_num3 = [0, 0]
assert my_function7(list_num1, my_function7(list_num2, list_num3)) == [
    'a', 2, 5, 1, 1, 0, 0]

list_num1 = [1, 2]
list_num2 = [3, 4]
list_num3 = [0, 0]
print(my_function7(list_num1, my_function7(list_num2, list_num3)))


# Trac nghiem 8
def my_function8(n):
    mini = n[0]
    for num in n:
        if num < mini:
            mini = num
    return mini


print("---Trac nghiem 8---")
my_list = [1, 22, 93, -100]
assert my_function8(my_list) == -100

my_list = [1, 2, 3, -1]
print(my_function8(my_list))


# Trac nghiem 9
def my_function(n):
    maxi = n[0]
    for num in n:
        if num > maxi:
            maxi = num
    return maxi


print("---Trac nghiem 9---")
my_list = [1001, 9, 100, 0]
assert my_function(my_list) == 1001

my_list = [1, 9, 9, 0]
print(my_function(my_list))


# Trac nghiem 10
def my_function(integers, number=1):
    return any([(nums == number) for nums in integers])


print("---Trac nghiem 10---")
my_list = [1, 3, 9, 4]
assert my_function(my_list, -1) == False

my_list = [1, 2, 3, 4]
print(my_function(my_list, 2))


# Trac nghiem 11
def my_function(list_nums=[0, 1, 2]):
    var = 0
    for i in list_nums:
        var += i
    return var/len(list_nums)


print("---Trac nghiem 11---")
assert my_function([4, 6, 8]) == 6
print(my_function())


# Trac nghiem 12
def my_function(data):
    var = []
    for i in data:
        if i % 3 == 0:
            var.append(i)
    return var


print("---Trac nghiem 12---")
assert my_function([3, 9, 4, 5]) == [3, 9]
print(my_function([1, 2, 3, 5, 6]))


# Trac nghiem 13
def my_function(y):
    var = 1
    while (y > 1):
        var *= y
        y -= 1
    return var


print("---Trac nghiem 13---")
assert my_function(8) == 40320
print(my_function(4))


# Trac nghiem 14
def my_function(x):
    return x[::-1]


print("---Trac nghiem 14---")
x = 'I can do it'
assert my_function(x) == "ti od nac I"
x = 'apricot'
print(my_function(x))


# Trac nghiem 15
def function_helper(x):
    # Your code here
    # Neu x >0 tra ve ’T ’, nguoc lai tra ve ’N’
    if x > 0:
        return 'T'
    return 'N'


def my_function(data):
    res = [function_helper(x) for x in data]
    return res


print("---Trac nghiem 15---")
data = [10, 0, -10, -1]
assert my_function(data) == ['T', 'N', 'N', 'N']
data = [2, 3, 5, -1]
print(my_function(data))


# Trac nghiem 16
def function_helper(x, data):
    for i in data:
        if x == i:
            return 0
    return 1


def my_function(data):
    res = []
    for i in data:
        if function_helper(i, res):
            res . append(i)
    return res


print("---Trac nghiem 16---")
lst = [10, 10, 9, 7, 7]
assert my_function(lst) == [10, 9, 7]
lst = [9, 9, 8, 1, 1]
print(my_function(lst))
