import random
import os
import os.path

login = False

# checking if user exist
def check_login(login):
    
    username = input("Enter your username: ").lower()
    password = input("Enter your password: ").lower()
    staff = open('staff.txt', 'r')
    listofStaff = []
    dictionary = {}
    for line in staff:
        line = line.strip()
        if line == '':
            listofStaff.append(dictionary)
            dictionary = {}
        else:
            pair = line.split(' ')
            if len(pair) == 2:
                key, value = pair
                dictionary[key] = value
            else:
                key = pair[0]
                value = pair[1] + ' ' + pair[2]
                dictionary[key] = value
    listofStaff.append(dictionary)

    for staff in listofStaff:
        if username == staff['username'] and password == staff['password']:
            print('login successful')
            login = True
            #create a session
            session = open('session.txt', 'w')
            session.write(staff['full_name'])
            
    if login == False:
        print('Password or Username incorrect! Try again')
    return login

# Main logic that will trigger all functions
def logic(login):
    choice = input("What will you like to do? \nSelect an Option with the number assigned \n1. Create new bank account \n2. Check Account Details \n3. Logout \n>> ")
    # create a new account
    if choice == '1':
        account_name = input("Enter account name: ")
        opening_balance = input("Enter opening balance: ")
        account_type = input("Enter account type(Saving Or Current): ")
        account_email = input("Enter email to be used to open this account: ")
        account_number = ''
        for n in range(10):
            account_number += str(random.randint(0, 9))
        account_number = int(account_number)
        print(f'Your new account number is {account_number}')

        customer = open('customer.txt', 'a')
        customer.writelines(
f'''account_name {account_name}
opening_balance {opening_balance}
account_type {account_type}
account_email {account_email}
account_number {account_number}
''')
        customer.close()
    
    # checking  account details
    elif choice == '2':
        account_number = input('To check your account details, please enter your account number: ')
        customer = open('customer.txt', 'r')
        dictionary = {}
        for line in customer:
            line = line.strip()
            pair = line.split(' ')
            if len(pair) == 2:
                key, value = pair
                dictionary[key] = value
            else:
                key = pair[0]
                value = pair[1] + ' ' + pair[2]
                dictionary[key] = value
        if dictionary['account_number'] == account_number:
            print('Here are your account details:')
            print('')
            for key in dictionary:
                print(f'{key}: {dictionary[key]}')
        else:
            print('Sorry this account does not exist. Please try again.')
    
    # logout and delete session
    elif choice == '3':
        os.remove('session.txt')
        login = False
    return login

close_app = False

while close_app == False:
    message = ''
    try:
        session = open('session.txt', 'r')
    except IOError:
        message = 'Session file does not exist'
    else:
        session.close()

    if message != '':
        option = input('''
Select an option by the entering the number:
1. Staff Login
2. Close App
''')
    else:
        login = True
        option = '1'
    if option == '1':
        while login == False:
            login = check_login(login)

        while login == True:
            session = open('session.txt', 'r')
            name = session.read()
            session.close()
            print(f'Welcome {name}')
            login = logic(login)

    elif option == '2':
        close_app = True