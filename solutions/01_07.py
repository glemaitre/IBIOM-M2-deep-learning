class ManualLinearClassifier:
    def __init__(self, decision_points):
        self.decision_points = decision_points
    
    def fit(self, X, y):
        dummy_feature = np.ones(shape=(self.decision_points.shape[0], 1))
        self.intercept_ = -1
        self.coefs_ = np.linalg.solve(self.decision_points, dummy_feature)
        
    def decision_function(self, X):
        return (np.dot(X, self.coefs_) + self.intercept_).ravel()

    @staticmethod
    def _sigmoid(X):
        return 1 / (1 + np.exp(-X))
    
    def predict_proba(self, X):
        prob = self._sigmoid(self.decision_function(X))
        return np.vstack((1 - prob, prob)).T
    
    def predict(self, X):
        dist = np.sign(self.decision_function(X))
        dist[dist < 0] = 0
        return dist.astype(int)
