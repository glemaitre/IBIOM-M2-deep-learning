def decision_function(X, coefs, intercept):
    return np.dot(X, coefs) + intercept
