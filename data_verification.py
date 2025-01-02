import torch


data = torch.load('data/FashionMNIST/data.pt')
targets = torch.load('data/FashionMNIST/targets.pt')


print(f"Data shape: {data.shape}")
print(f"Targets shape: {targets.shape}")