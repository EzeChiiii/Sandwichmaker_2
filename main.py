import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
# cashier_instance = Cashier()




def main():
    ###  write the rest of the codes ###

    while True:

        user_input = input("What would you like? (small/ medium/ large/ off/ report: ").lower()

        if user_input == "off":
            print("Turning off the machine.")
            break  # Exit the while loop, ending the program

        elif user_input in "report":

            # print("Current Resources Avaiable:", sandwich_machine.machine_resources)
            for ingredient, amount in sandwich_maker_instance.machine_resources.items():
                print(f"{ingredient.capitalize()}: {amount}")


        elif user_input in ["small", "medium", "large"]:

            order_ingredients = recipes[user_input]["ingredients"]  # Get required ingredients
            order_cost = recipes[user_input]["cost"]  # Get sandwich price

            # Check if there are enough ingredients for the order
            if not sandwich_maker_instance.check_resources(order_ingredients):
                continue  # Stop the process if not enough ingredients

            print(f"Resources are available for order {user_input}")

            inserted_money = sandwich_maker_instance.process_coins()
            print(f"You inserted {inserted_money:.2f}")

            if sandwich_maker_instance.transaction_result(inserted_money, order_cost):
                # Step 4: Make the sandwich and update resources
                sandwich_maker_instance.make_sandwich(user_input, order_ingredients)  # Make the sandwich
            else:
                print("Insufficient funds. Returning coins.")  # Refund if not enough money

        else:
            print("Invalid input. Enter a correct option.")


if __name__=="__main__":
    main()
