'''
Recap - Recipe Manager
Let's recap what we have learned about dictionaries.

#Challenge:

You are managing a digital recipe book where each recipe is stored as a dictionary. 
Each dictionary contains the name of the recipe as the key and a list of ingredients as the value. 
Your task is to perform several operations to update and manage the recipe book.
1. Create the Recipe Book:
    Create a dictionary named recipe_book with the following recipes:
        "Pancakes": ["flour", "milk", "eggs", "sugar"]
        "Salad": ["lettuce", "tomato", "cucumber", "olive oil"]
2. Access Ingredients:
    Print the list of ingredients for "Pancakes".
3. Add a New Recipe:
    Add a new recipe "Smoothie" with the ingredients ["banana", "milk", "honey"] to the dictionary.
4. Modify a Recipe:
    Add "blueberries" to the "Smoothie" recipe.
5. Print All Recipes:
    Print the entire recipe_book dictionary to verify the updates.

'''

# Step 1: Create the Recipe Book
recipe_book = {
    "Pancakes": ["flour", "milk", "eggs", "sugar"],
    "Salad": ["lettuce", "tomato", "cucumber", "olive oil"]
}

# Step 2: Access Ingredients
print(recipe_book["Pancakes"])

# Step 3: Add a New Recipe
recipe_book['Smoothie'] = ['banana', 'milk', 'honey']

# Step 4: Modify a Recipe
recipe_book['Smoothie'].append('blueberries')

# Step 5: Print All Recipes
print(recipe_book)

# Output the entire recipe book to verify updates
print("Updated Recipe Book:", recipe_book)

