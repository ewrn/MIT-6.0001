semi_annual_raise = 0.07
r = 0.04
down_payment = 0.25 * 1000000
current_savings = 0
bisection_steps = 0

starting_salary = float(input("Enter your starting salary: "))

low = 0
high = 10000
best = False

while bisection_steps < 30:
    savings_rate = int((low + high)/2)
    annual_salary = starting_salary
    current_savings = 0

    for month in range(1,37):
        current_savings += current_savings * r/12
        current_savings += savings_rate/10000 * annual_salary/12

        if month % 6 == 0:
            annual_salary += annual_salary * semi_annual_raise

    bisection_steps += 1
    
    if abs(current_savings - down_payment) < 100:
        best = True
        break
    elif current_savings > down_payment:
        high = savings_rate
    else:
        low = savings_rate
        
if best:
    print("Best savings rate:", savings_rate/10000)
    print("Steps in bisection search:", bisection_steps)
else:
    print("It is not possible to pay the down payment in three years.")