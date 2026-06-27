# bill = float(input("how much is your bill?\n"))
# tip = int(input("how much do you want to tip?\n"))
# total_tip = bill * tip/100
# total = total_tip + bill
# print("here is your tip: $", total_tip)
# print("here is your bill: $", total)

# for tip for lots of people
people = int(input("how many people are there?\n"))
bill = float(input("how much is your bill?\n"))
tip = int(input("how much do you want to tip?\n"))
total_tip = bill * tip/100
total = total_tip + bill
shared_tip = round(total_tip/people,2)
shared_total = round(total/people,2)
print("here is the total tip: $", round(total_tip,2))
print("here is the total bill: $", round(total,2))
print("here is how much each person will tip: $", round(shared_tip,2))
print("here is how much each person will pay: $", shared_total)

if 8 > 9:
    print("8 is greater than 9")
if 8>9:
