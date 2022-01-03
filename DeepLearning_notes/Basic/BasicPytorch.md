
# 
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

### reshape
```Python
torch.view(shape) # View tensor shares the same underlying data with its base tensor 
```

- `torch.roll()`  
  - Roll the tensor along the given dimension(s). 
  - Elements that are shifted beyond the last position are re-introduced at the first position. 
