from collections import Counter

# Function to calculate Gini index
def calculate_gini(labels):
    total_samples = len(labels)
    class_counts = Counter(labels)
    gini = 1
    for cls in class_counts:
        cls_probability = class_counts[cls] / total_samples
        gini -= cls_probability ** 2
    return gini

# Function to split dataset based on attribute value
def split_dataset(data, labels, attribute_index, attribute_value):
    left_data, left_labels, right_data, right_labels = [], [], [], []
    for i, row in enumerate(data):
        if row[attribute_index] == attribute_value:
            left_data.append(row)
            left_labels.append(labels[i])
        else:
            right_data.append(row)
            right_labels.append(labels[i])
    return left_data, left_labels, right_data, right_labels

# Function to find the best attribute for splitting
def find_best_split(data, labels):
    num_attributes = len(data[0])
    best_attribute_index = -1
    best_gini = float('inf')
    for col in range(num_attributes):
        attribute_values = set(row[col] for row in data)
        for val in attribute_values:
            left_data, left_labels, right_data, right_labels = split_dataset(data, labels, col, val)
            gini = (len(left_labels) / len(labels)) * calculate_gini(left_labels) + \
                   (len(right_labels) / len(labels)) * calculate_gini(right_labels)
            if gini < best_gini:
                best_gini = gini
                best_attribute_index = col
                best_attribute_value = val
                best_left_data = left_data
                best_left_labels = left_labels
                best_right_data = right_data
                best_right_labels = right_labels
    return best_attribute_index, best_attribute_value, best_left_data, best_left_labels, \
           best_right_data, best_right_labels

# Function to build decision tree
def build_decision_tree(data, labels):
    # Base case: If all labels are the same, return leaf node
    if len(set(labels)) == 1:
        return labels[0]
    
    # Find the best attribute for splitting
    best_attribute_index, best_attribute_value, left_data, left_labels, \
    right_data, right_labels = find_best_split(data, labels)
    
    # Recursive call to build left and right subtrees
    left_subtree = build_decision_tree(left_data, left_labels)
    right_subtree = build_decision_tree(right_data, right_labels)
    
    # Construct node
    node = {'attribute_index': best_attribute_index,
            'attribute_value': best_attribute_value,
            'left_subtree': left_subtree,
            'right_subtree': right_subtree}
    
    return node

# Function to predict using decision tree
def predict(tree, example):
    if isinstance(tree, str):  # Leaf node
        return tree
    attribute_index = tree['attribute_index']
    attribute_value = example[attribute_index]
    if attribute_value == tree['attribute_value']:
        return predict(tree['left_subtree'], example)
    else:
        return predict(tree['right_subtree'], example)

# Sample data
# Format: [Alt, Bar, Fri, Hun, Pat, Price, Rain, Res, Type, Est, Wait]
data = [
    ['Some', 'F', 'F', 'T', 'Some', '$$$', 'F', 'T', 'French', '0-10', 'T'],
    ['Full', 'F', 'F', 'T', 'Full', '$', 'F', 'F', 'Thai', '30-60', 'F'],
    ['Some', 'T', 'F', 'F', 'None', '$', 'T', 'F', 'Burger', '0-10', 'T'],
    ['Full', 'F', 'T', 'T', 'Some', '$', 'F', 'F', 'Thai', '10-30', 'T'],
    ['Full', 'F', 'F', 'F', 'Some', '$$$', 'F', 'T', 'French', '>60', 'F'],
    ['Some', 'F', 'T', 'F', 'Full', '$$', 'F', 'T', 'Italian', '0-10', 'T'],
    ['None', 'F', 'F', 'F', 'None', '$', 'F', 'F', 'Burger', '0-10', 'F'],
    ['Some', 'T', 'F', 'F', 'Some', '$$', 'T', 'T', 'Thai', '0-10', 'T'],
    ['Full', 'T', 'T', 'T', 'Full', '$', 'T', 'F', 'Burger', '>60', 'F'],
    ['Full', 'T', 'T', 'T', 'Full', '$$$', 'F', 'T', 'Italian', '10-30', 'F'],
    ['Some', 'F', 'F', 'F', 'None', '$', 'T', 'T', 'Thai', '0-10', 'F'],
    ['Full', 'T', 'T', 'T', 'Full', '$', 'F', 'F', 'Burger', '30-60', 'T']
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

