bill = float(input("how much is your bill?\n"))
tip = int(input("how much do you want to tip?\n"))
total_tip = bill * tip/100
total = total_tip + bill
print("here is your tip: $", total_tip)
print("here is your bill: $", total)
