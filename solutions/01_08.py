from sklearn.metrics import accuracy_score
clf = ManualLinearClassifier(decision_points)
clf.fit(X, y)
print('The mean accuracy is: ', accuracy_score(y, clf.predict(X)))
