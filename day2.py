print("Welcome to the tip calculator")
bill = float(input("What was the total bill? \n"))
percent_tip = int(input("What percentage tip would you like to give? \n %"))
people = int(input("How many people to split the bill? \n"))

# Calculate the total with the bill
total_bill = bill + (bill / (100/percent_tip))
split_bill = round(total_bill / people, 2)

print(f"Each person should pay ${split_bill}")
