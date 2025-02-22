
from cashier import Cashier

class SandwichMaker(Cashier):
    def __init__(self, resources):
        super().__init__()
        self.machine_resources = resources


    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        #####

        for ingredient, amount in ingredients.items():  # If not enough of any ingredient, print a message and stop
            if self.machine_resources[ingredient] < amount:
                print("Sorry, not enough resources.")
                return False

        return True  # Return True only if all ingredients are available

    def make_sandwich(self, sandwich_size, order_ingredients):
        ########

        # sandwich = recipes[sandwich_size]  # Get the recipe for the sandwich

        for ingredient, amount in order_ingredients.items():
            self.machine_resources[ingredient] -= amount  # Deduct used ingredients
            print("_________\n")
            print(f"Used {amount} {ingredient}. Remaining: {self.machine_resources[ingredient]}")

        print(f"Your {sandwich_size} sandwich is ready. Bon Appetit!\n")  # Confirmation message