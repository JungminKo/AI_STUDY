

- fit_transform / transform
  - fit_transform : fit to data, then transform it / use for x_train
  - transform : trnasform x / use for x_test


- `sklearn.preprocessing.OrdinalEncoder` :  to encode categorical features as an integer array
```Python
from sklearn.preprocessing import OrdinalEncoder

oe = OrdinalEncoder(handle_unknown='use_encoded_value', # handle_unknown{‘error’, ‘use_encoded_value’}, default=’error’
                    unknown_value = -1) # When handle_unknown is set to ‘use_encoded_value’, this parameter is required
                    
X_train = oe.fit_transform(X_train)
X_test = oe.transform(X_test)
```

- `sklearn.preprocessing.LabelEncoder` : to encode target labels with value between 0 and n_classes-1
```Python
from sklearn.preprocessing import OrdinalEncoder

le = LabelEncoder()

y_train = le.fit_transform(y_train)
y_test = le.transform(y_test)
```
