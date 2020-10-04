"""
Assume that annualy salary has a fixed percentage increse every 6 months.
Under this case, how many months needed to afford the downpayment.
"""
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter % of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream House Price: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))
portion_down_payment = total_cost * 0.25
current_savings = 0
r = 0.04
n = 0
while current_savings < portion_down_payment:
    current_savings += current_savings * (r/12) + (annual_salary / 12) * portion_saved
    n += 1
    if n % 6 == 0:
        annual_salary = annual_salary * (1 + semi_annual_raise)
print("Number of Months: ", n)
