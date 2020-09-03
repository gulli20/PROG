### CODE STARTS ###

print("Welcome to car rentals!")

# List of price per day and miles driven for budget and daily classes
question = 'y'
price_per_day_b = 40.0
price_per_day_d = 60.0
price_per_miles = 0.25

while question == 'y':
    # initialize Car Rental program
    question = input("Would you like to continue (y/n)? ")
    if question == 'n':
        break
    # Ask the user series of question about the usage of the rental car
    customer_code = input("Customer code (b or d): ")
    n_days = int(input("Number of days: "))
    miles_start = int(input("Odometer reading at the start: "))
    miles_end = int(input("Odometer reading at the end: "))

    # For customers classified as budget
    if customer_code == 'b':
        miles_driven = miles_end - miles_start
        print("Miles driven: ", miles_driven)
        price_miles_b = miles_driven * price_per_miles
        price_days_b = n_days * price_per_day_b
        amount_due_b = price_miles_b + price_days_b
        amount_due_b = round(amount_due_b, 1)
        print("Amount due: ", amount_due_b)
    # For customers classified as daily
    elif customer_code == 'd':
        miles_driven = miles_end - miles_start
        print("Miles driven: ", miles_driven)
        # Calculate if customer has driven more than 100 miles per day
        miles_per_day = n_days * 100
        if miles_driven > miles_per_day:
            price_miles_d = (miles_driven - miles_per_day) * price_per_miles
        else:
            price_miles_d = 0
        price_days_d = n_days * price_per_day_d
        amount_due_d = price_miles_d + price_days_d
        amount_due_d = round(amount_due_d, 1)
        print("Amount due: ", amount_due_d)

### CODE ENDS ###