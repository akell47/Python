x_small_sample = x_sample[::4]
y_small_sample = func(x_small_sample)

degree, alpha = 4, 10

X = np.array([x_small_sample]).T
fig, axes = plt.subplots(1, 3, figsize=(20, 4))
for no, my_model in enumerate([LinearRegression(), Ridge(alpha=alpha), Lasso(alpha=alpha)]):
    model = make_pipeline(PolynomialFeatures(degree), my_model)
    r2, MSE = [], []
    for k in xrange(100):  # Fit a few times the model to different training sets
        X_train, X_test, y_train, y_test = train_test_split(
            X, y_small_sample, train_size=.7)
        r2.append(model.fit(X_train, y_train).score(X_test, y_test))
        y_pred = model.predict(np.array([domain]).T)
        axes[no].plot(domain, y_pred, alpha=.3)
        y_pred_sample = model.predict(np.array([x_small_sample]).T)
        MSE.append(np.square(y_pred_sample - y_small_sample).sum())
    axes[no].scatter(x_small_sample, y_small_sample, s=70)
    axes[no].set_title("%s (R2 %.2f, MSE %3d)" )
    axes[no].set_xlim(-.2, max(domain)), axes[no].set_ylim(-1, 21)
