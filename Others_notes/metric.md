
- F beta score

```Python
def fscore(precision, recall, beta=1, eps=1e-07):
    bb = beta**2
    return (1 + bb) * (precision * recall)/(bb * precision + recall + eps)
```
