"""Minimal autograd + training loop example for Week 04.

- Fits a tiny synthetic dataset with a simple linear model.
- Prints loss per epoch to show decrease.
- Demonstrates `torch.no_grad()` and `torch.inference_mode()` for inference.
"""
import time
import torch
from torch import nn

# Reproducible behavior
torch.manual_seed(42)

# Tiny dataset: y = 2*x + 3 with small noise
X = torch.linspace(-1, 1, steps=20).unsqueeze(1)  # (20,1)
Y = 2.0 * X + 3.0 + 0.1 * torch.randn_like(X)

class TinyModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(1, 1)

    def forward(self, x):
        return self.linear(x)


def train(model, x, y, epochs=200, lr=0.1):
    opt = torch.optim.SGD(model.parameters(), lr=lr)
    loss_fn = nn.MSELoss()
    for epoch in range(1, epochs + 1):
        pred = model(x)
        loss = loss_fn(pred, y)
        opt.zero_grad()
        loss.backward()
        opt.step()
        if epoch % (epochs // 5) == 0 or epoch == 1:
            print(f"epoch {epoch:3d} loss={loss.item():.6f}")
    return loss.item()


def inference(model, x):
    # inference_mode is fastest and prevents autograd bookkeeping when available
    if hasattr(torch, "inference_mode"):
        with torch.inference_mode():
            return model(x)
    else:
        with torch.no_grad():
            return model(x)


if __name__ == "__main__":
    model = TinyModel()
    print("Initial parameters:")
    for n, p in model.named_parameters():
        print(n, p.data.numpy())

    print("\nStart training")
    start = time.time()
    final_loss = train(model, X, Y, epochs=500, lr=0.1)
    dt = time.time() - start
    print(f"Training finished in {dt:.3f}s, final loss={final_loss:.6f}\n")

    print("Trained parameters:")
    for n, p in model.named_parameters():
        print(n, p.data.numpy())

    # Show inference with and without grad
    x_test = torch.tensor([[4.0], [10.0]])

    print("\nInference with autograd (requires_grad=False by default for outputs):")
    y1 = model(x_test)
    print(y1)

    print("\nInference with no_grad / inference_mode:")
    y2 = inference(model, x_test)
    print(y2)

    # Confirm that outputs are the same
    print("\nOutputs equal:", torch.allclose(y1, y2))

    # Demonstrate that gradients are not tracked in inference context
    with torch.no_grad():
        y3 = model(x_test)
    print("\nIn no_grad requires_grad of output:", y3.requires_grad)

    try:
        # if inference_mode exists, outputs also don't require grad
        if hasattr(torch, "inference_mode"):
            with torch.inference_mode():
                y4 = model(x_test)
            print("inference_mode requires_grad:", y4.requires_grad)
    except Exception:
        pass

    print("\nExample complete.")
