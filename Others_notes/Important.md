### os 
- `os.listdir(path)` : returns a list containing the names of the entries in the directory given by path
- `os.path.join(path, *path)` : Join one or more path components intelligently
- `os.makedirs(path, exist_ok=True)`

### shutil


### argparse
```Python
parser = argparse.ArgumentParser(description='## Model')
parser.add_argument('--trained_model', default='weight.pth', type=str, help='pretrained model')
```
