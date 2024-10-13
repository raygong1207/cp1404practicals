
def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many number of months? "))

    for each_month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {each_month}: "))
        incomes.append(income)

    print_report(incomes, number_of_months)


def print_report(incomes, number_of_months):
    """Print income report for incomes over a given number of months."""
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, number_of_months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()
