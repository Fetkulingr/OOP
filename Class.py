'''
This module make

Athor: Fetkulin Grigory, Fetkulin.G.R@yandex.ru
'''


class User:
    """AI is creating summary for
    """
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.hdd = None
        self.hdd_type = None

    def get_user_input(self):
        """AI is creating summary for get_user_input
        """
        # Define the available processor models
        cpu_options = {
            1: "Intel Core i5",
            2: "Intel Core i7",
            3: "AMD Ryzen 5",
            4: "AMD Ryzen 7"
        }
        print("Available processor models:")
        for option, model in cpu_options.items():
            print(f"{option}: {model}")
        cpu_choice = int(input("Select the processor model (enter a number): "))
        self.cpu = cpu_options.get(cpu_choice)

        while True:
            # Prompt the user to enter the amount of RAM
            ram_input = input("Enter the amount of RAM (in GB): ")
            if ram_input.isdigit():
                self.ram = int(ram_input)
                break
            else:
                print("Mistake! Enter a number.")

        # Define the available hard drive types
        hdd_options = {
            1: "SSD",
            2: "HD"
        }
        print("Available Hard Drive types:")
        for option, hdd_type in hdd_options.items():
            print(f"{option}: {hdd_type}")
        hdd_choice = int(input("Select the type of hard drive (enter a number): "))
        self.hdd_type = hdd_options.get(hdd_choice)

        while True:
            # Prompt the user to enter the hard disk size
            hdd_input = input("Enter the hard disk size (in GB): ")
            if hdd_input.isdigit():
                self.hdd = int(hdd_input)
                break
            else:
                print("Mistake! Enter a number.")

    def is_input_correct(self):
        """AI is creating summary for is_input_correct

        Returns:
            [type]: [description]
        """
        # Validate user input (if needed)
        return True

    def run(self):
        """AI is creating summary for run
        """
        self.get_user_input()
        if self.is_input_correct():
            print("Characteristics of your computer:")
            print(f"Processor Model: {self.cpu}")
            print(f"Random access memory: {self.ram} GB")
            print(f"Hard drive: {self.hdd} GB, {self.hdd_type}")


user = User()
user.run()
