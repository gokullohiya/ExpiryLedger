import sqlite3

from Util import Utility


class Main(Utility):
    userName = 'admin'
    password = 'admin'

    def __init__(self):
        super().__init__()
        self.ut = Utility()
#       self.sq = Sql()

    def options(self):
        while True:
            choice = int(input("1.Add\n2.Delete\n3.Search\n4.Expiring Items\n5.Exit"))
            if choice == 1:
                self.ut.add()
            elif choice == 2:
                self.ut.delete()
            elif choice == 3:
                self.ut.search()
            elif choice == 4:
                self.ut.expiry()
            else:
                break


if __name__ == "__main__":
    connection = sqlite3.connect("product_information.db")
    cursor = connection.cursor()
    print("Welcome")
    userName = input("Please Enter Username:")
    password = input("Enter Password:")
    while userName != Main.userName and password != Main.password:
        userName = input("Please Enter Username:")
        password = input("Enter Password:")
        print("Enter correct details")

    admin = Main()
    admin.options()
