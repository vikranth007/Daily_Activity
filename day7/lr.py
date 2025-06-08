import os

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"


import torch
from torch import nn
import matplotlib.pyplot as plt

device = "cuda" if torch.cuda.is_available() else "cpu"

# print(device)

weight = 0.7
bias = 0.3

X = torch.arange(0, 1, 0.02).unsqueeze(dim=1)
y = weight * X + bias

train_split = int(0.8 * len(X))
X_train , y_train = X[:train_split:], y[:train_split]
X_test, y_test = X[train_split:], y[train_split:]


# print(len(X_train), len(y_train), len(X_test), len(y_test))

def plot_predictions(train_data = X_train, train_labels=y_train, test_data=X_test, test_labels=y_test,predictions=None):
    plt.figure(figsize=(10, 7))
    plt.scatter(train_data, train_labels, c='b', s=4, label="Training_data")

    plt.scatter(test_data, test_labels, c='g', s=4, label="Testing_data")

    if predictions is not None:
        plt.scatter(test_data, predictions, c='r', s=4, label='predictions')
    plt.legend()
    plt.show()

# plot_predictions(X_train, y_train, X_test, y_test)





class LinearRegression(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_layer = nn.Linear(in_features=1, out_features=1)

    def forward(self, X):
        return self.linear_layer(X)


torch.manual_seed(42)
model = LinearRegression()


model = model.to(device)



loss_fn = nn.L1Loss()

optimizer  = torch.optim.SGD(params = model.parameters(), lr=0.01)


torch.manual_seed(42)

epochs = 1000

X_train = X_train.to(device)
y_train = y_train.to(device)
X_test = X_test.to(device)
y_test = y_test.to(device)


for epoch in range(epochs):

    model.train()

    y_pred = model(X_train)

    loss = loss_fn(y_pred, y_train)

    optimizer.zero_grad()

    loss.backward()

    optimizer.step()

    # testing 
    model.eval()
    with torch.no_grad():
        y_pred = model(X_test)
        test_loss = loss_fn(y_pred, y_test)

    if epoch % 10 == 0:
        print(f"epoch : {epoch} | train_loss : {loss} | test_loss : {test_loss}")
    


model.eval()
with torch.inference_mode():
    y_pred = model(X_test)
print(y_pred)


plot_predictions(predictions=y_pred.cpu())