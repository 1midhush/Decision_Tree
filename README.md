# Decision Tree for Table Serving Prediction

This project implements a decision tree algorithm to predict whether a table should be served or not based on various attributes. The decision tree is constructed using the Gini index as the splitting criterion.

## Dataset

The dataset used for training and testing the decision tree consists of the following variables:

1. **Altitude (Alt)**: Altitude of the restaurant, categorized as "Some" or "Full".
2. **Bar Availability (Bar)**: Availability of a bar at the restaurant, categorized as "T" (True) or "F" (False).
3. **Day of the Week (Fri)**: Whether it's a Friday or not, categorized as "T" (True) or "F" (False).
4. **Hungry (Hun)**: Whether the customer is hungry or not, categorized as "T" (True) or "F" (False).
5. **Patron Type (Pat)**: Type of patron, categorized as "Some", "Full", or "None".
6. **Price Range (Price)**: Price range of the restaurant, categorized as "$", "$$", or "$$$".
7. **Rainy Weather (Rain)**: Whether it's raining or not, categorized as "T" (True) or "F" (False).
8. **Reservation (Res)**: Whether a reservation has been made, categorized as "T" (True) or "F" (False).
9. **Cuisine Type (Type)**: Type of cuisine offered at the restaurant.
10. **Estimated Wait Time (Est)**: Estimated wait time for a table, categorized as "0-10", "10-30", "30-60", or ">60" minutes.

## Usage

1. **Install Required Packages**: Ensure you have Python installed along with the necessary packages. You can install the required packages using pip:
    ```
    pip install pandas
    ```

2. **Prepare Dataset**: Prepare your dataset in CSV format with the specified variables.

3. **Run the Script**: Run the `decision_tree.py` script to train the decision tree model and make predictions. Ensure to update the file path in the script to point to your dataset.

## Example

Here's an example of how to use the decision tree model:

```python
# Example usage of the decision tree model
# Make sure to provide the necessary data
new_example = ['Full', 'F', 'F', 'T', 'Full', '$', 'F', 'F', 'Thai', '30-60']

# Predict using decision tree
prediction = predict(decision_tree, new_example)
print("Prediction for the new example:", prediction)
