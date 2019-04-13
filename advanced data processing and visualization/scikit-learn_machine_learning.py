# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 18:19:21 2018

@author: bxu601
"""

# 利用KNN分类算法进行分类
from sklearn import datasets, neighbors
iris = datasets.load_iris()
knn = neighbors.KNeighborsClassifier()
# 从已有数据中学习
knn.fit(iris.data, iris.target)
# 利用分类模型进行未知数据的预测（确定标签）
print(knn.predict([[5.0, 3.0, 5.0, 2.0]]))

# 利用k-means聚类算法进行聚类
from sklearn import cluster, datasets
iris = datasets.load_iris()
kmeans = cluster.KMeans(n_clusters = 3).fit(iris.data)
pred = kmeans.predict(iris.data)   # 确定数据的类别
# 比较算法正确率
for label in pred:
    print(label, end = ' ')    # 打印预测出的各条数据的标签
print('\n')
for label in iris.target:
    print(label, end = ' ')    # 打印原始标注好的正确标签  
print()

from sklearn import svm, datasets
iris = datasets.load_iris()
svc = svm.LinearSVC()
svc.fit(iris.data, iris.target) # 学习
print(svc.predict([[ 5.0, 3.0, 5.0, 2.0]]))  # 预测