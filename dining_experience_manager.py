class DiningExperienceManager:
    def __init__(self):
        self.menu = {
            'Chinese Food': 8,
            'Italian Food': 10,
            'Pastries': 5,
            'Chef\'s Specials': 12
        }

    def display_menu(self):
        print("Menu:")
        for item, price in self.menu.items():
            print(f"{item}: ${price}")

    def get_order(self):
        order = {}
        for item in self.menu:
            quantity = self.get_valid_quantity(item)
            if quantity > 0:
                order[item] = quantity
        return order

    def get_valid_quantity(self, item):
        while True:
            try:
                quantity = int(input(f"Enter the quantity of {item} (0 to skip): "))
                if quantity < 0:
                    print("Please enter a positive integer or 0 to skip.")
                elif quantity > 100:
                    print("Maximum order quantity is 100.")
                else:
                    return quantity
            except ValueError:
                print("Invalid input. Please enter a valid quantity.")

    def calculate_total_cost(self, order):
        base_cost = 5
        total_cost = 0

        for item, quantity in order.items():
            total_cost += self.menu[item] * quantity

        if total_cost > 50:
            total_cost -= 10
        if total_cost > 100:
            total_cost -= 25

        total_quantity = sum(order.values())
        if total_quantity > 5:
            total_cost *= 0.9
        if total_quantity > 10:
            total_cost *= 0.8

        if any(item in self.menu for item in order if "Chef's Specials" in item):
            total_cost *= 1.05

        return total_cost

    def run(self):
        self.display_menu()
        order = self.get_order()

        if not order:
            print("No meals selected. Order canceled.")
            return -1

        total_cost = self.calculate_total_cost(order)

        print("\nOrder Summary:")
        for item, quantity in order.items():
            print(f"{item} x {quantity}")
        print(f"Total Cost: ${total_cost}")

        return total_cost


if __name__ == "__main__":
    manager = DiningExperienceManager()
    total_cost = manager.run()
    if total_cost != -1:
        print("Order confirmed. Enjoy your meal!")