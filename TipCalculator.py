
# calculates tip based off the total bill and the number of people splitting the bill
print("Tip Calculator")
bill_total = float(input("Bill total? "))
num_people = int(input("How many are splitting the bill? "))
tip_percent = int(input("What percentage would you like to tip? "))
pay_amount = float((bill_total / num_people) + ((bill_total / num_people) * tip_percent/100))
roundPay = "{:.2f}".format(round(pay_amount, 2))
print(f"Tip amount: ${roundPay}")
