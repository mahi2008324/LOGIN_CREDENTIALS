class Login_credentials:
    def __init__(self):
        self.user = 'venky'
        self.password = '1234'                             # store password as string for comparison

    def login(self):                                       #login page
        print("\n----- LOGIN PAGE -----\n")
        user = input("ENTER THE USERNAME: ")               #taking user name from enduser
        if user == self.user:                              #checks username exists
            pas = input("ENTER THE PASSWORD: ")            #taking password from enduser
            if pas == self.password:                       #checks password correct
                print("YOU ARE LOGGED IN")
            else:                                          #if password is incorrect
                print("YOUR PASSWORD IS INCORRECT")
        else:                                              #if user name not exists
            print("USER NOT FOUND. REDIRECTING TO SIGN UP...")
            self.sign_up()                                 #takes to sign up page

    def sign_up(self):                                     #sign up page
        print("\n----- SIGN UP PAGE------\n")
        new_user = input("CREATE USERNAME           : ")              #create the new user
        if new_user == self.user:                          #if user already exists
            print("USERNAME ALREADY EXISTS. TRY LOGGING IN.")
            self.login()                                   #if user exists takes to login page
            return

        email = input("PLEASE ENTER THE EMAIL ID : ")         #email enetring
        if email.endswith("@gmail.com"):                      #checks email ends with @gmail.com
            pass
        else:                                                  #if not  takes to re-signup
            print("GIVE VALID EMAIL")
            self.sign_up()
            return
        phone_no = input("ENTER YOUR PHONE NUMBER   : ")      #phone number entering
        if len(phone_no) != 10 or not phone_no.isdigit():  #checking the phone is in digits and in lenght of 10
            print("INVALID PHONE NUMBER. PLEASE ENTER A 10-DIGIT NUMBER.")
            self.sign_up()
            return

        password = input("CREATE PASSWORD           : ")              #creating the password
        confirm_password = input("REENTER THE PASSWORD      : ") #conforming the password
        if password != confirm_password:                   #checking the password is matches with conforming password
            print("PASSWORDS DO NOT MATCH. TRY AGAIN.")
            self.sign_up()
            return
        # Save the new user
        self.user = new_user                              #updating the new user
        self.password = password                          #updating the new user ka password

        print("SIGNUP SUCCESSFUL. PLEASE LOGIN NOW.")
        self.login()                                     #takes to login page            

# Run the program
l = Login_credentials()                                  #object creation for class
l.login()                                                #calling the method