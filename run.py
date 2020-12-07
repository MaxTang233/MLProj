from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import average_precision_score
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import plot_precision_recall_curve
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn import tree

import matplotlib.pyplot as plt
from util import *
import numpy as np


X1, y1 = read_dataset ("project3_dataset1.txt")
X2, y2 = read_dataset ("project3_dataset2.txt")

def ten_fold_cross_validation(X, y, algo, params):
#Accuracy, Precision, Recall, F-1 measure, and AUC (area under
#the curve)
	
	'''Here we divided X into 10 sets, 9/10 of the data are 
	using as training data each time, and the remaining 1/10 
	are using as test data. 

	- X1 is a (569, 30) numpy array representing the features, 
	- y1 is a (569, ) array representing the labels for X1

	- X2 is a (462, 9) numpy array, 
	- y2 is a (462, ) array

	'''

	#Decide which classifier to use
	if algo == 'Logistic Regression':
		clf = LogisticRegression(random_state=0)
	if algo == 'Knn':
		clf = KNeighborsClassifier(n_neighbors=params)
	if algo == 'SVM':
		#TODO: what does this mean
		clf = make_pipeline(StandardScaler(), SVC(gamma='auto'))
	if algo == 'Decision Tree':
		clf = tree.DecisionTreeClassifier()


	kf = KFold(n_splits=10)
	i = 0
	for train_index, test_index in kf.split(X):
	# 	print("TRAIN:", train_index, "TEST:", test_index)
		X_train = X[train_index]
		y_train = y[train_index]
		X_test = X[test_index]
		y_test = y[test_index]
		
		clf.fit(X_train, y_train)
		disp = plot_precision_recall_curve(clf, X_test, y_test)
		disp.ax_.set_title('2-class Precision-Recall curve: ')
		plt.savefig(algo+ str(i) +'.png')
		i+=1


if __name__ == '__main__':
	ten_fold_cross_validation(X1, y1, 'SVM', None)
	# ten_fold_cross_validation(X1, y1, 'Knn', 3)










