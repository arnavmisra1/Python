class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name #created a class of person where first and last name attributes stored.

class Client(Person):

    def __init__(self, first_name, last_name, account_number, balance = 0):
        super().__init__(first_name, last_name) #super holds all attributes of parent class.
        self.account_number = account_number
        self.balance = balance #created two new attributes in child class client.

    def __str__(self):
        return f'Client: {self.first_name} {self.last_name}\nAccount Balance {self.account_number} : ${self.balance}'
    #used str function from polymorphism to print the information using literal strings.


    def deposit(self, amount_deposit):
        self.balance += amount_deposit
        print("Deposit Successful") #method for deposit created.

    def withdraw(self, amount_withdraw):

        if self.balance >= amount_withdraw:
            self.balance -= amount_withdraw
            print("Withdraw Successful")
        else:
            print("You have insufficient funds in your account") #method for withdraw created with valid if else case.

def create_client():
    first_name_ct = input("Enter your first name: ")
    last_name_ct = input("Enter your last name: ")
    account_number = input("Enter your account number: ")
    client1 = Client(first_name_ct, last_name_ct, account_number) #instance called and stored.

    return client1 #stores information of bank account by providing valid inputs


def start():
    my_customer = create_client()
    print(my_customer)
    option = 0
    print("Welcome to PBS Bank\n")
    print("Choose an option")

    while option != 'E':
        print("Deposit(D), Withdrawal(W) or Exit(E)")
        option = input()

        if option == 'D':
            dep_amount = int(input("Enter your deposit amount: "))
            my_customer.deposit(dep_amount)

        elif option == 'W':
            with_amount = int(input("Enter your withdrawal amount: "))
            my_customer.withdraw(with_amount)

        print(my_customer)

    print("Thank you for choosing Python Bank of Services. We hope you had a good experience.")

start()
 #created start method for the functioning of bank.














