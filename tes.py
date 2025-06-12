class LoginSystem:
    def __init__(self):
        self.username = 'venky'
        self.password = '1234'

    def login(self):
        print("\n----- LOGIN PAGE -----\n")
        entered_username = input("ENTER THE USERNAME: ")

        if entered_username == self.username:
            entered_password = input("ENTER THE PASSWORD: ")
            if entered_password == self.password:
                print("YOU ARE LOGGED IN SUCCESSFULLY.")
            else:
                print("INCORRECT PASSWORD. TRY AGAIN.")
        else:
            print(" USER NOT FOUND. PLEASE SIGN UP.")
            self.sign_up()

    def sign_up(self):
        print("\n----- SIGN UP PAGE -----\n")

        while True:
            new_username = input("CREATE USERNAME: ")
            if new_username == self.username:
                print(" USERNAME ALREADY EXISTS. TRY LOGGING IN.")
                self.login()
                return
            break

        while True:
            email = input("ENTER YOUR EMAIL: ")
            if not email.endswith("@gmail.com"):
                print(" INVALID EMAIL. IT MUST END WITH @gmail.com")
            else:
                break

        while True:
            phone = input("ENTER YOUR PHONE NUMBER: ")
            if len(phone) == 10 and phone.isdigit():
                break
            else:
                print(" INVALID PHONE NUMBER. ENTER A 10-DIGIT NUMBER.")

        while True:
            pwd = input("CREATE PASSWORD: ")
            confirm_pwd = input("CONFIRM PASSWORD: ")
            if pwd == confirm_pwd:
                break
            else:
                print(" PASSWORDS DO NOT MATCH. TRY AGAIN.")

        # Store new user
        self.username = new_username
        self.password = pwd

        print(" SIGNUP SUCCESSFUL! PLEASE LOGIN TO CONTINUE.\n")
        self.login()


# Run the system
app = LoginSystem()
app.login()
