from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    # ----------- PREPARE THE DATA ----------- #
    
    iris = load_iris()

    # Extract feature matrix
    X = np.array(iris['data'])

    # Extract labels (correct answers)
    y = np.array(iris['target'])

    # (checker, rows should be the same)
    #print(X.shape)
    #print(y.shape)

    # ----------- SPLIT THE DATASET ----------- #
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    
    # ----------- TRAIN THE MODEL ----------- #
    model = DecisionTreeClassifier()

    model.fit(X_train,y_train)

    plt.figure(figsize=(16,10), dpi=100)
    plot_tree(model, feature_names=iris['feature_names'], class_names=iris['target_names'], filled=True)
    plt.show()