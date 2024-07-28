import numpy as np


def create_train_data():
    data = [['Sunny', 'Hot', 'High', 'Weak', 'no'],
            ['Sunny', 'Hot', 'High', 'Strong', 'no'],
            ['Overcast', 'Hot', 'High', 'Weak', 'yes'],
            ['Rain', 'Mild', 'High', 'Weak', 'yes'],
            ['Rain', 'Cool', 'Normal', 'Weak', 'yes'],
            ['Rain', 'Cool', 'Normal', 'Strong', 'no'],
            ['Overcast', 'Cool', 'Normal', 'Strong', 'yes'],
            ['Overcast', 'Mild', 'High', 'Weak', 'no'],
            ['Sunny', 'Cool', 'Normal', 'Weak', 'yes'],
            ['Rain', 'Mild', 'Normal', 'Weak', 'yes']]
    return np.array(data)


def compute_prior_probablity(train_data):
    y_unique = ['no', 'yes']
    prior_probability = np.zeros(len(y_unique))
    target = train_data[:, 4]
    prior_probability[0] = np.count_nonzero(
        train_data[:, 4] == "no")/len(train_data)
    prior_probability[1] = np.count_nonzero(
        train_data[:, 4] == "yes")/len(train_data)
    return prior_probability


def compute_conditional_probability(train_data):
    y_unique = ['no', 'yes']
    conditional_probability = []
    list_x_name = []

    for i in range(train_data.shape[1] - 1):
        x_unique = np.unique(train_data[:, i])
        list_x_name.append(x_unique)
        x_conditional_probability = np.zeros((len(x_unique), len(y_unique)))

        for j, label in enumerate(y_unique):
            scale_data = train_data[train_data[:, -1] == label]
            for k, feature_data in enumerate(x_unique):
                x_conditional_probability[k][j] = np.sum(
                    scale_data[:, i] == feature_data)/len(scale_data)

        conditional_probability.append(x_conditional_probability)
    return conditional_probability, list_x_name


def get_index_from_value(feature_name, list_features):
    return np.where(list_features == feature_name)[0][0]


# Train Naive Bayes Model
def train_naive_bayes(train_data):
    # Step 1: Calculate Prior Probability
    y_unique = ['no', 'yes']
    prior_probability = compute_prior_probablity(train_data)

    # Step 2: Calculate Conditional Probability
    conditional_probability, list_x_name = compute_conditional_probability(
        train_data)

    return prior_probability, conditional_probability, list_x_name


# Prediction
def prediction_play_tennis(X, list_x_name, prior_probability, conditional_probability):
    x1 = get_index_from_value(X[0], list_x_name[0])
    x2 = get_index_from_value(X[1], list_x_name[1])
    x3 = get_index_from_value(X[2], list_x_name[2])
    x4 = get_index_from_value(X[3], list_x_name[3])
    p_0 = prior_probability[0] * conditional_probability[0][x1, 0] * conditional_probability[1][x2, 0] * \
           conditional_probability[2][x3, 0] * conditional_probability[3][x4, 0]
    p_1 = prior_probability[1] * conditional_probability[0][x1, 1] * conditional_probability[1][x2, 1] * \
            conditional_probability[2][x3, 1] * conditional_probability[3][x4, 1]
    print(p_0, p_1)
    if p_0 > p_1:
        y_pred = 0
    else:
        y_pred = 1
    return y_pred


# 4.1
train_data = create_train_data()
print(train_data)


# 4.2
prior_probablity = compute_prior_probablity(train_data)
print("P(play tennis = No) =", prior_probablity[0])
print("P(play tennis = Yes) =", prior_probablity[1])


# 4.3
conditional_probability, list_x_name = compute_conditional_probability(
    train_data)
print("x1 = ", list_x_name[0])
print("x2 = ", list_x_name[1])
print("x3 = ", list_x_name[2])
print("x4 = ", list_x_name[3])


# 4.4
# cau 16
train_data = create_train_data()
_, list_x_name = compute_conditional_probability(train_data)
outlook = list_x_name[0]

i1 = get_index_from_value("Overcast", outlook)
i2 = get_index_from_value("Rain", outlook)
i3 = get_index_from_value("Sunny", outlook)

print(i1, i2, i3)

# cau 17
train_data = create_train_data()
conditional_probability, list_x_name = compute_conditional_probability(
    train_data)
# Compute P("Outlook" = "Sunny"| Play Tennis = "yes")
x1 = get_index_from_value("Sunny", list_x_name[0])
print("P(Outlook = 'Sunny' | Play Tennis = 'yes') = ",
      np.round(conditional_probability[0][x1, 1], 2))

# cau 18
# Compute P(" Outlook "=" Sunny "| Play Tennis "=" No ")
x1 = get_index_from_value("Sunny", list_x_name[0])
print("P('Outlook' = 'Sunny' | Play Tennis = 'No') = ",
      np.round(conditional_probability[0][x1, 0], 2))


# 4.6
X = ['Sunny', 'Cool', 'High', 'Strong']
data = create_train_data()
prior_probability, conditional_probability, list_x_name = train_naive_bayes(data)
pred = prediction_play_tennis(X, list_x_name, prior_probability, conditional_probability)

if pred:
    print("Ad should go!")
else:
    print("Ad should not go!")
