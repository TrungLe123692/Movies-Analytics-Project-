# -*- coding: utf-8 -*-
"""Portfolio Project

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VyjFArKNhrfflNGA76zK8HA3Itgf6k0X
"""

# Commented out IPython magic to ensure Python compatibility.
# Import libraries
import pandas as pd
import numpy as np
import seaborn as sns


import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib
plt.style.use('ggplot')
from matplotlib.pyplot import figure

# %matplotlib inline
matplotlib.rcParams['figure.figsize']=(12,8)


pd.options.mode.chained_assignment=None

# Load the data
df =pd.read_csv("movies.csv")

# Overview of the data
df

# Remove missing values in the data

for col in df.columns:
  pct_missing=np.mean(df[col].isnull())
  print("{} - {}%".format(col,round(pct_missing*100)))

print(df.dtypes)

# Remove the outliers
df.boxplot(column=['gross'])



df.drop_duplicates()

# Reorder the data

df.sort_values(by=['gross'],inplace=False, ascending=False)

sns.regplot (x="gross",y="budget",data =df)

sns.regplot(x="score",y="gross",data =df)

# Correlation matrix between numeric values
numeric_df = df.select_dtypes(include=['int64', 'float64'])
correlation = numeric_df.corr(method='pearson')

numeric_df = df.select_dtypes(include=['int64', 'float64'])
correlation = numeric_df.corr(method='kendall')

numeric_df = df.select_dtypes(include=['int64', 'float64'])
correlation = numeric_df.corr(method='spearman')

correlation_matrix = numeric_df.corr()

sns.heatmap(correlation_matrix, annot = True)

plt.title("Correlation matrix for Numeric Features")

plt.xlabel("Movie features")

plt.ylabel("Movie features")

plt.show()

# Using factorize - this assigns a random numeric value for each unique categorical value

df.apply(lambda x: x.factorize()[0]).corr(method='pearson')

correlation_matrix = df.apply(lambda x: x.factorize()[0]).corr(method='pearson')

sns.heatmap(correlation_matrix, annot = True)

plt.title("Correlation matrix for Movies")

plt.xlabel("Movie features")

plt.ylabel("Movie features")

plt.show()

correlation_mat = df.apply(lambda x: x.factorize()[0]).corr()

corr_pairs = correlation_mat.unstack()

print(corr_pairs)

sorted_pairs = corr_pairs.sort_values(kind="quicksort")

print(sorted_pairs)

strong_pairs = sorted_pairs[abs(sorted_pairs) > 0.5]

print(strong_pairs)

# Looking at the top 15 compaies by gross revenue

CompanyGrossSum = df.groupby('company')[["gross"]].sum()

CompanyGrossSumSorted = CompanyGrossSum.sort_values('gross', ascending = False)[:15]

CompanyGrossSumSorted = CompanyGrossSumSorted['gross'].astype('int64')

CompanyGrossSumSorted

df['Year'] = df['released'].astype(str).str[:4]
df

df.groupby(['company', 'year'])[["gross"]].sum()

CompanyGrossSum = df.groupby(['company', 'year'])[["gross"]].sum()

CompanyGrossSumSorted = CompanyGrossSum.sort_values(['gross','company','year'], ascending = False)[:15]

CompanyGrossSumSorted = CompanyGrossSumSorted['gross'].astype('int64')

CompanyGrossSumSorted

CompanyGrossSum = df.groupby(['company'])[["gross"]].sum()

CompanyGrossSumSorted = CompanyGrossSum.sort_values(['gross','company'], ascending = False)[:15]

CompanyGrossSumSorted = CompanyGrossSumSorted['gross'].astype('int64')

CompanyGrossSumSorted

plt.scatter(x=df['budget'], y=df['gross'], alpha=0.5)
plt.title('Budget vs Gross Earnings')
plt.xlabel('Gross Earnings')
plt.ylabel('Budget for Film')
plt.show()

# Review the data set after adjustment
df

df_numerized = df

for col_name in df_numerized.columns:
    if(df_numerized[col_name].dtype == 'object'):
        df_numerized[col_name]= df_numerized[col_name].astype('category')
        df_numerized[col_name] = df_numerized[col_name].cat.codes

df_numerized

df_numerized.corr(method='pearson')

correlation_matrix = df_numerized.corr(method='pearson')

sns.heatmap(correlation_matrix, annot = True)

plt.title("Correlation matrix for Movies")

plt.xlabel("Movie features")

plt.ylabel("Movie features")

plt.show()

for col_name in df.columns:
    if(df[col_name].dtype == 'object'):
        df[col_name]= df[col_name].astype('category')
        df[col_name] = df[col_name].cat.codes
df