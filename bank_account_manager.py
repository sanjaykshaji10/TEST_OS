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
    create_account(account)

# now define separate functions for deposit, withdraw and display balance
def deposit_in(c_name, acc_no, acc_type, amount):
    # get the values
    print()


def withdraw_out(c_name, acc_no, acc_type, amount):
    print()


def display_bal(acc_no):
    print()



