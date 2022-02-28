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
4. Custom dataset (make sure it has target column)
''')

prompt = int(input())

if prompt == 1:
    data = datasets.load_iris()
elif prompt == 2:
    data = datasets.load_wine()
elif prompt == 3:
    data = datasets.load_breast_cancer()
elif prompt == 4:
    filename = input("Masukkan nama file csv yang berada pada folder test: ")
else:
    print("Data tidak valid. Mengembalikan hasil untuk iris..")
    data = datasets.load_iris()  

if (prompt != 4):
    print("Masukkan pilihan kolom pertama: ")
    for i in range(len(data.feature_names)):
        print(str(i+1) + ". " + data.feature_names[i].title())
    first_choice = int(input()) - 1

    print("Masukkan pilihan kolom kedua: ")
    for i in range(len(data.feature_names)):
        print(str(i+1) + ". " + data.feature_names[i].title())
    second_choice = int(input()) - 1

    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['Target'] = pd.DataFrame(data.target)

    #visualisasi hasil ConvexHull
    plt.figure(figsize = (10, 6))
    colors = ['b','r','g']
    plt.title(str(data.feature_names[first_choice].title()) + " vs " + str(data.feature_names[second_choice].title()))
    plt.xlabel(data.feature_names[first_choice])
    plt.ylabel(data.feature_names[second_choice])
    for i in range(len(data.target_names)):
        bucket = df[df['Target'] == i]
        bucket = bucket.iloc[:,[first_choice, second_choice]].values
        hull = myConvexHull(bucket)
        plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
        for j in range(len(hull)-1):
            plt.plot([hull[j][0], hull[j+1][0]], [hull[j][1], hull[j+1][1]], colors[i])
        plt.plot([hull[len(hull)-1][0], hull[0][0]], [hull[len(hull)-1][1], hull[0][1]], colors[i])
    plt.legend()
    plt.show()

else:
    df = pd.read_csv("test/" + filename)
    if ('target') not in df:
        print("File tidak memiliki klom target. Exiting..")
        quit()

    print("Masukkan pilihan kolom pertama: ")
    for i in range(len(df.columns)-1):
        print(str(i+1) + ". " + df.columns.values[i].title())
    first_choice = int(input()) - 1

    print("Masukkan pilihan kolom kedua: ")
    for i in range(len(df.columns)-1):
        print(str(i+1) + ". " + df.columns.values[i].title())
    second_choice = int(input()) - 1

    #visualisasi hasil ConvexHull
    plt.figure(figsize = (10, 6))
    colors = ['b','r','g']
    plt.title(str(df.columns.values[first_choice].title()) + " vs " + str(df.columns.values[second_choice].title()))
    plt.xlabel(df.columns.values[first_choice])
    plt.ylabel(df.columns.values[second_choice])
    for i in range(len(df['target'].unique())):
        bucket = df[df['target'] == i]
        bucket = bucket.iloc[:,[first_choice, second_choice]].values
        hull = myConvexHull(bucket)
        plt.scatter(bucket[:, 0], bucket[:, 1], label=df['target'].unique()[i])
        for j in range(len(hull)-1):
            plt.plot([hull[j][0], hull[j+1][0]], [hull[j][1], hull[j+1][1]], colors[i])
        plt.plot([hull[len(hull)-1][0], hull[0][0]], [hull[len(hull)-1][1], hull[0][1]], colors[i])
    plt.legend()
    plt.show()