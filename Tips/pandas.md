### Pandas Dataframe
- change the name of column
```Python
# column 이름 바꾸기
df.rename(columns={0: "x", 1: "y", 2: "z"}, inplace=True)

# cf. index 이름 바꾸기
df.rename(index={0: "x", 1: "y", 2: "z"})
df.rename({1: 2, 2: 4}, axis='index')
```
- check null data 
```Python
# column 별로 null data 개수 세기
df.isnull().sum(axis=0)

# null data 시각화하기
import missingno as msno
msno.matrix(df=df, figsize=(8,8), color(0.8, 0.5, 0.2) # null data의 위치는 흰색으로 시각화
msno.bar(df=df, figsize=(8, 8), color=(0.8, 0.5, 0.2)) # 전체 개수 중 몇 %가 null data인지를 시각화
```

- save csv with korean  
```Python
df.to_csv("./data.csv", index=False, encoding='utf-8-sig')
```

- randomly sample from DataFrame
```Python
df.sample(n=None, # default : n, Number of items from axis to return. Cannot be used with frac.
          frac=None, # default : None, Fraction of axis items to return. Cannot be used with n.
          replace=False, # default : False, Allow or disallow sampling of the same row more than once.
          weights=None, # default : None, Default ‘None’ results in equal probability weighting. 
          random_state=None, #default : None, seed for random number generator
          axis=None # {0 or 'index', 1 or 'columns', None}, default : None, Axis to sample.
         )
```

- convert string to numpy.array inside a DataFrame column
```Python
import ast
df["array"] = df["array"].apply(lambda x: np.array(ast.literal_eval(x)))

```

- compute a simpe cross tabulation of two(or more) factors
```Python
pd.crosstab(df['col_name1'], df['col_name2'], margins=True) 
```
