#banking system program

#The error_response is used to give user feedback
#especially when an invalid value is entered
def error_response(error_message):
    print(error_message)

#The file reader function, reads textfile and converts them for use in the program
def filereader():
    global d
    # d is the dictionary that holds the staff predefined details
    d = {}
    with open('staff.txt', 'r') as file:
        for line in file:
            (key, val) = line.split()
            d[str(key)] =  val
            
# This function collects details from the filereader function and verifies it.
def staff_id_confirmation(user_login_name, user_login_password):
    if (user_login_name == d['username1'] and user_login_password == d['password1']) or\
       (user_login_name == d['username2'] and user_login_password == d['password2']):
        print('Login successful')
    else:
        print('Login not successful, try again')
        
# This customer_acct number function generates an account number for the
#customer, after successful registration and returns the account number
#of the customer  
def customer_account_number_creator():
    global account_number
    account_number ='0'
    from random import randint
    for i in range(9):
        digits = randint(0, 9)
        account_number += str(digits)
    return account_number

#This function writes new customer account details to the customer
#file
def customer_account_file():
    customer_details = open('customer.txt', 'w')
    customer_details.write(f'''Account Name: {account_name}
Opening Balance: {opening_balance}
Account Type: {account_type}
Account E_mail: {account_email}
Account Number: {account_number}''')
    customer_details.close()
    
# creates a user session file    
def user_session_file():
    global user_session
    user_session = open('user_session.txt', 'w')
    user_session.write(f'''username: {username}
password: {password}''')
    user_session.close()

#The account checker function takes the account number of the customer,
#validates the input account number, and prints the details
def customer_details_checker():
    acct_number = input('Enter account number:\n')
    customer_details = open('customer.txt', 'r')
    customer = customer_details.read()
    if acct_number in customer:
        print(customer)
    else:
        print('please enter correct acct details')

# The file_delete function deletes temporary user_session files
def file_delete(user_session_file):
    import os
    os.remove(user_session_file)

error_message1 = 'Invalid response, respond with 1, or 2'
error_message2 = 'Invalid response, respond with 1, 2, or 3'      
while True:
    try:
        staff_login = eval(input('1 Staff Login \n2 Close App\n'))
    except NameError:
        error_response(error_message1)
        continue
    except SyntaxError:
        error_response(error_message1)
        continue
    if staff_login == 1:
        username = input('Username: ')
        password = input('password: ')
        filereader()
        staff_id_confirmation(username, password)
        user_session_file()
        while True:
            try:
                 customer_action = eval(input('1 Create New Bank Account \n2 Check Account Details \n3 Logout\n'))
            except NameError:
                error_response(error_message2)
                continue
            except SyntaxError:
                error_response(error_message2)
                continue
            if customer_action == 1:
                account_name = input('Account Name:\n')
                opening_balance = eval(input('Opening Balance(NGN):\n'))
                account_type = input('Account Type(savings, current, Fixed Deposit):\n')
                account_email = input('E_mail address:\n')
                print('Your account number is:',customer_account_number_creator())
                customer_account_file()
            elif customer_action == 2:
                customer_details_checker()
            elif customer_action == 3:
                file_delete(user_session)
                break
            else:
                print('Invalid response, please respond with 1 , 2, 3')
    elif staff_login == 2:
        break
    else:
        error_response(error_message1)
        continue
        
                
            
