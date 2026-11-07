
# Decision Tree Implementation

# Training dataset
data = [
    ['Sunny', 'No'],
    ['Sunny', 'No'],
    ['Rainy', 'Yes'],
    ['Rainy', 'Yes'],
    ['Cloudy', 'Yes']
]

# Count Yes and No
def count_values(data):
    yes = 0
    no = 0

    for row in data:
        if row[1] == 'Yes':
            yes += 1
        else:
            no += 1

    return yes, no

# Build Decision Tree
def decision_tree(data):
    yes, no = count_values(data)

    if yes > no:
        return 'Yes'
    elif no > yes:
        return 'No'
    else:
        return 'Yes'

# Prediction
print("Decision Tree Algorithm")
print("-----------------------")

weather = input("Enter weather (Sunny/Rainy/Cloudy): ")

if weather == 'Sunny':
    result = 'No'
elif weather == 'Rainy':
    result = 'Yes'
elif weather == 'Cloudy':
    result = 'Yes'
else:
    result = decision_tree(data)

print("Prediction:", result)
