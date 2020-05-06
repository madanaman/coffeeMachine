menu = {"pizza": "Margarita, Four Seasons, Neapoletana, Vegetarian, Spicy",
        "salad": "Caesar salad, Green salad, Tuna salad, Fruit salad",
        "soup": "Chicken soup, Ramen, Tomato soup, Mushroom cream soup"}
a = input()
if a in menu:
    print(menu[a])
else:
    print("Sorry, we don't have it in the menu")