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
    def __init__(self, c_name, account_number, account_type, balance_amount):
        self.c_name = c_name
        self.account_number = account_number
        self.account_type = account_type
        self.balance_amount = balance_amount
        # basically create an account
        # then store it into a data base


def create_account_table():
    conn = psycopg2.connect("dbname='accounts' user='postgres' password='cyant695' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS account_holder (Username TEXT, Account_No INTEGER, Account_Type TEXT, Balance REAL)")
    conn.commit()
    conn.close()


def create_account(account):
    print()
    # here the argument account is an object of the class
    # basically an insert function
    # an account has name, ac_no, ac_type(savings / credits), balance
    conn = psycopg2.connect("dbname='accounts' user='postgres' password='cyant695' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("INSERT INTO account_holder VALUES(%s,%s,%s,%s)", (account.c_name, account.account_number, account.account_type, account.balance_amount))
    conn.commit()
    conn.close()
    # created an account


def add_account_to_db(account):
    # adding the account to the database
    # here this will be a process
    # process 1
    create_account(account)

# now define separate functions for deposit, withdraw and display balance
def deposit_in(c_name, acc_no, acc_type, amount):
    # get the values
    # retrieve the table, update the values
    # add the amount to the balance
    # and all of it should be another process
    # process 2
    print()


def withdraw_out(c_name, acc_no, acc_type, amount):
    # get the values
    # retrieve the table, update the values
    # subtract the amount from the balance
    # if and only if previous_balance >= amount_to_be_withdrawn
    # process 3
    print()


def display_bal(acc_no):
    # retrieve the table
    # show the consumer_name and balance
    # process 4
    print()


# main function
# this is the parent process
# it works when
if __name__ == '__main__':

    processes = []
    create_account_table()
    print('table created')
    enquiry = 'y'
    while enquiry == 'y' or enquiry == 'Y':
        print('\nbank_account_manager')
        print('1. Create new account\n2. Deposit into account\n3. Withdraw from account\n4. Show balance')
        choice = int(input('Enter your choice'))
        if choice == 1:
            print()
        elif choice == 2:
            print()
        elif choice == 3:
            print()
        elif choice == 4:
            print()
        else:
            print('Enter a valid choice...')
        enquiry = input('Enquire Again? (y/n) ')
    print('Thanks for using our service :)')
