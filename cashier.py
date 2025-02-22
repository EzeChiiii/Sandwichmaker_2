class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        ###
        while True:

            try:
                amount_nickel = int(input("How many nickels?: "))*0.05
                amount_dime = int(input("How many dimes?: "))*0.10
                amount_dollars = int(input("How many dollars?: "))*1.00
                amount_quarters = int(input("How many quarters?: "))*0.25
                total = amount_nickel + amount_dime + amount_dollars + amount_quarters
                return total # Return the total amount inserted


            except ValueError:
                print("Invalid input. Please enter a number.")  # Handles invalid inputs

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        ##
        if coins >= cost:
            change = round(coins - cost, 2)  # Calculate change and rounds to 2 decimal places over
            if change > 0:
                print(f"Here is your change: ${change:.2f}")
            return True  # returns true if payment is successful

        else:
            print("Sorry, that's not enough money. Money refunded.")
            return False  # failed payment