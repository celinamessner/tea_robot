# Tea Stock (tea stock and temperature settings)

# Ideal temperatures for each type of tea
tea_temperatures = {
    "Mint": 90,
    "Green": 80,
    "Black": 95,
    "Chamomile": 93
}

# Stock for each type of tea
tea_stock = {
    "Mint": 5,
    "Green": 2,
    "Black": 8,
    "Chamomile": 0
}

class WaterBoiler:
    def __init__(self):
        self.temperature = 25       # starting temp

    def heat_to(self, target_temp):
        self.temperature = target_temp
        print(f"Heating water to {self.temperature}°...")

# Tea dispenser
class TeaDispenser:
    def __init__(self):
        self.available = tea_stock        # start with initial stock

    def check_availability(self, tea_type):     # check if the tea is available
        return self.available.get(tea_type, 0) > 0

    def dispense(self, tea_type):       # dispense the tea and update the stoc
        if self.check_availability(tea_type):
            print(f"Dispensing {tea_type} tea...")
            self.available[tea_type] -= 1
            print(f"Stock left: {self.available[tea_type]}")
        else:
            print(f"{tea_type} tea is not available!")

# Order queue (FIFO)
class OrderQueue:
    def __init__(self):
        self.queue = []

    def add_order(self, order):
        print(f"New order received: {order}")
        self.queue.append(order)

    def get_next_order(self):
        if self.queue:
            return self.queue.pop(0)        # FIFO: Remove and return the first item in the list
        return None

    def has_orders(self):
        return len(self.queue) > 0

# Tea maker (combines boiler and dispenser)
class Tea_Maker:
    def __init__(self, boiler, dispenser):
        self.boiler = boiler
        self.dispenser = dispenser

    def prepare_tea(self, tea_type):
        print(f"Preparing {tea_type} tea...")
        if not self.dispenser.check_availability(tea_type):
            print("Error: Tea not available!")
            return False

        # Get the temperature for the respective tea
        desired_temp = tea_temperatures[tea_type]

        # Set the water temperature based on the tea type
        print(f"Heating water to the right temperature for {tea_type}...")
        self.boiler.heat_to(desired_temp)
        
        self.dispenser.dispense(tea_type)
        print(f"Tea prepared successfully at {desired_temp}°C!")
        return True


# Robot controller
class Robot:
    def __init__(self):
        self.queue = OrderQueue()
        self.boiler = WaterBoiler()
        self.dispenser = TeaDispenser()
        self.tea_maker = Tea_Maker(self.boiler, self.dispenser)

    def take_order(self, tea_type):
        if tea_type in tea_temperatures:  # Only allow available teas
            self.queue.add_order(tea_type)
        else:
            print("Sorry, we don't have that tea.")

    def process_orders(self):
        while self.queue.has_orders():
            next_order = self.queue.get_next_order()
            print(f"\nProcessing order: {next_order}")
            success = self.tea_maker.prepare_tea(next_order)
            if not success:
                print("Order failed.\n")
            else:
                print("Order complete.\n")

            # After an order is processed, prompt for new orders
            print("Ready for the next order!")

# Tea Making Flow
def main():
    robot = Robot()

    print("Welcome to the Tea Making Robot!")
    print("Type in your tea order (e.g. 'Green', 'Black').")
    print("Type 'exit' to stop ordering.")

    # Loop the program to allow continuous orders
    while True:
        # Get user input for the tea order
        tea_order = input("Enter your tea order: ").strip()

        if tea_order.lower() == "exit":
            print("Exiting the Tea Making robot.")
            break
        else:
            robot.take_order(tea_order)

        # Process the orders
        robot.process_orders()

# Run the tea robot
main()