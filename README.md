Decision Tree Classifier
This repository contains a simple implementation of a decision tree classifier in Python. The decision tree classifier is built using the Gini index to find the best attribute for splitting the dataset at each step.

Functions
calculate_gini(labels)
Calculates the Gini index for a given set of labels.

Parameters:
labels (list): A list of labels for the dataset.
Returns:
gini (float): The Gini index for the labels.
split_dataset(data, labels, attribute_index, attribute_value)
Splits the dataset based on a given attribute and its value.

Parameters:
data (list of lists): The dataset features.
labels (list): The labels corresponding to the dataset.
attribute_index (int): The index of the attribute to split on.
attribute_value (str/int/float): The value of the attribute to split on.
Returns:
left_data, left_labels, right_data, right_labels: The resulting datasets and labels after the split.
find_best_split(data, labels)
Finds the best attribute and value to split the dataset on to minimize the Gini index.

Parameters:
data (list of lists): The dataset features.
labels (list): The labels corresponding to the dataset.
Returns:
best_attribute_index (int): The index of the best attribute to split on.
best_attribute_value (str/int/float): The value of the best attribute to split on.
best_left_data, best_left_labels, best_right_data, best_right_labels: The resulting datasets and labels after the best split.
build_decision_tree(data, labels)
Builds the decision tree recursively.

Parameters:
data (list of lists): The dataset features.
labels (list): The labels corresponding to the dataset.
Returns:
node (dict or str): The decision tree represented as nested dictionaries, or a string if it is a leaf node.
predict(tree, example)
Predicts the label for a given example using the decision tree.

Parameters:
tree (dict): The decision tree.
example (list): The example to predict.
Returns:
prediction (str): The predicted label for the example.
Example
Here is an example of how to use the decision tree classifier:

python
Copy code
# Sample data
data = [
    ['Some', 'F', 'F', 'T', 'Some', '$$$', 'F', 'T', 'French', '0-10', 'T'],
    ['Full', 'F', 'F', 'T', 'Full', '$', 'F', 'F', 'Thai', '30-60', 'F'],
    # ... more data ...
]

# Extract features and labels
features = [row[:-1] for row in data]
labels = [row[-1] for row in data]

# Build decision tree
decision_tree = build_decision_tree(features, labels)

# Example to predict
new_example = ['Full', 'F', 'F', 'T', 'Full', '$', 'F', 'F', 'Thai', '30-60']

# Predict using decision tree
prediction = predict(decision_tree, new_example)
print("Prediction for the new example:", prediction)
Installation
This implementation does not require any special libraries, only Python 3.

Usage
Copy the code for the functions into your Python environment and use the example provided to build and test the decision tree classifier.

License
This project is licensed under the MIT License.

Contact
For any questions or suggestions, please contact the repository owner.
