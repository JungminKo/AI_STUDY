

### LabelPropagation
```Python
from sklearn.semi_supervised import LabelPropagation 

label_prop_model = LabelPropagation(kernel='knn', # {'knn', 'rbf'} default='rbf'
                              #gamma=70, # default=20, Parameter for rbf kernel.
                              n_neighbors=20, # default=7, Parameter for knn kernel which is a strictly positive integer.
                              max_iter=1000, # default=30, Maximum number of iterations allowed.
                              tol=0.001, # default=1e-3, Convergence tolerance: threshold to consider the system at steady state.
                              n_jobs=-1, # default=None, The number of parallel jobs to run. -1 means using all processors. 
                             )
```
