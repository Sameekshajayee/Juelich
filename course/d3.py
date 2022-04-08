import pandas as pd
from os.path import join

path =  r'C:\Users\samee\Masters Internship\course_material\course_material\excercises\d2'
df_iris = pd.read_excel(join(path,'iris_data.xlsx'))
# Select only Versicolor and Virginica
subset_iris = df_iris[(df_iris['target']=='versicolor') | (df_iris['target']=='virginica')]

#X: Feature Values, Y: labels

x= subset_iris.iloc[:,:-1] # all the rows, all the columns except last
y= subset_iris.iloc[:,-1] # all the rows of the last column

# Divide the dataset in training and test set

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test= train_test_split(x,y,test_size= 0.3, random_state=42)

#Training and test set
#x_train.shape #x_test.shape
