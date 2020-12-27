from dataclasses import dataclass
from functools import reduce


def parse_input_file():
    with open("day21_data.txt", "r") as file:
        return file.readlines()


@dataclass
class Recipe:
    ingredients: list
    allergens: list


def get_allergic_ingredients(allergen, recipes):
    ingredients = [i.ingredients for i in recipes if allergen in i.allergens]
    return list(reduce(set.intersection, [set(item) for item in ingredients ]))


def part_1():
    input = parse_input_file()
    safe_ingredients = set()
    all_ingredients = []
    allergens = set()
    recipes = []
    for line in input:
        contents = line.split('(')
        ingredients = contents[0].split()
        safe_ingredients.update(ingredients)
        all_ingredients.extend(ingredients)
        curr_allergens = contents[1].replace(')', '').replace(',', '').split()[1:]
        allergens.update(curr_allergens)
        recipe = Recipe(ingredients, curr_allergens)
        recipes.append(recipe)
    for allergen in allergens:
        allergic_ingr = get_allergic_ingredients(allergen, recipes)
        safe_ingredients.difference_update(allergic_ingr)
    count = 0
    for ingr in all_ingredients:
        if ingr in safe_ingredients:
            count += 1
    print(count)


def part_2():
    input = parse_input_file()
    allergens = set()
    potential_allergic_ingredients = {}
    recipes = []
    for line in input:
        contents = line.split('(')
        ingredients = contents[0].split()
        curr_allergens = contents[1].replace(')', '').replace(',', '').split()[1:]
        allergens.update(curr_allergens)
        recipe = Recipe(ingredients, curr_allergens)
        recipes.append(recipe)
    for allergen in allergens:
        potential_allergic_ingredients[allergen] = get_allergic_ingredients(allergen, recipes)
    while sum([len(v) for v in potential_allergic_ingredients.values()]) > len(potential_allergic_ingredients):
        for key, val in potential_allergic_ingredients.items():
            if len(val) == 1:
                for k, v in potential_allergic_ingredients.items():
                    if not v == val and val[0] in v:
                        v.remove(val[0])
    potential_allergic_ingredients_sorted = dict(sorted(potential_allergic_ingredients.items()))
    canonical_dangerous_ingredient_list = ','.join(str(x[0]) for x in potential_allergic_ingredients_sorted.values())
    print(canonical_dangerous_ingredient_list)


part_1()
part_2()
