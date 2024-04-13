class Category:
  def __init__(self, name):
    self.name = name
    self.ledger = []

  def deposit(self, amount, description=""):
    self.ledger.append({"amount": abs(amount), "description": description})

  def withdraw(self, amount, description=""):
    amount = abs(amount)

    self.ledger.append({"amount": -amount, "description": description})

    if not self.check_funds(amount):
      return False

    return True

  def get_balance(self):
    return sum([transaction["amount"] for transaction in self.ledger])

  def transfer(self, amount, category):
    amount = abs(amount)

    if not self.check_funds(amount):
      return False

    self.ledger.append({"amount": -amount, "description": f"Transfer to {category.name}"})
    category.deposit(amount, f"Transfer from {self.name}")

    return True

  def check_funds(self, amount):
    return amount <= self.get_balance()

  def __str__(self):
    # most_largest_line = max(len(f"{transaction['description']} {transaction['amount']}") for transaction in self.ledger)

    # lines = [
    #   f"{transaction['description']}{transaction['amount']:>{most_largest_line - len(transaction['description'])}.2f}" for transaction in self.ledger
    # ]

    # title = f"{self.name:*^{most_largest_line}}"

    # return title + "\n" + "\n".join(lines) + f"\nTotal: {self.get_balance():.2f}"

    lines = [
      f"{transaction['description'][:23]:<23}{transaction['amount']:>7.2f}" for transaction in self.ledger
    ]

    title = f"{self.name:*^30}\n"

    return title + "\n".join(lines) + f"\nTotal: {self.get_balance():.2f}"

  def get_withdrawals(self):
    return sum([abs(transaction["amount"]) for transaction in self.ledger if transaction["amount"] < 0])


class BarChart:
    def __init__(self, percentages, title=""):
        self.percentages = percentages
        self.title = title
        self.bars = []

    def build_bar(self):
        for level in range(100, -10, -10):
            self.bars.append(
                f"{str(level).rjust(3)}| " +
                "  ".join(
                    "o" if percentage >= level else " " for _, percentage in self.percentages
                ) + "  "
            )

    def _build_bar_x_axis(self):
        most_largest_name = max(len(name) for name, _ in self.percentages)
        x_axis = [
            "     " + "  ".join(
                name[i] if i < len(name) else " " for name, _ in self.percentages
            ) for i in range(most_largest_name)
        ]
        return [line + "  " for line in x_axis]

    def __str__(self):
        self.build_bar()  # Ensure the bars are built before generating the string
        bar_chart_str = self.title + "\n" \
            + "\n".join(self.bars) + "\n" \
            + "    " + "-" * (3 * len(self.percentages) + 1) + "\n" \
            + "\n".join(self._build_bar_x_axis())
        return bar_chart_str

def compute_total_withdrawals(categories):
    total_withdrawals = sum(category.get_withdrawals() for category in categories)
    return total_withdrawals

def compute_percentage_spent_by_category(category, total_withdrawals):
    if total_withdrawals > 0:
        percentage_spent = (category.get_withdrawals() / total_withdrawals) * 100
    else:
        percentage_spent = 0
    return percentage_spent

def create_spend_chart(categories):
    total_withdrawals = compute_total_withdrawals(categories)
    percentages = [
        (category.name, compute_percentage_spent_by_category(category, total_withdrawals))
        for category in categories
    ]

    return str(BarChart(percentages, "Percentage spent by category"))


if __name__ == "__main__":
  food = Category("Food")
  clothing = Category("Clothing")

  food.deposit(1000, "deposit")
  food.withdraw(10.15, "groceries")
  food.withdraw(15.89, "restaurant and more food for dessert")
  food.transfer(50, clothing)

  print(food)
  print()

  food = Category("Food")
  entertainment = Category("Entertainment")
  business = Category("Business")

  food.deposit(900, "deposit")
  entertainment.deposit(900, "deposit")
  business.deposit(900, "deposit")
  food.withdraw(105.55)
  entertainment.withdraw(33.40)
  business.withdraw(10.99)

  print(create_spend_chart([business, food, entertainment]))
