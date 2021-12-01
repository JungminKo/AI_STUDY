### Pandas Dataframe


- convert string to numpy.array in side a DataFrame column
```Python
# df : dataframe  

import ast
df["array"] = df["array"].apply(lambda x: np.array(ast.literal_eval(x)))

```
