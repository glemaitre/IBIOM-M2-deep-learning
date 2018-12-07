coefs = np.linalg.solve(decision_points,
                        np.ones(shape=(decision_points.shape[0], 1)))
coefs
