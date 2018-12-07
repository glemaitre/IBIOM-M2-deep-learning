plt.scatter(X[:, 0], X[:, 1], c=y)
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1]);
plt.plot(decision_points[:, 0], decision_points[:, 1]);
