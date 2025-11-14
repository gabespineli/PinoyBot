"""
pinoybot.py

PinoyBot: Filipino Code-Switched Language Identifier

This module provides the main tagging function for the PinoyBot project, which identifies the language of each word in a code-switched Filipino-English text. The function is designed to be called with a list of tokens and returns a list of tags ("ENG", "FIL", or "OTH").

Model training and feature extraction should be implemented in a separate script. The trained model should be saved and loaded here for prediction.
"""

import os
import pickle
from typing import List
import numpy as np
import featurematrix as fm

# Main tagging function
def tag_language(tokens: List[str]) -> List[str]:
    """
    Tags each token in the input list with its predicted language.
    Args:
        tokens: List of word tokens (strings).
    Returns:
        tags: List of predicted tags ("ENG", "FIL", or "OTH"), one per token.
    """
    # 1. Load your trained model from disk (e.g., using pickle or joblib)
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)

    # 2. Extract features from the input tokens to create the feature matrix
    features = np.array(fm.getMatrix(tokens))

    # 3. Use the model to predict the tags for each token
    predicted = model.predict(features)

    # 4. Convert the predictions to a list of strings ("ENG", "FIL", or "OTH")
    tags = [str(tag) for tag in predicted]

    # 5. Return the list of tags
    return tags

    # You can define other functions, import new libraries, or add other Python files as needed, as long as
    # the tag_language function is retained and correctly accomplishes the expected task.

if __name__ == "__main__":
    # Example usage
    example_tokens = [
    "Malaking", "epekto", "sa", "Boston", "Celtics", "ang", "pagkawala", "ni", "Jason", 
    "titum", "sa", "kanilang", "line", "up", "nila", "sa", "game", "6", "dahil", 
    "natalo", "Sila", "Ng", "new", "York", "Knicks", "kung", "kamakailan", "SI", 
    "Jason", "titum", "nagkaroon", "Ng", "injury", "dahilan", "Hindi", "sya", 
    "nakalaro", "sa", "game", "6", "at", "nyari", "na", "Sila", "sa", "kamay", 
    "Ng", "new", "York", "knicks"
    ]

    tags = tag_language(example_tokens)
    for token, tag in zip(example_tokens, tags):
        print(token, tag)