import sqlite3 as sql


from Constants import *
# define connection and cursor
# import Util


class Sql:

    def __init__(self):
        connection = sql.connect("product_information.db")
        self.cursor = connection.cursor()
        self.create_table()
        self.counter = 0

# create table
    def create_table(self):
        command1 = f"""CREATE TABLE IF NOT EXISTS 
    {TABLE_NAME}({ITEM_ID} INTEGER AUTO_INCREMENT,{NAME} TEXT,{manufacturing} DATE, "{VALIDITY}" INTEGER, "{expiry}" DATE, PRIMARY KEY ({ITEM_ID}))"""

        self.cursor.execute(command1)

    def insert_command(self, name, date, validity, expiry_date):
        self.counter += 1
        command = f"""INSERT INTO {TABLE_NAME} VALUES({self.counter},"{name}","{date}",{validity}," {expiry_date}")"""
        self.cursor.execute(command)
        self.print_all()

    def expiry(self):
        command3 = "SELECT * FROM products ORDER BY ExpiryDate"
        self.cursor.execute(command3)
        self.print_to_screen()

    def delete(self, key):
        command = f""" DELETE FROM {TABLE_NAME} WHERE item_id = {key}"""
        self.cursor.execute(command)
        self.print_all()

    def search(self, name):
        command = f"""SELECT * FROM {TABLE_NAME} WHERE {NAME} = "{name}" """
        self.cursor.execute(command)
        self.print_to_screen()

    def print_to_screen(self):
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)

    def print_all(self):
        command = f"""SELECT * FROM {TABLE_NAME}"""
        self.cursor.execute(command)
        results = self.cursor.fetchall()
        print(results)
