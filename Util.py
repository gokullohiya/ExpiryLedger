from mysql import Sql


class Utility(Sql):
    def __init__(self):
        super().__init__()
        self.sql = Sql()

    def add(self):
        name = str(input("Enter item name:"))
        date = input("Enter date(YYYY-MM-DD):")
        manufacturing_date = list(map(int, date.split("-")))
#       my_date = datetime.strptime(manufacturing_date, "%Y-%m-%d")
        valid_months = int(input('Enter Valid Months:'))
        expiry_date = self.date_adder(manufacturing_date, valid_months)
#       six_months = manufacturing_date#+relativedelta(months=+6)
#       lst.append(six_months)
        self.sql.insert_command(name, date, valid_months,"-".join(str(x) for x in expiry_date))

    # sql.cursor.execute(command)

    def date_adder(self, date, months):
        date[0] += months//12
        date[1] += months%12
        return date


    def delete(self):
        self.sql.print_all()
        num = int(input("Which record you want to delete:"))
        self.sql.delete(num)
        print("Item has been deleted")


    def search(self):
        name = input("Item name:")
        self.sql.search(name)

    def expiry(self):
        self.sql.expiry()



