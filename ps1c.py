def rate(starting_salary):
    """
    Using bisection method to figure out what is the best rate 
    to save each month so that we can afford the down payment 
    in 3 years. 
    This hasn NOT been checked as we need to call this function,
    but working computer is not allowed to do so. 
    """
    total_cost = 10 ** 6
    portion_down_payment = 0.25
    down_payment = total_cost * portion_down_payment
    semi_annual_raise = 0.07
    current_saving = 0
    r = 0.04
    n = 0 
    low = 0 
    high = 10000
    portion_saved = 0
    while n <= 36 and abs(current_saving - down_payment < 100):
        current_saving += current_saving * (r / 12) + (starting_salary_salary / 12 )* (portion_saved / 10000)
        n += 1
        if n % 6 == 0:
            starting_salary_salary = starting_salary_salary * (1 + semi_annual_raise)
        if current_saving < down_payment:
            low = portion_saved
        else:
            high = portion_saved
        portion_saved = (low + high) / 2
    if abs(current_saving - down_payment < 100):
        print("Best savings rate:", portion_saved)
        print("Steps in bisection search:", n)
    else:
        print("It is not possible to pay the down payment in three years.")
