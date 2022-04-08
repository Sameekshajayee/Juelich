import pandas as pd
import seaborn as sns
from os.path import join
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, plot_roc_curve, accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

#1. Loading the data and first investigation
#a. Import the data with pandas and store the dataframe as variable

path = r'C:\Users\samee\Masters Internship\course_material\course_material\excercises\d3'
file= 'cancer_data.xlsx'
cancer_path= join(path,file)
df= pd.read_excel(cancer_path)

#b. Store the feature names in a variable
features= df.columns

#c. How many samples and features contain the data set
total = df.shape
print(f'The number of samples {total[0]} and number of features {total[1]}')

#Solutions way:
count_samples, count_features= df.shape

#d. How many samples are malignant(target=1), how many are benign?
malignant= df['target'].value_counts()[1]
#print(malignant)
benign= df['target'].value_counts()[0]
#print(benign)

#Solutions way:
counts_malignant= df[df['target']==1].shape[0]
counts_benign= df[df['target']==0].shape[0]

#e. Display the target as bar chart (hint: seabor.countplot)

sns.countplot(data=df, x =df['target'], label='frequency')
plt.show()

#2. Preprocessing
#1. Divide the dataset into X (feature values ) and Y (labels)
x= df.iloc[:,1:]
y= df.iloc[:,1]

#Solutions:
X = df.iloc[:, 1:]
y = df['target']

#b. Split the data into 70% training and 30% test data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3,random_state=42 )

#c. Fit the StandardScaler to the training data only. Transform training and test data
#Normalisation
scaler= StandardScaler()
scaler= scaler.fit(x_train)
x_train= scaler.transform(x_train)
x_test= scaler.transform(x_test)


