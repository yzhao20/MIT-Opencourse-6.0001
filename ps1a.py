"""
This script is used to find how much months you need
to afford to the downpayment of a house. Assuming you
are save a certain percentage of your monthly salary to 
saving account. 
It passed ALL test cases.
"""
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter % of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream House Price: "))
portion_down_payment = total_cost * 0.25
current_savings = 0
r = 0.04
n = 0
while current_savings < portion_down_payment:
    current_savings += current_savings * (r/12) + (annual_salary / 12) * portion_saved
    """
    Alternative to the above line: current_savings = current_savings * (1 + r / 12) + (annual_salary / 12) * portion_saved
    """
    n += 1
print("Number of Months: ", n)
