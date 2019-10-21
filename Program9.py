import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix,accuracy_score

names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
df = pd.read_csv("Data_8_9.csv", names = names)
print(df.head())

#seperate X and Y values
x = df.iloc[:, :-1].values 
y = df.iloc[:,-1].values

x_train, x_test, y_train, y_test = train_test_split(x, y)

scaler = StandardScaler()
scaler.fit(x_train)

x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

#Model
classifier = KNeighborsClassifier(n_neighbors = 3)
classifier.fit(x_train, y_train)

y_pred = classifier.predict(x_test)
print()
for i in range(len(y_pred)):
    print ("Actual Label : ",y_test[i],"Predicted Label : ",y_pred[i])
print ("*"*10)
    
print ("Confusion Matrix : ")
print(confusion_matrix(y_test, y_pred))
print("Accuracy: ",accuracy_score(y_test, y_pred)*100)
print ("Classification Report : ")
print(classification_report(y_test, y_pred))