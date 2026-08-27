import numpy as np
import torch 
from torch import nn
import matplotlib.pyplot as plt
m= 0.1234
c= 0.6789
X= np.arange(0.2,0.04)
y= m*X+c

split= int(0.8*len(X))
X_train, y_train = X[:split], y[:split]
X_test, y_test= X[split:], y[split:]

X_train_tensors= torch.from_numpy(X_train)
y_train_tensors= torch.from_numpy(y_train)
X_test_tensors= torch.from_numpy(X_test)
y_test_tensors= torch.from_numpy(y_test)
print(f"Shape of X_train is{X_train.shape} and type is {type(X_train)}")
print(f"Shape of X_train_tensors is{X_train_tensors.shape} and type is {type(X_train_tensors)}")

def plot_data(
        X_train= X_train , y_train = y_train, X_test=X_test, y_test=y_test,predictions= None):
    plt.scatter(X_train,y_train, c='r', label="Training Data")
    plt.scatter(X_test,y_test, c='b', label="Testing data")
    if predictions is not None:
        plt.scatter(X_test,predictions, c='g', label='Predicted Data')
    plt.show()
plot_data()




# class MyFirstNeuralNetwork(nn.Module):
#     def __init__(self):
#         super().__init__()
#         self.weights= nn.Parameter(torch.randn(size=1, requires_grad=True, dtype= nn.float))
#         self.bias = nn.Parameter(torch.randn(size=1, requires_grad=True, dtype= nn.float))

#     def forward(self, x:torch.Tensor) -> torch.Tensor:
#         return self.weights * x + self.bias

# with nn.inference_mode():
#     y_preds= model(X_test_tensors)

# plot_data(predictions= y_preds)

# loss_fn = nn.MSELoss()
# optimizer = nn.optim.SGD(
#     params= model.parameters(),
#     lr= 0.1

# )
# epoch= 500
# train_loss_list= []
# test_loss_list= []
# model.to(device)
# X_train_tensors, y_train_tensors = X_train_tensors.to(device), y_train_tensors.to(device)
# X_test_tensors, y_test_tensors = X_test_tensors.to(device), y_test_tensors.to(device)
# for epoch in range(epochs):
#     model.train()
#     trin_preds= model(X_train_tensors, train_preds)
#     optimizer.zero_grad()
#     train_loss.backward()
#     optimizer.step()
#     model.eval()
#     with torch.inference_model():
#         test_preds= model(X_test_tensors)
#         test_loss= loss_fn(y_test_tensors, )
#     train_loss_list.append(train_loss.detach().cpu())
#     test_loss_list.append(test_loss.detach().cpu())
#     if(epoch+1)%50 ==0:
#         print(f'Epoch {epoch}|Train Loss{train_loss:.4f}|Test loss {test_loss:.4f}')


# #loss curve
# model.state_dict()

                    
