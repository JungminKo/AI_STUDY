# numpy 주요 함수
### mathematical functions
- `np.clip(a, a_min, a_max)` : clip (limit) the values in an array.
- `np.diff(a, n=1, axis=-1)` : calculate the n-th discrete difference along the given axis
- `np.ceil(a)`, `np.floor(a)`
- `np.median(a)`

### 행렬곱셈관련 함수
- `np.dot(a, b)` : a, b의 행렬곱셈
- `a@b` : a, b의 행렬곱셈
- `a*b` : a, b의 inner product
- `np.multiply(a, b)` : a, b 의 elemenwise product



### change array shape
1. np.newaxis / np.expand_dims
```Python
x = np.arange(3) # array([0, 1, 2]) # shape : (3,)

# np.newaxis
x[:, np.newaxis] # array([[0], [1], [2]])  # shape : (3,1)
x[np.newaxis, :] # array([[0, 1, 2]])  # shape : (1,3)

# np.expand_dims
np.expand_dims(x, axis=0) # array([[0, 1, 2]])  # shape : (1,3)
np.expand_dims(x, axis=1) # array([[0], [1], [2]])  # shape : (3,1)

# np.tile
# construct an array by repeating A the number of times given by reps
np.tile(a, 2) # array([0, 1, 2]) -> array([0, 1, 2, 0, 1, 2])
```

2. np.squeeze
```Python
# Remove axes of length one from x
x = np.arange(12).reshape(1,3,2,2)
x = np.squeeze(x) # shape : (1,3,2,2) -> (3,2,2)
```

3. 축바꾸기
```Python
x = np.arange(24).reshape(2,3,4)
np.transpose(x) # x.T # shape : (4,3,2)
np.swapaxes(x, 0, 1) # shape : (3,2,4)
np.swapaxes(x, 0, 2) # shape : (4,3,2)
np.swapaxes(x, 1, 2) # shape : (2,4,3)

##Image
image = image.transpose(2,0,1) # (224, 224, 3) -> (3, 224, 224)
```

4. return flattened array
- `np.ravel(a)`/ `a.ravel()` : Return a contiguous flattened array
- `a.reshape(-1)`
- `np.flatten(a)` : Return **a copy** of the array collapsed into one dimension


### np.random
```Python
# Create an array of the given shape and populate it with random samples from a uniform distribution over [0, 1).
np.random.rand(row, col)

# Generates a random sample from a given 1-D array
np.random.choie(a, size=None, p=None) # a : 1-D array-like or int - int : np.arange(a)

# Return random integers from low (inclusive) to high (exclusive)
np.random.randint(low, high=None, size=None) # if high=None, 0부터 low-1까지의 숫자중 sampling
``` 

### 기타
- **`array.tolist()`** : numpy 타입은 list로 변환
- **`np.int0()`** : numpy 타입을 int64로 변환
- **`np.r_[]`** : 배열을 왼쪽에서 오른쪽으로 붙임
  - ex. `df.iloc[:, np.r_[2, 3:5, 10]` 과 같이 dataframe의 iloc를 범위 지정해서 접근할 때 편함

- **`array.ndim`** : return The number of dimensions 
- `np.argwhere(condition)` : 조건(condition)에 맞는 인덱스 모두 반환 
  - ex. 배열 v의 값이 달라지는 부분 파악하기 : `np.argwhere(v[:-1] != v[1:])`  # shape: (n, 1)
  
- `np.where(condition, x, y)`: 조건(condition)에 맞는 인덱스 모두 반환
  - `np.argwhere`처럼 condition만 주어질 수도 있음
    - 그러면 `np.asarray(condition).nonzero()` 로 사용되는 것이 좋음
    - ***주의*** : index는 반환되는 tuple의 첫번째 요소이므로 [0]번째 값에 접근해야 함
    - ex. 배열 v의 값이 달라지는 부분 파악하기 : `np.where(v[:-1] != v[1:])[0]` # shape : (n, )
  - `np.where(a<4, a, 10*a)` : a<4이면 a, 아니면 10 * a로 값을 대체하여 array 반환

- `np.cumsum(a)` : the cumulative sum of the elements along a given axis

- `np.roll(a, shift)` : Roll array elements along a given axis, positive : back-> front, negative : front->back
