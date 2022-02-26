import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from src.myConvexHull import myConvexHull

print('''
Welcome to Convex Hull Visualization!
Enter your desired dataset:
1. Iris (from sklearn)
2. Wine (from sklearn)
3. Breast Cancer (from sklearn)
''')

prompt = int(input())

if prompt == 1:
    data = datasets.load_iris()
elif prompt == 2:
    data = datasets.load_wine()
elif prompt == 3:
    data = datasets.load_breast_cancer()
else:
    print("Data tidak valid. Mengembalikan hasil untuk iris..")
    data = datasets.load_iris()  

df = pd.DataFrame(data.data, columns=data.feature_names)
df['Target'] = pd.DataFrame(data.target)
print(df.shape)
df.head()

#visualisasi hasil ConvexHull
plt.figure(figsize = (10, 6))
colors = ['b','r','g']
plt.title('Petal Width vs Petal Length')
plt.xlabel(data.feature_names[0])
plt.ylabel(data.feature_names[1])
for i in range(len(data.target_names)):
    bucket = df[df['Target'] == i]
    bucket = bucket.iloc[:,[0,1]].values
    hull = myConvexHull(bucket)
    print(hull)
    plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
    for j in range(len(hull)-1):
        plt.plot([hull[j][0], hull[j+1][0]], [hull[j][1], hull[j+1][1]], colors[i])
    plt.plot([hull[len(hull)-1][0], hull[0][0]], [hull[len(hull)-1][1], hull[0][1]], colors[i])
plt.legend()
plt.show()