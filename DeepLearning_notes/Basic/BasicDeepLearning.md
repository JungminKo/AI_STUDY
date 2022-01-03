
### Logistic Loss


### Forward


### Backward


### Gradient Descent

## 


## Activation Function
- Sigmoid 
  - forward 
    <div align="begin"><img src="https://latex.codecogs.com/svg.image?\sigma(x)&space;=&space;\frac{1}{1&plus;e^{-x}}" title="\sigma(x) = \frac{1}{1+e{-x}}" />
    
    ```python
    def sigmoid(x):
      s = 1/(1+np.exp(-x))
      return s
    ```
  - backward
    <div align="begin"><img src="https://latex.codecogs.com/svg.image?\sigma^\prime(x)&space;=&space;\sigma(x)(1-\sigma(x))" title="\sigma^\prime(x) = \sigma(x)(1-\sigma(x))" />
    
    ```python
    def sigmoid_derivative(x):
      s = sigmoid(x)
      ds = s*(1-s)
      return ds
    ```
- softmax
  - forward
    <div align="begin"><img src="https://latex.codecogs.com/svg.image?softmax(x)&space;=&space;\frac{e^{x_i}}{\sum_{j}e^{x_j}&space;}" title="softmax(x) = \frac{e^{x_i}}{\sum_{j}e^{x_j} }" />
    
    ```python
    def softmax(x): # x.shape = (m,n) ; m : number of training examples, n: number of features
      x_exp = np.exp(x)
      x_exp_sum = np.sum(x_exp, axis=1, keepdims=True) 
      s = x_exp/x_sum
      return s
    ```
  - backward
    
    ```python
    def softmax_derivative(x):

      return ds
    ```
    
 ## Loss Functions
 - L1 loss function
  
   ```python
    def L1_loss(y_pred, y):
      loss = np.sum(abs(y_pred-y))
      return loss
    ```
    
 - L2 loss function
 
    ```python
    def L2_loss(y_pred, y):
      loss = np.sum(np.dot(y_pred-y, y_pred-y))
      return loss
    ```
      
      
 - cross-entropy cost
    
    ```python
    def cross_entropy_cost(y_pred, y): # y_pred : probability vector to label predictions , y : true label vector
      m = y.shape[1]
      cost = -1/m*np.sum((np.dot(y, np.log(y_pred).T) + np.dot(1-y, np.log((1-y_pred)).T)))
      cost = np.squeeze(cost)
      
      return cost
    ```

