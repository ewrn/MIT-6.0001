
current_savings = 0
r = 0.04
months = 0
portion_down_payment = 0.25

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

while current_savings <= total_cost * portion_down_payment:
    current_savings += current_savings * r/12
    current_savings += portion_saved * annual_salary/12    
    months += 1    
    
    if months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise
  
print("Number of months:", months)
