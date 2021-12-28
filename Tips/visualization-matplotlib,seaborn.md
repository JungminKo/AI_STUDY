# matplotlib.pyplot 
```Python
import matplotlib.pyplot as plt

plt.style.use("seaborn")
sns.set(font_scale=1.5, style='white') # style : 'whitegrid'

%matplotlib inline 
# the output of plotting commands is displayed inline within frontends like the Jupyter notebook, 
# directly below the code cell that produced it. 
# The resulting plots will then also be stored in the notebook document.
```
- Basic
```Python
f, ax = plt.subplots(1,2, figsize=(18,8))
ax[0].set_title('graph_1', y= 1.02) # y: position of title
df['col_name'].plot.bar(ax=ax[0]) #  
ax[0].set_ylabel('ylabel')

ax[1].se_title('graph_2', y= 1.02)
plt.subplots_adjust(wspace=0.2, hspace=0.5)
```

- Generate a pie plot
```Python
df['col_name'].plot.pie(autopct='%1.1f%%', shadow=True, explode = [0.1, 0.1, 0.1, 0.1] )  
     # explode : len(x) array which specifies the fraction of the radius with which to offset each wedge 
```
- Generate a vertical bar plot
```Python
df['col_name'].plot.bar()
```

# seaborn
```Python
import seaborn as sns
```

- Show the **counts of observations** in each categorical bin using bars
```Python
sns.countplot(x='col_name', hue='col_name2', data=df) # hue variables will determine how the data are plotted.
```

- Show point estimates and confidence intervals as rectangular bars
```Python
sns.barplot(x='col_name1', y='col_name2', data=df)
```

- Plot univariate or bivariate histograms to show distributions of datasets
```Python
sns.histplot(data=df['col_name']) 
```

- Plot rectangular data as a color-encoded matrix.
```Python
sns.heatmap(data)

# create correlation matrix
sns.heatmap(df[['col_name1', 'col_name2', 'col_name3', 'col_name4', 'col_name5']].corr(), 
                annot=True, fmt=".2f", cmap='coolwarm')
```


- Draw a categorical plot onto a FacetGrid
```Python
sns.factorplot(x='col_name1', y='col_name2', data=df, size=6) 
# hue='col_name3', col='col_name3', 
# kind : {“point”, “bar”, “strip”, “swarm”, “box”, “violin”, or “boxen”}, default="strip"
```

- Plot univariate or bivariate distributions using kernel density estimation
```Python
sns.kdeplot(data=df, x = 'col_name')
```

- Draw a combination of boxplot and kernel density estimate
```Python
sns.violinplot(x='col_name1', y='col_name2', hue='col_name3', data=df, scale='count', split=True) 
# scale : {“area”, “count”, “width”}
```
