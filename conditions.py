#first program

temp = input("Enter the temp: ")
if(temp=="hot"):
    print("Its a hot day\nDrink plenty water")
elif(temp=="cold"):
    print("Its a cold day\n Wear warm clothes")
else:
    print("Its a lovely day")

#second program
price = 200000
has_good_credit = False
if has_good_credit:
    down_payment= 0.1*price
    print(down_payment)
else:
    down_payment = 0.2 * price
    print(down_payment)

#Third program using logical operators
#using logical and
has_high_income=True
has_good_credit = True
if(has_high_income and has_good_credit):
    print("Eligible for loan")
else:
    print("not eligible")

#using logical or
has_high_income=True
has_good_credit = False
if(has_high_income or has_good_credit):
    print("Eligible for loan")
else:
    print("not eligible")

#using not
#using logical or
has_criminal_rec=False
has_good_credit = True
if(has_good_credit and not has_criminal_rec):
    print("Eligible for loan")
else:
    print("not eligible")

