## Function

### 간단한 tensor 계산
```Python
import tensorflow as tf

tf.add(A, B)
tf.subtract(A, B)
tf.matmul(A, B, transpose_a=False, transpose_b=False) 
# 주의 : tf.matmul(A, B, transpose_b=True) =  tf.matmul(A, tf.transpose(B, ), transpose_b=True) 

tf.math.sqrt(A)
tf.shape(A) # dimensions of A
tf.cast(A, tf.float32) # tf.int32
tf.transpose(A, B) # 축 : 

tf.math.argmax(A, axis=None) # axis 설정 가능
tf.math.reduce_max(A, axis=None, keepdims=False) # axis 설정 가능 
  # reduction operation for the elementwise tf.math.maximum op
  # keepdims=True이면 length: 1, False이면 length: 0

tf.boolean_mask(A, mask, axis=None) # A:N-D Tensor , mask : K-D boolean tensor , K<=N
tf.gather(params, indices) # tensor params를 indices에 맞게 slicing
```

### tf 자주 사용하는 함수
```Python
# tf v1.14의 경우, from tensorflow.python.keras.layers에서 호출

from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.models import Model, load_model, Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout, Input, Reshape, Add, concatenate 
from tensorflow.keras.layers import Conv1D, Conv2D, Flatten, BatchNormalization
from tensorflow.keras.layers import AveragePooling2D, MaxPooling2D, ZeoPadding2Ds
from tensorflow.keras.layers import Masking, TimeDistributed, LSTM, GRU, Bidirectional
from tensorflow.keras.optimizers import Adam



model = Model(inputs = input, outputs = output)


X = Activation("relu")(X) # tensorflow.keras.layers.ReLU()(X)도 가능
X = Dropout(rate=dropout_rate)(X)


X = Conv2D(filters, kernel_size, strides=(1, 1), padding='valid', activation=None)(X) 
# padding = 'valid' or 'same'

X = BatchNormalization(axis=-1, momentum=0.99, epsilon=0.001)(X)

X = Add()([shortcut, X]


X = GRU(units=num_unit, return_sequences=True)(X) # return_sequences = True와 False의 차이

```



- `tensorflow.keras.layers.Activation('relu')`와 `tensorflow.keras.layers.ReLU` 의 차이?

- `tensorflow.keras.layers.GlobalAveragePooling2D()`과 `tensorflow.keras.layers.AveragePooling2D()`의 차이?
  - GlobalAveragePooling2D는 n개의 channel의 값을 평균하는 반면, 
  - AveragePooling2D는 channel별로 stride만큼 이동해가며 pool_size의 값에 대한 평균을 출력
