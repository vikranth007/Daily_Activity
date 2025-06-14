import torch 
from torch import nn
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

device = "cuda" if torch.cuda.is_available() else "cpu"


x, y = make_blobs(n_samples=1000,n_features=2, centers=4, random_state=42)

x = torch.from_numpy(x).type(torch.float)
y = torch.from_numpy(y).type(torch.LongTensor)

# print(x), print(y)

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)



class Blobmodel(nn.Module):
    def __init__(self,input_features, output_features, hidden_units):
        super().__init__()
        self.linear = nn.Sequential(
            nn.Linear(in_features=input_features, out_features=hidden_units),
            nn.ReLU(),
            nn.Linear(in_features=hidden_units, out_features=hidden_units),
            nn.ReLU(),
            nn.Linear(in_features=hidden_units, out_features=output_features))
    
    def forward(self, x):
        return self.linear(x)


model = Blobmodel(input_features=2,output_features=4,hidden_units=8).to(device)



# Create a loss function and optimizer

loss_fn = nn.CrossEntropyLoss()

# optimizer

optimizer = torch.optim.SGD(model.parameters(), lr=0.1)

# Calculate accuracy (a classification metric)
def accuracy_fn(y_true, y_pred):
    correct = torch.eq(y_true, y_pred).sum().item() # torch.eq() calculates where two tensors are equal
    acc = (correct / len(y_pred)) * 100 
    return acc




# Train loop

torch.manual_seed(42)
torch.cuda.manual_seed(42)

epochs = 100

# put data to target device

X_train, y_train = X_train.to(device), y_train.to(device)
X_test, y_test = X_test.to(device), y_test.to(device)


for epoch in range(epochs):

    model.train()

    y_logits = model(X_train)
    y_pred = torch.softmax(y_logits, dim=1).argmax(dim=1)

    loss = loss_fn(y_logits, y_train)
    acc = accuracy_fn(y_true=y_train, y_pred=y_pred)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    # Testing loop

    model.eval()
    with torch.inference_mode():
        test_logits = model(X_test)
        test_pred = torch.softmax(test_logits, dim=1).argmax(dim=1)

        test_loss = loss_fn(test_logits, y_test)
        test_acc = accuracy_fn(y_true=y_test, y_pred=test_pred)


    if epoch % 10 == 0:
        print(f"epoch: {epoch} | train loss : {loss} | Acc : {acc} Test loss : {test_loss} | test Acc : {test_acc}")
        













