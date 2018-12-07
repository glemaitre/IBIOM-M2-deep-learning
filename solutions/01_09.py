def grad_nll(X, y, coefs):
    y_pred = np.dot(X, coefs)
    y_pred = 1 / (1 + np.exp(-y_pred))
    grad = (y_pred - y)
    return np.dot(X.T, grad)
