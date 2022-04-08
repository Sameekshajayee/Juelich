import pandas as pd
import seaborn as sns
from os.path import join
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, plot_roc_curve, accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier


#%% 1)
# a)

path = r'C:\Users\samee\Masters Internship\course_material\course_material\excercises\d3'
file= 'cancer_data.xlsx'
cancer_path= join(path,file)
data= pd.read_excel(cancer_path)

# b)
features = data.columns

# c)
counts_samples, counts_features = data.shape

# d)
counts_malignant = data[data['target'] == 1].shape[0]
counts_benign = data[data['target'] == 0].shape[0]

# e)
sns.countplot(data['target'], label='frequency')
plt.show()

#%% 2) Preprocessing
# a)
X = data.iloc[:, 1:]
y = data['target']

# b)
# split data train 70 % and test 30 %
x_train, x_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.3,
                                                    random_state=42)

# c) normalization
x_train_before = x_train
scaler = StandardScaler()
scaler = scaler.fit(x_train)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

# d)
# In general it is a good idea to use the test set only one time in the end of the experiment to
# test the performance of the algorithm. Therefore before this step you should not touch the test
# set. This will increase the generalizability of your model.

# e) Histogram
plt.figure()
plt.hist(x_train_before.iloc[:, 0], histtype='stepfilled', bins=20)
plt.hist(x_train[:, 0], histtype='stepfilled', bins=20)
plt.legend(['Before Normalization', 'After Normalization'])
plt.title('Normalization')
plt.xlabel('Texture Mean')
plt.ylabel('Frequency')
plt.show()


#%% 3) Modelling
# a)
clf_rf = RandomForestClassifier(n_estimators=100, random_state=42)

# b)
clf_rf = clf_rf.fit(x_train, y_train)
clf_rf.classes_  # 0: Benign, 1: Malignant

# c)
probabilities = clf_rf.predict_proba(x_test)
predictions = clf_rf.predict(x_test)

#%% 4) Evaluation
# a)
cm = confusion_matrix(y_test, predictions)
# Extra: Visualization of the confusion matrix
sns.heatmap(cm, annot=True, cmap='Blues', cbar=False)
plt.show()

# b)
FP = cm[0, 1]
FN = cm[1, 0]
print(f'Wrong malignant: {FP}\nWrong benign: {FN}')

# c)
plot_roc_curve(clf_rf, x_test, y_test)
plt.show()

# d)
ac = accuracy_score(y_test, predictions)
print('Accuracy is: ', ac)

# e)


def accuracy(cm):
    FN = cm[1, 0]
    TP = cm[1, 1]
    TN = cm[0, 0]
    FP = cm[0, 1]
    ACC = (TP + TN) / (TP + TN + FP + FN)
    return round(ACC, 2)

accuracy(cm)

# f)
# Imagine you have a disbalanced dataset which means you have 90% tumor A and 10% tumor B.
# Given a classifier that predicts everything tumor A you achieve a high accuracy even though tumor B
# has not been classified correctly a single time. In contrast the AUC for such a classifier would have been very low
# showing you a poor performance of the classifier.
