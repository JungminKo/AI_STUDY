### Pandas Dataframe
- randomly sample from DataFrame
```Python
# df : dataframe
df.sample(n=None, # default : n, Number of items from axis to return. Cannot be used with frac.
          frac=None, # default : None, Fraction of axis items to return. Cannot be used with n.
          replace=False, # default : False, Allow or disallow sampling of the same row more than once.
          weights=None, # default : None, Default ‘None’ results in equal probability weighting. 
          random_state=None, #default : None, seed for random number generator
          axis=None # {0 or 'index', 1 or 'columns', None}, default : None, Axis to sample.
         )
```

- convert string to numpy.array inside a DataFrame column
```Python
# df : dataframe  

import ast
df["array"] = df["array"].apply(lambda x: np.array(ast.literal_eval(x)))

```
