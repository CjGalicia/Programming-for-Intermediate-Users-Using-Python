Flavors = {"vanilla", "chocolate", "strawberry", "cookies n' cream", "bubblegum"}
Toppings = {"almonds", "banana slices", "chocolate syrup", "caramel syrup", "white chocolate chips"}

ice_cream = dict(zip(Flavors, Toppings))

print (ice_cream)

ice_cream["chocolate"] = "blueberries"
ice_cream.update({"matcha": "pistachios", "ube": "mango slices"})
print (ice_cream)