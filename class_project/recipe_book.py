# # Recipe Book program using Dictionary
print("   CAFE   ")
recipe={}
n=int(input("enter number of recipe: "))
for i in range(n):
    dish = input("name of dishes: ")
    ingredients= input("enter ingredients(comma-separated): ")
    list=[item.strip() for item in ingredients.split(",")]
    recipe[dish]=list
name_dish=input("\n name of recipe:")
if name_dish in recipe:
    print("Ingredients:", ", ".join(recipe[name_dish]))
else:
    print("not found this recipe")
print("\nRecipe Book:")
for dish, ingredients in recipe.items():
    print(f"{dish} : {', '.join(ingredients)}")


