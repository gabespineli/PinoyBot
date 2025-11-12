import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, classification_report
import numpy as np
import featurematrix as fm

if __name__ == '__main__':
    # ----------- PREPARE THE DATA ----------- #
    
    df = pd.read_csv('csintsy_annotations.csv')

    # Encode words to numbers
    X = np.array(fm.getMatrix(df['word']))
    
    # Extract labels as target
    y = df['label'].values

    # (checker, rows should be the same)
    #print(X.shape)
    #print(y.shape)

    # ----------- SPLIT THE DATASET (70-15-15) ----------- #
    # First split: 70% train, 30% temp (val+test)
    X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # Second split: 50% validation, 50% test (of the 30%)
    X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)
    
    # ----------- TRAIN THE MODEL ----------- #
    model = DecisionTreeClassifier()

    model.fit(X_train,y_train)

    # ----------- VALIDATION PERFORMANCE ----------- #
    val_predictions = model.predict(X_val)
    
    print("="*60)
    print("VALIDATION PERFORMANCE:")
    print("="*60)
    print(f"Accuracy: {accuracy_score(y_val, val_predictions) * 100:.2f}%")
    print(f"Macro F1-Score: {f1_score(y_val, val_predictions, average='macro') * 100:.2f}%")
    print("\n" + classification_report(y_val, val_predictions))

    # ----------- TEST PERFORMANCE ----------- #
    test_predictions = model.predict(X_test)
    
    print("="*60)
    print("TEST PERFORMANCE:")
    print("="*60)
    print(f"Accuracy: {accuracy_score(y_test, test_predictions) * 100:.2f}%")
    print(f"Macro F1-Score: {f1_score(y_test, test_predictions, average='macro') * 100:.2f}%")
    print("\n" + classification_report(y_test, test_predictions))