# numpy 주요 함수

### 행렬곱셈관련 함수
- `np.dot(a, b)` : a, b의 행렬곱셈
- `a@b` : a, b의 행렬곱셈
- `a*b` : a, b의 inner product
- `np.multiply(a, b)` : a, b 의 elemenwise product


### to expand the dimensions
1. np.newaxis
```Python
x = np.arange(3) # array([0, 1, 2]) # shape : (3,)
x[:, np.newaxis] # array([[0], [1], [2]])  # shape : (3,1)
x[np.newaxis, :] # array([[0, 1, 2]])  # shape : (1,3)
```



### 기타
- `np.int0()` : numpy 타입을 int64로 변환
