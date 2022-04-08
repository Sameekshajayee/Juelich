#create a dictionary
patient = {'name': 'Sameeksha', 'age':25,'disease':'Alzeimers','therapy':'drug b','response':'True'}

#Iterating over dictionaries
for characteristic in  patient:
    print(characteristic,patient[characteristic])

# Create a dictionary with multiple values
names = ['Max', 'Peter', 'Abby']
age=[77, 54, 28]
disease=['Alzheimers', 'Parkinson', 'Alzheimers']
therapy=['Drug B', 'Drug A', 'Drug B']
response=[True, False, False]

patients={'name':names,
          'age': age,
          'disease':disease,
          'therapy':therapy,
          'response':response}




# DATAFRAMES
# creating a dataframes
import pandas as pd
from os.path import join
df= pd.DataFrame(patients)

#Saving a data frame as excel file
path = r'C:\Users\samee\Masters Internship\course_material\course_material\slides'
output_path= join(path,'test_excel.xlsx')
df.to_excel(output_path)

# The IRIS DataSet
path= r'C:\Users\samee\Masters Internship\course_material\course_material\excercises\d2'
# To read a data frame stored in excel file
df_iris=pd.read_excel(join(path,'iris_data.xlsx'))

#df_iris.iloc[0:5, :]   gets rows (and/or columns) at integer locations.
#df_iris.loc[0:5, 'target']  gets rows (and/or columns) with particular labels.

# Masking and Indexing
#Set up a specifing condition that creates a "Boolean Mask"
mask = df_iris['target']=='setosa'
setosa=df_iris[mask]

# Exploratory statistical analysis
#dataframe.describe()---- all common metrics(mean,median,std...) of the data set

#Data Visulisation
# 1.  Bar Plot

#Get unique counts for each category
#counts=df_iris['target'].value_counts()
import matplotlib.pyplot as plt
plt.figure()
plt.bar(counts.keys(), counts.values)
plt.ylabel('Sample counts')
plt.show()

# 2. Histogram
plt.figure()
plt.hist(setosa['sepal length (cm)'])
plt.xlabel('sepal length (cm)')
plt.ylabel('Sample counts')
plt.show()


# Multiple Histograms
def plot_axes(data):
    fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(10,8))
    axs= axs.flatten()
    for i in range(0,4):
        column=data.keys()[i]
        axs[i].hist(data[column])
        axs[i].set_xlabel(column)
        axs[i].set_ylabel("Sample counts")
    return plt.show()
plot_axes(setosa)

#Plot Histogram for another IRIS subtype

viginica= df_iris[df_iris['target']=='virginica']
plot_axes(viginica)

#Compare Distrubutions of IRIS subtypes for a specifc features
# SEABORN
#KDE- Density plot is a variation of a histogram and useful when comparing multiple distribution in one plot
import seaborn as sns
plt.figure()
sns.kdeplot(setosa['sepal length (cm)'])
sns.kdeplot(viginica['sepal length (cm)'])
plt.legend(['setosa', 'virginica'])
plt.xlabel('sepal length (cm)')
plt.ylabel('Normalized sample counts')
plt.show()



# 3. Scatter Plot
# Useful to find relationships between data
# pyplot.scatter() to plot a scatter plot between two continuous variables
plt.figure()
plt.scatter(setosa['sepal length (cm)'],setosa['sepal width (cm)'], c='b')
plt.scatter(viginica['sepal length (cm)'], viginica['sepal width (cm)'], c='r')
plt.legend(['setosa', 'virginica'])
plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width(cm)')
plt.show()


# Pair Plot
sns.pairplot(df_iris, hue='target', diag_kind='kde')
plt.show()

# Linear Correlation between two variables
#The linear correlation coefficient measures the strength of the linear relationship between two variables.
# If r is close to ±1, the two variables are highly correlated and if plotted on a scatter plot,
# the data points cluster about a line. If r is far from ±1, the data points are more widely scattered.

import numpy as np
def correlation(data):
    corr_coef= round(np.corrcoef(data['sepal length (cm)'],
                                 data['sepal width (cm)']) [0][1], 3)
    return corr_coef
corr_coef_setosa = correlation(setosa)
corr_coef_viginica = correlation(viginica)

def parameters(data):
    slope, intercept = np.polyfit(data['sepal length (cm)'], data['sepal width (cm)'], deg=1)
    return slope, intercept

slope_setosa, intercept_setosa = parameters(setosa)
slope_viginica, intercept_viginica = parameters(viginica)

x_values_setosa= setosa['sepal length (cm)']
y_values_setosa= setosa['sepal width (cm)']

x_values_vignica= viginica['sepal length (cm)']
y_values_viginica= viginica['sepal width (cm)']

plt.figure()

#1. Setosa
plt.scatter(x_values_setosa, y_values_setosa)
plt.plot(x_values_setosa, x_values_setosa*slope_setosa+intercept_setosa)

#2. Viginica
plt.scatter(x_values_vignica, y_values_viginica)
plt.plot(x_values_vignica, x_values_vignica*slope_viginica+intercept_viginica)

#3. Correlation Coefficients
plt.text(7.5, 4.85, f'setosa r:{corr_coef_setosa}',
         horizontalalignment='center',
         verticalalignment= 'center')
plt.text(7.5, 4.7, f'virginica r:{corr_coef_viginica}',
         horizontalalignment='center',
         verticalalignment='center')
plt.xlabel('sepal legth (cm)')
plt.ylabel('sepal width (cm)')
plt.show()


# Correlation HeatMap
# Find relationship between all variable and visualize in color

mask= np.tril(df_iris.corr())
heatmap_matrix = sns.heatmap (correlation_matrix, annot= True,
                              vmin=-1, vmax=1, cmap='coolwarm', mack=mask)








