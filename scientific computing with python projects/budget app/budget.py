class Category:

    def __init__(self, name):
        self.name = name
        self.total = 0
        self.ledger = []

    def __str__(self):
        stars = '*' * ((30 - len(self.name)) // 2)
        table = stars + self.name + stars + "\n"
        mid_space = 0
        for i in self.ledger:
            mid_space = " " * (30 - (len("{0:.2f}".format(i["amount"])) + len(i["description"][:23])))
            table = table + i["description"][:23] + mid_space + "{0:.2f}".format(i["amount"]) + "\n"
        table = table + "Total: {}".format(self.total)
        return table

    def deposit(self, amount, *description):
        if description:
            self.ledger.append({"amount": amount, "description": description[0]})
        else:
            self.ledger.append({"amount": amount, "description": ""})
        self.total = self.total + amount

    def withdraw(self, amount, *description):
        if self.check_funds(amount):
            if description:
                self.ledger.append({"amount": (-1 * amount), "description": description[0]})
            else:
                self.ledger.append({"amount": (-1 * amount), "description": ""})
            self.total = self.total - amount
            return True
        else:
            return False

    def transfer(self, amount, receiver):
        if self.check_funds(amount):
            sender_description = "Transfer to {}".format(receiver.name)
            receiver_description = "Transfer from {}".format(self.name)
            self.withdraw(amount, sender_description)
            receiver.deposit(amount, receiver_description)
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount > self.total:
            return False
        else:
            return True

    def get_balance(self):
        return self.total

def create_spend_chart(categories):
    all_chart = "Percentage spent by category\n"
    all_data = []
    chart_data = []
    total_spent = 0
    for category in categories:
        category_spent = 0
        for i in category.ledger:
            if i["amount"] < 0:
                category_spent = category_spent - i["amount"]
        total_spent = total_spent + category_spent
        all_data.append({"category_name": category.name, "category_spent": category_spent})

    for data in all_data:
        perc = int(((data["category_spent"] / total_spent) * 100) / 10) * 10
        chart_data.append({"category_name": data["category_name"], "category_perc": perc})

    for i in range(100, -1, -10):
        pre_space = " " * (3 - len(str(i)))
        perc_line = pre_space + str(i) + "|" + "          "
        for j in chart_data:
            if j["category_perc"] == i or j["category_perc"] > i:
                perc_line_list = list(perc_line)
                perc_line_list[5 + (3 * (chart_data.index(j)))] = "o"
                perc_line = "".join(perc_line_list)
        all_chart = all_chart + perc_line + "\n"
    all_chart = all_chart + "    ----------" + "\n"


    name_list = []
    for k in range(len(chart_data)):
        name_list.append(chart_data[k]["category_name"])

    max_len = max(len(x) for x in name_list)

    for i in range(max_len):
        new_line = "    "
        for name in name_list:
            if i < len(name):
                new_line = new_line + " " + name[i] + " "
            else:
                new_line = new_line + "   "
        new_line = new_line + " "
        if i < max_len - 1:
            all_chart = all_chart + new_line + "\n"
        else:
            all_chart = all_chart + new_line
    return all_chart
