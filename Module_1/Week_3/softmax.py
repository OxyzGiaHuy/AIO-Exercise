import torch
import torch.nn as nn


class MySoftmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x_exp = torch.exp(x)
        sum_exp = x_exp.sum(0, keepdim=True)
        return x_exp/sum_exp


class MySoftmaxStable(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x_max = torch.max(x, dim=0, keepdim=True)
        x_exp = torch.exp(x - x_max.values)
        sum_exp = x_exp.sum(0, keepdim=True)
        return x_exp/sum_exp


data = torch.Tensor([1, 2, 300_000_000])
softmax = MySoftmax()
output1 = softmax(data)
print(output1)
print(round(output1[0].item(), 2))

data = torch.Tensor([1, 2, 3])
softmax_stable = MySoftmaxStable()
output2 = softmax_stable(data)
print(round(output2[-1].item(), 2))
print(output2)
