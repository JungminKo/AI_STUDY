

### LabelPropagation
```Python
from sklearn.semi_supervised import LabelPropagation 

label_prop_model = LabelPropagation(kernel='knn', # {'knn', 'rbf'} default='rbf'
                              #gamma=20, # default=20, Parameter for rbf kernel.
                              n_neighbors=20, # default=7, Parameter for knn kernel which is a strictly positive integer.
                              max_iter=1000, # default=30, Maximum number of iterations allowed.
                              tol=0.001, # default=1e-3, Convergence tolerance: threshold to consider the system at steady state.
                              n_jobs=-1, # default=None, The number of parallel jobs to run. -1 means using all processors. 
                             )
                             
label_prop_model.fit(X, Y)
```

### LabelSpreading
```Python
from sklearn.semi_supervised import LabelSpreading

label_spread_model = LabelSpreading(kernel='rbf',#{'knn', 'rbf'} default='rbf'
                         gamma=20, #default=20, Parameter for rbf kernel
                         n_neighbors=7, #default=7, Parameter for knn kernel which is a strictly positive integer
                         alpha=0.5, #Clamping factor. 
                                    #A value in (0, 1) that specifies the relative amount 
                                    #that an instance should adopt the information from its neighbors as opposed to its initial label.
                                    #alpha=0 means keeping the initial label information; 
                                    #alpha=1 means replacing all initial information.
                         max_iter=100,#default=30, Maximum number of iterations allowed
                         tol=0.001,#default=1e-3, Convergence tolerance; threshold to consider the system at steady state.
                         n_jobs=-1, # default=None, The number of parallel jobs to run. -1 means using all processors.
                         )
                         
label_spread_model.fit(X, Y)                         
```
