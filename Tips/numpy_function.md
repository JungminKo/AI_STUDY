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
- `np.r_[]` : 배열을 왼쪽에서 오른쪽으로 붙임
  - ex. `df.iloc[:, np.r_[2, 3:5, 10]` 과 같이 dataframe의 iloc를 범위 지정해서 접근할 때 편함


- `np.where(condition)`: 조건(condition)에 맞는 인덱스 모두 반환
  - ***주의*** : index는 반환되는 tuple의 첫번째 요소이므로 [0]번째 값에 접근해야 함
  - ex. 배열 v의 값이 달라지는 부분 파악하기 : `np.where(v[:-1] != v[1:])[0]`
