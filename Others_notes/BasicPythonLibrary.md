### os 
- `os.listdir(path)` : returns a list containing the names of the entries in the directory given by path
- `os.path.join(path, *path)` : Join one or more path components intelligently
- `os.makedirs(path, exist_ok=True)`

### shutil


### argparse
```Python
parser = argparse.ArgumentParser(description='## Model')
parser.add_argument('--trained_model', default='weight.pth', type=str, help='pretrained model')


## Parsing boolean values with argparse
parser.add_argument("--Boolean", default='True', type=str2bool, help="Boolean")

def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ("yes", "y", "true", "t", "1"):
        return True
    elif v.lower() in ("no", "false", "f", "n", "0"):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.') 
        
```

### random
- `random.randint(0, 2)` : return an integer number / both included
- `random.uniform(0, 1)` : return a random floating number / both included
- `random.choice(list)` : return a random element from a list
- `random.choices(list, weights=[1,2,3], k=1)` : return a list
