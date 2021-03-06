# matplotlib.pyplot 
### Setting
```Python
import matplotlib.pyplot as plt

plt.style.use("seaborn")
sns.set(font_scale=2, style='white') # style : 'whitegrid'

%matplotlib inline 
# the output of plotting commands is displayed inline within frontends like the Jupyter notebook, 
# directly below the code cell that produced it. 
# The resulting plots will then also be stored in the notebook document.
```
- use korean in graph
```Python
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname = 'C:\windows/fonts/malgun.ttf').get_name()

rc('font',family = font_name)
```

### Plots
- set title : `plt.title("title", y=1.05)`
- legend : `plt.legend(["legend1", "legend2"])`
- save : `plt.savefig('./fig.png')`

### Subplots
- **Create a figure and a set of subplots** : `f, ax = plt.subplots(1,2, figsize=(18,8))`
- **Adjust the subplot layout parameters** : `plt.subplots_adjust(wspace=0.2, hspace=0.4)`
```Python
### type1
f, ax = plt.subplots(1,2, figsize=(18,8)) 
df['col_name'].plot.bar(ax=ax[0]) 
ax[0].set_title('graph_1', y= 1.05) # y: position of title
ax[0].set_ylabel('ylabel')

ax[1].set_title('graph_2', y= 1.05)

### type2
plt.subplots(1, 2, 1)
plt.plot(x, y)
plt.subplots(1, 2, 2)
plt.plot(x, y)
```

### pandas.DataFrame.plot
- kind : `line`, `bar`, `barh`, `hist`, `box`, `kde`, `density`, `area`, `pie`, `scatter`, `hexbin` → [reference](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html#pandas.DataFrame.plot)
- Generate a pie plot
```Python
df['col_name'].plot.pie(autopct='%1.1f%%', shadow=True, explode = [0.1, 0.1, 0.1, 0.1] )  
     # textprops={'fontsize': 20} # adjusting fontsize
     # explode : len(x) array which specifies the fraction of the radius with which to offset each wedge 
```
- Generate a vertical bar plot
```Python
df['col_name'].plot.bar()
df['col_name'].value_counts().plot.bar()
```

# seaborn
```Python
import seaborn as sns
```
## Plotting with categorical variable 
- Draw a categorical plot onto a FacetGrid
     > **_factorplot_**, **_catplot_** 은 figure-level interface로 `plt.subplot`의 ax와 함께 사용될 수 없음
     > 
     > 만약에, ax로 쓰고 싶으면 `factorplot` 대신 각각 대응되는 axes-level function을 사용해야 함

     ```Python
     sns.factorplot(x='col_name1', y='col_name2', data=df, size=6) 
     # hue='col_name3', col='col_name3', 
     # kind : {“point”, “bar”, “strip”, “swarm”, “box”, “violin”, or “boxen”}, default="strip"
     ```
- drawing categorical plots ; **axes-level function**
     - **scatterplots** : `stripplot()`
     - **distribution plots** 
          - Draw a combination of boxplot and kernel density estimate
               ```Python
               sns.violinplot(x='col_name1', y='col_name2', hue='col_name3', data=df, scale='count', split=True) 
               # scale : {“area”, “count”, “width”}
               # can be used with numerical variables ex. age, height
               ```
     - **estimate plots**
          - Show **point estimates and confidence intervals** as rectangular bars
               ```Python
               sns.barplot(x='col_name1', y='col_name2', data=df)
               ```
          - Show the **counts of observations** in each categorical bin using bars
               ```Python
               sns.countplot(x='col_name', hue='col_name2', data=df) # hue variables will determine how the data are plotted.
               ```
          - Show **point estimates and confidence intervals** using scatter plot glyphs
               ```Python
               sns.pointplot(x='col_name1', y='col_name2', hue='col_name3', data=df)
               ```


## Plotting with numerical/quantitative/continuous variable 
- distribution plots 
     - figure-level interface : `sns.displot()` # kind : {"hist", "kde", "ecdf}
     - axes-level function
          - Plot univariate or bivariate histograms to show distributions of datasets
               ```Python
               sns.histplot(data=df['col_name']) 
               ```
          - Plot univariate or bivariate distributions using kernel density estimation
               ```Python
               sns.kdeplot(data=df, x = 'col_name')
               
               # categorical variable (ex.target variable) 값별로 kde 그려서 분포 비교하기
               sns.kdeplot(data=df[df['categorical']==value]['col_name'])
               ```
- `sns.violinplot()`
- Plot rectangular data as a color-encoded matrix.
```Python
sns.heatmap(data)

# create correlation matrix
sns.heatmap(df[['col_name1', 'col_name2', 'col_name3', 'col_name4', 'col_name5']].corr(), 
                annot=True, linewidths=0.1, vmax=1.0, fmt=".2f", cmap='coolwarm', annot_kws={'size':16})
```






