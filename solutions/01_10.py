def sgd_train(X, y, batch_size, max_iter, learning_rate):
    X = np.hstack((X, np.ones(shape=(X.shape[0], 1))))
    y = np.atleast_2d(y).T
    # Initialize randomly the weights
    coefs = np.random.rand(X.shape[1], 1)

    it = 0
    while it < max_iter:
        # select a minibatch
        idx = np.random.choice(np.arange(X.shape[0]),
                               size=batch_size)
        X_subset, y_subset = X[idx], y[idx]
        for sample_idx in range(X_subset.shape[0]):
            # compute the gradient
            dnll = grad_nll(X_subset, y_subset[[sample_idx]], coefs[[sample_idx]])
            # update the parameter
            coefs -= learning_rate * dnll
        it += 1
    return coefs
