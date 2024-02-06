print("Welcome to Tip Calculator!!!!!")
print()

bill_amount = float(input("Please enter the total amount of bill: \n"))
print(f"So the bill amount is {bill_amount} Euros.")
print()

tip = int(input("Please enter the percent of tip you would like to give 10 , 12 , 15 ?: \n"))
print(f"So you've selected to give a tip of {tip} %.")
print()

persons = int(input("Please enter the number of people you would like to split the bill between: \n"))
print()
bill_per_person = ((bill_amount + (bill_amount * (tip / 100))) /persons)

print(f"The amount each person has to pay is " + "{:.2f}".format(bill_per_person) + " Euros")
print()
