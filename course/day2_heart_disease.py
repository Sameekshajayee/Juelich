from os.path import join
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#1.)
# a)
base=  r'C:\Users\samee\Masters Internship\course_material\course_material\excercises\d2'
file = 'heart.xlsx'
path = join(base,file)

df= pd.read_excel(path)

#b) To read columns
features= df.columns
print(features)


#c) number of unique targets
print(df['target'].unique())
print(df['target'].unique().shape[0])

#d.) Individual patients in the dataset
print(df.shape[0])

#e) First five patients
five= df[0:5]
print(five)

#Solutions way:
df.head(5)
#or
#df.iloc[0:5,:]


#f.) Quick description of the data set and only of the column age

df.describe()
df['age'].describe()

#g.) how many patients are with the heart disease and how many without ?
total=df.shape[0]
print(f'Total number of patients:{total}' )
p_w_disease= df['target']==True
count=df[p_w_disease].shape[0]
print(f'Number of patients with heart disease:{count}')

p_wo_disease= df['target']==False
count2=df[p_wo_disease].shape[0]
print(f'Number of patients without heart disease:{count2}')


#Solution :
#counts_no_disease=df['target'].value_counts()[0]




#2. Deeper Investigating
#a) already done in previous part
heart_disease = df[p_w_disease]
no_heart_disease= df[p_wo_disease]
#b) Histogram
plt.figure()
plt.hist(heart_disease['age'])
plt.xlabel('Age')
plt.ylabel('No. of patients')
plt.title('With Heart Disease')
plt.show()

plt.hist(no_heart_disease['age'])
plt.xlabel('Age')
plt.ylabel('No. of patients')
plt.title('Without Heart Disease')
plt.show()
print(heart_disease['age'].describe())

print(no_heart_disease['age'].describe())


#c. Bar Chart
bar_width= 0.25
#Counting the number 1's and 0's i.e male and female
count_disease = heart_disease['sex'].value_counts()
no_count_disease = no_heart_disease['sex'].value_counts()
plt.figure()

plt.bar(count_disease.keys() ,count_disease.values , width=bar_width)
plt.bar(no_count_disease.keys()+ bar_width, no_count_disease.values, width= bar_width )
#plt.bar(no_count_disease.keys() + bar_width,no_count_disease.values, width=bar_width)
#plt.xlabel('Sex')
#plt.ylabel('No. of patients')
#plt.show()

plt.xlabel('Sex', fontweight='bold')
plt.xticks(count_disease.keys()+bar_width/2,['male', 'female'])
#plt.xticks(count_disease.keys() + bar_width/2, ['male', 'female'])
plt.ylabel('Counts')
plt.legend(['Disease', 'No_Disease'])
plt.show()



OR



sns.countplot(data= heart_disease, x= 'sex', hue= 'target')
plt.show()

sns.countplot(x='target', hue='sex', data=heart_disease)
plt.show()


#d. PIE CHART

labels = ['male', 'female']
fig, axs = plt.subplots(nrows=1, ncols=2 , figsize=(8,4))
axs=axs.flatten()
axs[0].pie(count_disease.values, labels=labels)
axs[0].set_title("With Heart Disease")
axs[1].pie(no_count_disease.values, labels=labels)
axs[1].set_title("Without Heart Disease")
plt.show()

# Solution given

labels = ['male', 'female']
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
axs = axs.flatten()
axs[0].pie(counts_disease.values, labels=labels, startangle=90, autopct='%1.0f%%', textprops=dict(fontsize=16))
axs[0].set_title('Heart Disease')
axs[1].pie(counts_no_disease.values, labels=labels, startangle=90, autopct='%1.0f%%', textprops=dict(fontsize=16))
axs[1].set_title('No Heart Disease')
plt.show()



#3. Deeper Investigation.
#a. Scatter Plot of age and cholestrol
plt.figure()
plt.scatter(heart_disease['age'], heart_disease['cholesterol'], c='b')
plt.scatter(no_heart_disease['age'], no_heart_disease['cholesterol'], c='r')
plt.legend(['with heart disease', 'no heart disease'])
plt.xlabel('age')
plt.ylabel('cholesterol')
plt.show()


# Solutions
plt.figure()
plt.scatter(heart_disease['cholesterol'], heart_disease['age'])
plt.scatter(no_heart_disease['cholesterol'], no_heart_disease['age'])
plt.legend(['Disease', 'No_Disease'])
plt.show()

#b. Write two functions. One calculate the correlation between two features.
#What kind of assumption can you make now ?

def corr(feature1, feature2):
    corr_coeff = round (np.corrcoef(feature1,feature2)[0][1],3)
    return corr_coeff
#The other calculate the slope and intercept for linear regression.
def parameters(feature1,feature2):
    slope, intercept=np.polyfit(feature1, feature2, deg=1)
    return slope, intercept
#Use these to calculate the correlation coefficients, slope and intercept for the features age and cholesterol.
feature2= heart_disease['age']
feature1= heart_disease['cholesterol']
correlation_with = corr(feature1,feature2)
slope_with, intercept_with= parameters(feature1,feature2)

feature4= no_heart_disease['age']
feature3= no_heart_disease['cholesterol']
correlation_wo = corr(feature3,feature4)
slope_wo, intercept_wo= parameters(feature3,feature4)

x_values_w= feature1
y_values_w= feature2

x_values_wo= feature3
y_values_wo= feature4

#Plot everything in a scatter plot.
#Remember not to plt.show() everything it should be just added in the last
#1.
plt.scatter(x_values_w,y_values_w)
plt.plot(x_values_w, x_values_w*slope_with+intercept_with)


#2.
plt.scatter(x_values_wo,y_values_wo)
plt.plot(x_values_wo, x_values_wo*slope_wo+intercept_wo)


#3. Correlation Coefficient

plt.text(500, 32, f'disease r: {correlation_with}',
         horizontalalignment='center',
         verticalalignment='center')
plt.text(500, 30, f'no_disease r: {correlation_wo}',
         horizontalalignment='center',
         verticalalignment='center')
plt.legend(['Disease', 'No_Disease'])
plt.xlabel('cholesterol')
plt.ylabel('age')
plt.show()

#c. Correlation Matrix

plt.figure(figsize=(16,10)) # To define the size of the figure
mask=np.tril(df.corr()) #df.corr(): gives the correlation between all the variables # np.tril: just keeps the main diagnoal and lower trinagle
correlation_matrix = df.corr() # array with all the correlation values
#heat= sns.heatmap(correlation_matrix,mask=mask)

heat = sns.heatmap(correlation_matrix, annot= True, mask= mask)
plt.show()