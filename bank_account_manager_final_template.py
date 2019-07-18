import os
from multiprocessing import Process, current_process
import psycopg2
# for using postgresql database


# Data members:
# 1) Name of the depositor
# 2) Account number
# 3) Type of account
# 4) Balance amount in the account.
#
# Member functions:
# 1) To assign initial values
# 2) To deposit an amount
# 3) To withdraw an amount after checking the balance
# 4) To display name and balance.

# just for making some objects
class BankAccount:
    # initialization function
    def __init__(self, c_name, account_type, balance_amount):
        self.c_name = c_name
        #self.account_number = account_number
        self.account_type = account_type
        self.balance_amount = balance_amount
        # basically create an account
        # then store it into a data base


def create_account_table():
    conn = psycopg2.connect("dbname='accounts' user='postgres' password='cyant695' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS account_holder (Account_No SERIAL PRIMARY KEY, Username TEXT, Account_Type TEXT, Balance REAL)")
    conn.commit()
    conn.close()
    # the account number is the primary key for all the manipulation functions


def create_account(account):
    print("\nprocess name:", current_process().name)
    # here the argument account is an object of the class
    # basically an insert function
    # an account has name, ac_no, ac_type(savings / credits), balance
    # the balance is right now initiailzed to 0.00
    conn = psycopg2.connect("dbname='accounts' user='postgres' password='cyant695' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("INSERT INTO account_holder VALUES(DEFAULT,%s,%s,%s)", (account.c_name, account.account_type, account.balance_amount))
    conn.commit()
    conn.close()
    # created an account


def add_account_to_db(account):
    # adding the account to the database
    # here this will be a process
    # process 1
    create_account(account)

# now define separate functions for deposit, withdraw and display balance
def deposit_in(acc_no, acc_type, amount):
    # get the values
    # retrieve the table, update the values
    # add the amount to the balance
    # and all of it should be another process
    # process 2
    print("\nprocess name:", current_process().name)
    # enter the acc_no, acc_type and amount
    # only acc_no and acc_type are required
    conn = psycopg2.connect("dbname='accounts' user='postgres' password='cyant695' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT Balance FROM account_holder WHERE Account_No=%s AND Account_Type=%s", (acc_no, acc_type))
    return_balance = cur.fetchall()
    # it should be a single valued tuple
    return_balance = float(list(return_balance[0])[0])
    new_balance = return_balance + amount
    cur.execute("UPDATE account_holder SET Balance=%s WHERE Account_No=%s AND Account_Type=%s", (new_balance, acc_no, acc_type))
    conn.commit()
    conn.close()





def withdraw_out(acc_no, acc_type, amount):
    # get the values
    # retrieve the table, update the values
    # subtract the amount from the balance
    # if and only if previous_balance >= amount_to_be_withdrawn
    # process 3
    print("\nprocess name:", current_process().name)
    # enter the acc_no, acc_type and amount
    # only the acc_no and acc_type are required
    conn = psycopg2.connect("dbname='accounts' user='postgres' password='cyant695' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT Balance FROM account_holder WHERE Account_No=%s AND Account_Type=%s", (acc_no, acc_type))
    return_balance = cur.fetchall()
    # it should be a single valued tuple
    return_balance = float(list(return_balance[0])[0])
    if return_balance >= amount:
        new_balance = return_balance - amount
        cur.execute("UPDATE account_holder SET Balance=%s WHERE Account_No=%s and Account_Type=%s", (new_balance, acc_no, acc_type))
        conn.commit()
        conn.close()
    else:
        print('Insufficient balance in your account...:(')




def display_bal(acc_no):
    # retrieve the table
    # show the consumer_name and balance
    # process 4
    print("\nprocess name:", current_process().name)
    # display the costumer name and the balance
    conn = psycopg2.connect("dbname='accounts' user='postgres' password='cyant695' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT Username, Balance FROM account_holder WHERE Account_No=%s", (acc_no,))
    user_and_balance = cur.fetchall()
    user_and_balance = list(user_and_balance)
    user_name = user_and_balance[0][0]
    balance = user_and_balance[0][1]
    balance = float(balance)
    print('Hello, ', user_name)
    print('Your balance is ', balance)
    conn.close()


# main function
# this is the parent process
# it works when
if __name__ == '__main__':

    processes = []
    create_account_table()
    # ac_num = 1
    print('table created')
    enquiry = 'y'
    while enquiry == 'y' or enquiry == 'Y':
        print('\nbank_account_manager')
        print('1. Create new account\n2. Deposit into account\n3. Withdraw from account\n4. Show balance')
        choice = int(input('Enter your choice'))
        if choice == 1:
            print()
            # create account
            # create account_process
            username = input('Enter username: ')
            init_balance = 0.0
            # let the initial balance be taken as zero
            account_type = input('Enter account type (sb - savings, cur - current):')
            # account_number = ac_num
            # ac_num += 1
            # now create a BankAccount Object
            new_account = BankAccount(username, account_type, init_balance)
            # create a new process
            account_process = Process(target=create_account, args=(new_account,))
            account_process.start()

        elif choice == 2:
            print()
            # deposit into the account
            account_num = int(input('enter the account number: '))
            account_type = input('enter the account type')
            insert_amount = round(float(input('enter the amount to be deposited: ')), 2)
            deposit_process = Process(target=deposit_in, args=(account_num, account_type, insert_amount))
            deposit_process.start()

        elif choice == 3:
            print()
            # withdraw from account
            account_num = int(input('enter the account number: '))
            account_type = input('enter the account type')
            withdraw_amount = round(float(input('enter amount to be withdrawn: ')), 2)
            withdraw_process = Process(target=withdraw_out, args=(account_num, account_type, withdraw_amount))
            withdraw_process.start()

        elif choice == 4:
            print()
            # display the balance
            account_num = int(input('enter the account number '))
            display_process = Process(target=display_bal, args=(account_num,))
            display_process.start()

        else:
            print('Enter a valid choice...')

        enquiry = input('Enquire Again? (y/n) ')

    print('Thanks for using our service :)')
    
 # done
