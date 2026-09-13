import torch
import torch.nn as nn

torch.manual_seed(0)

X = torch.tensor([[1.0], [2.0]])
Y = X * torch.tensor([[2, 3]]) + torch.tensor([3, 4])

class TinyModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(1, 2)

    def forward(self, x):
        return self.linear(x)

def get_loss(model, x, y):
    loss_fn = nn.MSELoss()
    pred = model(x)
    loss = loss_fn(pred, y)
    print("==> loss:", loss)

if __name__ == "__main__":
    model = TinyModel()
    print("Initial parameters:")
    for name, param in model.named_parameters():
        print(f"  {name}: {param.data}")

    get_loss(model, X, Y)
