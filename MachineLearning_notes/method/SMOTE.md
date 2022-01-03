# SMOTE
- 출처 : https://towardsdatascience.com/smote-fdce2f605729
- solution for imbalanced data
- 기존 방법론인 `undersampling`, `oversampling`의 한계 극복
  - `undersampling` : lose a lot of valuable data
  - `oversampling` : create many duplicate data point
  - `data augmentation` : duplicating and perturbing ocrruences of the less frequent class

- **SMOTE** : create **synthetic** data points
  - `oversampling`은 동일한 data point를 만들었지만, `SMOTE`는 조금씩 다른 data point을 만듦. 일종의 `data augmentation` 방법
  - 과정 : **slightly** moving the data point in the direction of its neighbor
     1. draw a random sample from the minority class
     2. identify the k nearest neighbors
     3. take one of those neighbors and identify the vector between the current data point and the selected neighbor
     4. multiply the vector by a random number between 0 and 1
     5. to obtain the synthetic data point, add this to the current data point
     
     
  - 성능 : increase in recall, at the cost of lower precision
    - imbalanced data는 accuracy 보다는 다른 것들을 척도로 봐야 함
    - SMOTE의 경우 false negative를 줄이고, false positive를 높이는 방향으로 학습
      - ex. 코로나바이러스가 조금이라도 의심되면 걸렸다고 보는게 더 적절 (안그러면 걸린채로 돌아다녀서 코로나가 더 퍼지게 됨)


  - package : `from imblearn.over_sampling import SMOTE` 사용
  
    ```python
    from imblearn.over_sampling import SMOTE
    X_resampled, y_resampled = SMOTE().fit_resample(train_X, train_y)
    ```
