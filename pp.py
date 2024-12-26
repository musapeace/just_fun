weight = float(input("enter you weight:"))

# asking the user for choice 
choice = input("do you want the weight in 'k' or do you want the weight in 'p'")
if choice == "k":
    weight_in_kilogram = weight / 2.205
    print(f"weight in kg: {weight_in_kilogram}")
elif choice == "p":
    weight_in_pounds = weight * 2.205
    print(f"weight in pounds: {weight_in_pounds}")
else:
    print(done)       