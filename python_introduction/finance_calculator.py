income = int(input("Enter your total monthly income:"))
expense = int(input("Enter your total monthly expense:"))
monthly_savings = income - expense
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print ("Your monthly savings are $",monthly_savings, ".")
print ("Projected savings after one year, with interest, is: $",projected_savings, ".")