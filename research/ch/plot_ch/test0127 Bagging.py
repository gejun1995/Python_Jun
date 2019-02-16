import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

dataMat = np.random.multivariate_normal([1, 2], [[1, 0], [0, 10]], 1000)
labelMat = np.zeros(1000)
labelMat[:500] = 1
plt.scatter(dataMat[:, 0], dataMat[:, 1], s=15)


def plot_decision_regions(X, y, classifier, resolution=0.02):
    colors = ('lightgreen', 'cyan', 'gray', 'r', 'b')
    markers = ('s', 'x', 'o', '^', 'v')

    x1_min, x1_max = np.min(X[:, 0]) - 1, np.max(X[:, 0]) + 1
    x2_min, x2_max = np.min(X[:, 1]) - 1, np.max(X[:, 1]) + 1
    XX, YY = np.meshgrid(np.arange(x1_min, x1_max, resolution), np.arange(x2_min, x2_max, resolution))
    Z = classifier.predict(np.array([XX.ravel(), YY.ravel()]).T)
    Z = Z.reshape(XX.shape)
    plt.contourf(XX, YY, Z, alpha=.4)
    plt.xlim((XX.min(), XX.max()))
    plt.ylim((YY.min(), YY.max()))

    # plot class samples
    for idx, l in enumerate(np.unique(y)):
        plt.scatter(X[y == l, 0], X[y == l, 1], alpha=0.8, marker=markers[idx], label=l)

    plt.savefig('bagging.png')


baggingClassifier = BaggingClassifier()

X_train, X_test, y_train, y_test = train_test_split(dataMat, labelMat)

baggingClassifier.fit(X_train, y_train)
y_test_pred = baggingClassifier.predict(X_test)
plot_decision_regions(X_test, y_test, baggingClassifier)

print(classification_report(y_test, y_test_pred))
