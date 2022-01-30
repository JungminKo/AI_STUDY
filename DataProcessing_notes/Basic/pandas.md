# Series
**- to map values of Series according to input correspondence**
 ```Python
 s.map({'cat': 'kitten', 'dog': 'puppy'})
 df['sex'].map({"male":0, "female":1})
 s.map(lambda i: np.log(i) if i>0 else 0)
 ```
**- to extract capture groups in the regex pat as columns in a DataFrame**
 ```Python
 s.str.extract(r'([ab])(\d)') 
 ```
**- to Replace each occurrence of pattern/regex in the Series/Index.**
 ```Python
 s.str.replace('[^가-힣A-z ]', '')
 ```
**- to fill NA/NaN values using the specified method** : `s.fillna(5, inplace=False)`

**- to return a Series containing counts of unique values** : `s.value_counts()`


#  Dataframe
## Basic info about data
**- to print a concise summary of a DataFrame** : `df.info()`

**- to generate descriptive statistics** : `df.describe()`
  - `df.describe().T`를 하면 더 많은 column에 대해서 볼 수 있으므로 편함
  - `df.describe(include=np.object).T`를 하면 모든 object columns에 대해 describe를 볼 수 있음
    - `unique` 로 categorical variable인지 여부 확인 가능

**- to check null data** : `df.isnull()`
```Python
# column 별로 null data 개수 세기
df.isnull().sum()
# column 별로 null data가 한개라도 있는지 확인
df.isnull().any() # 결과 : True/False

# null data가 있는 columns만 보기
is_missing = df.isnull().sum()>0
df.isnull().sum()[is_missing]

# null data 시각화하기
import missingno as msno
msno.matrix(df=df, figsize=(8,8), color(0.8, 0.5, 0.2) # null data의 위치는 흰색으로 시각화
msno.bar(df=df, figsize=(8, 8), color=(0.8, 0.5, 0.2)) # 전체 개수 중 몇 %가 null data인지를 시각화
```


## change column/index 
**- to change the name of column**
 ```Python
 # column 이름 바꾸기
 df.rename(columns={0: "x", 1: "y", 2: "z"}, inplace=True)

 # cf. index 이름 바꾸기
 df.rename(index={0: "x", 1: "y", 2: "z"})
 df.rename({1: 2, 2: 4}, axis='index')
 ```

**- to drop specified labels from rows or columns**
```Python
df.drop('index', axis=0, inplace=False) # drop row 
df.drop('col_name', axis=1) # drop column # can put a list to drop columns
```

**- to select a subset of the DataFrame’s columns based on the column dtypes**
```Python
df.select_dtypes(include='object') # parameters : include, exclude 
df.select_dtypes(include='number')
df.select_dtypes(include='datetime') # 끝에 .columns을 붙이면 해당하는 column을 뽑아낼 수 있음 
```


**- to save csv with korean**  
```Python
df.to_csv("./data.csv", index=False, encoding='utf-8-sig')
```

**- to group DataFrame using a mapper or by a Series of columns** : `groupby`
```Python
df.groupby('col1', as_index=True).count() # .sum(), .mean(), .max(), .min()
df[['col1','col2']].groupby('col1', as_index=True).count()
```

**- to randomly sample from DataFrame**
```Python
df.sample(n=None, # default : n, Number of items from axis to return. Cannot be used with frac.
          frac=None, # default : None, Fraction of axis items to return. Cannot be used with n.
          replace=False, # default : False, Allow or disallow sampling of the same row more than once.
          weights=None, # default : None, Default ‘None’ results in equal probability weighting. 
          random_state=None, #default : None, seed for random number generator
          axis=None # {0 or 'index', 1 or 'columns', None}, default : None, Axis to sample.
         )
```

**- to convert string to numpy.array inside a DataFrame column**
```Python
import ast
df["array"] = df["array"].apply(lambda x: np.array(ast.literal_eval(x)))
```

**- to compute a simpe cross tabulation of two(or more) factors**
```Python
pd.crosstab(df['col_name1'], df['col_name2'], margins=True) #.style.background_gradient(cmap='summer_r')
```

**- to apply a function along an axis of the DataFrame**
  
  - ex. to change continuous variables to categorical variables
```Python
def category_age(x):
    if x<10:
          return 0
    elif x<20:
          return 1
    else:
          reuturn 2
df['col_names_cate'] = df['col_names'].apply(category_age
```

