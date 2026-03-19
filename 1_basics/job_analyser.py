
def calculated_salary(base_salary,bonus_rate=.1):
    return base_salary * (1 + bonus_rate)

def calculated_bonus(total_salary, base_salary):
    return (total_salary - base_salary) / base_salary
