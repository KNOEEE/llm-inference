import torch
from torch import nn

# This is a module
# It can have parameters, buffers, and submodules.
# A module can accept input tensors and produce output tensors.
class FeatureBlock(nn.Module):
    """A tiny submodule with a learnable parameter."""

    def __init__(self):
        super().__init__()
        # scale is a learnable parameter
        # It is updated during training.
        self.scale = nn.Parameter(torch.tensor(1.5))  # 0 dimension

    def forward(self, x):
        return x * self.scale


class MyModel(nn.Module):
    """A model with parameters, a buffer, and a submodule."""

    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(3, 2)
        # feature_bias is a buffer
        # It is not updated during training.
        self.register_buffer("feature_bias", torch.tensor([0.1, -0.1]))
        self.submodule = FeatureBlock()

    def forward(self, x):
        x = self.linear(x)
        x = self.submodule(x)
        return x + self.feature_bias


if __name__ == "__main__":
    print("== Model structure ==")
    model = MyModel()
    print(model)

    print("\n== Parameters ==")
    for name, param in model.named_parameters():
        print(name, param.shape)

    print("\n== Buffers ==")
    for name, buffer in model.named_buffers():
        print(name, buffer.shape, buffer)

    x = torch.randn(4, 3)
    y_before = model(x)
    print("\n== Before save/load output ==")
    print(y_before)

    checkpoint = model.state_dict()
    print("\n== state_dict keys ==")
    for k in checkpoint:
        print(k)

    model2 = MyModel()
    model2.load_state_dict(checkpoint)

    y_after = model2(x)
    print("\n== After save/load output ==")
    print(y_after)
    print("\n== Outputs identical? ==")
    print(torch.allclose(y_before, y_after))

    print("\n== Summary ==")
    print(
        "The state_dict stores learnable parameters and persistent buffers. "
        "Loading the same state back into a new model reproduces the same output."
    )
