import torch
from torch import nn



device = "cuda" if torch.cuda.is_available() else "cpu"
print(device)