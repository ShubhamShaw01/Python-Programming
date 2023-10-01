#wap to implement bank account 
class Balance:
    def __init__(self, name, bal):
        self.name = name
        self.bal = bal

    def show_message(self):
        if self.bal > 0:
            print(self.name, self.bal)


def main():
    size = int(input("Enter the number of persons: "))
    arr = []
    for i in range(size):
        name = input(f"Enter the name of person {i + 1}: ")
        balance = float(input(f"Enter the balance of person {i + 1}: "))
        arr.append(Balance(name, balance))

    for balance_obj in arr:
        balance_obj.show_message()


if __name__ == "__main__":
    main()
