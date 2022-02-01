
### Check GPU
```Python
import torch

torch.cuda.is_available() # >>> True
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print('Using device:', device) # >>> 'cuda'
```

### 

```Python
import torch
import torch.nn as nn

 # A sequential container. Modules will be added to it in the order they are passed in the constructor
nn.Sequential()
nn.Sequential(
          nn.Conv2d(1,20,5),
          nn.ReLU(),
          nn.Conv2d(20,64,5),
          nn.ReLU()
        )
 
# Holds submodules in a list.
nn.ModuleList() 
nn.ModuleList([nn.Linear(10, 10) for i in range(10)])
```
### Basic operation
- `torch.add(a, b)`
- `torch.mul(a, b)`
- `torch.dot(a, b)` : matrix multiplication
- `torch.min(a)`, `torch.max(a)` : returns min/max and min_indices/max_indices

### reshape
- `tensor.view(shape)` 
  - View tensor shares the same underlying data with its base tensor
- `torch.squeeze(input, dim=None)`
  - Returns a tensor with all the dimensions of input of size 1 removed
- `torch.unsqueeze(input, dim)`
  - Returns a new tensor with a dimension of size one inserted at the specified position
  
- `torch.roll()`  
  - Roll the tensor along the given dimension(s). 
  - Elements that are shifted beyond the last position are re-introduced at the first position. 
  
### Dataset, DataLoader
- `torch.utils.data.Dataset` : sample과 label을 저장
- `torch.utils.data.DataLoader` : sample에 쉽게 접근할 수 있도록 iterable 하게 만듦

  - 사용자 정의 Dataset 클래스 : ` __init__`, `__len__`,  `__getitem__`
   ```Python
   import os
   import pandas as pd
   from torchvision.io import read_image

   class CustomImageDataset(Dataset):
       def __init__(self, annotations_file, img_dir, transform=None, target_transform=None):
           self.img_labels = pd.read_csv(annotations_file, names=['file_name', 'label'])
           self.img_dir = img_dir

       def __len__(self):
           return len(self.img_labels)

       def __getitem__(self, idx):
           img_path = os.path.join(self.img_dir, self.img_labels.iloc[idx, 0])
           image = read_image(img_path)
           label = self.img_labels.iloc[idx, 1]
           
           return image, label
   ```
   
### Loss
```Python
torch.nn.BCELoss() # BCELoss : Binary Cross Entropy Loss

```

### Optimizer
```Python
torch.optim.SGD(model.parameters(), lr=0.01, momentum=0.9)
```

### Extra
- `torch.from_numpy(ndarray)` : Creates a Tensor from a numpy.ndarray
- `torch.randn(shape)`: Returns a tensor filled with random numbers from a normal distribution with mean 0 and variance 1 
- `torch.arange(start=0, end)`
