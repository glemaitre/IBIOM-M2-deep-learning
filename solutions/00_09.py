pipe = make_pipeline(MinMaxScaler(), SGDClassifier(loss='log'))
