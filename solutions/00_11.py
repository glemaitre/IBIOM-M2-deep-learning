from sklearn.metrics import recall_score
recall_score(y_test, pipe.predict(X_test), average=None)
