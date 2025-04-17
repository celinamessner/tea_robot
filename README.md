# README

## 📋 Overview
The Tea Making Robot is a Python-based simulation that models a robotic tea preparation system using Object-Oriented Programming (OOP) principles. It manages tea orders, heats water, dispenses tea, and tracks stock levels through modular components like the boiler, dispenser, and order queue.

## ⚙️ Features
Take Orders

Accepts user input for different tea types.

Validates availability and queues the order.

Process Orders

Heats water to tea-specific temperatures.

Dispenses the correct tea.

Updates tea stock.

Exit Program

Type exit to end the session.

## 🧠 System Components
### 🔧 Tea Configuration
```python
tea_temperatures = {
    "Mint": 90,
    "Green": 80,
    "Black": 95,
    "Chamomile": 93
}

tea_stock = {
    "Mint": 5,
    "Green": 2,
    "Black": 8,
    "Chamomile": 0
}
```

###💧 WaterBoiler Class
```python
class WaterBoiler:
    def __init__(self):
        self.temperature = 25  # Starting temperature

    def heat_to(self, target_temp):
        self.temperature = target_temp
        print(f"Heating water to {self.temperature}°...")
```

###🍵 TeaDispenser Class
```python
class TeaDispenser:
    def __init__(self):
        self.available = tea_stock

    def check_availability(self, tea_type):
        return self.available.get(tea_type, 0) > 0

    def dispense(self, tea_type):
        if self.check_availability(tea_type):
            print(f"Dispensing {tea_type} tea...")
            self.available[tea_type] -= 1
            print(f"Stock left: {self.available[tea_type]}")
        else:
            print(f"{tea_type} tea is not available!")
```

### 🧾 OrderQueue Class
``` python
class OrderQueue:
    def __init__(self):
        self.queue = []

    def add_order(self, order):
        print(f"New order received: {order}")
        self.queue.append(order)

    def get_next_order(self):
        return self.queue.pop(0) if self.queue else None

    def has_orders(self):
        return len(self.queue) > 0
```

### 🤖 Tea_Maker Class
```python
class Tea_Maker:
    def __init__(self, boiler, dispenser):
        self.boiler = boiler
        self.dispenser = dispenser

    def prepare_tea(self, tea_type):
        print(f"Preparing {tea_type} tea...")
        if not self.dispenser.check_availability(tea_type):
            print("Error: Tea not available!")
            return False

        desired_temp = tea_temperatures[tea_type]
        print(f"Heating water to the right temperature for {tea_type}...")
        self.boiler.heat_to(desired_temp)

        self.dispenser.dispense(tea_type)
        print(f"Tea prepared successfully at {desired_temp}°C!")
        return True
```

### 🧠 Robot Class (Controller)
``` python
class Robot:
    def __init__(self):
        self.queue = OrderQueue()
        self.boiler = WaterBoiler()
        self.dispenser = TeaDispenser()
        self.tea_maker = Tea_Maker(self.boiler, self.dispenser)

    def take_order(self, tea_type):
        if tea_type in tea_temperatures:
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
            print("Ready for the next order!")
```

### 🖥️ main() Function
```python
def main():
    robot = Robot()
    print("Welcome to the Tea Making Robot!")
    print("Type in your tea order (e.g. 'Green', 'Black').")
    print("Type 'exit' to stop ordering.")

    while True:
        tea_order = input("Enter your tea order: ").strip()
        if tea_order.lower() == "exit":
            print("Exiting the Tea Making robot.")
            break
        else:
            robot.take_order(tea_order)
        robot.process_orders()
```

## ✅ Testing
Test cases performed:

Order Black Tea – Should heat water and dispense.

Order Black Tea Again – Stock reduced accordingly.

Order Chamomile Tea – Out of stock; error message shown.

### ✅ Expected Results
All orders processed as expected.

Tea out of stock triggers correct error handling.

## 📚 References
Klump, R. (2001). Understanding object-oriented programming concepts. IEEE Power Engineering Society Summer Meeting.

