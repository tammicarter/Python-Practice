''' 
Ask user there weight (inpounds), 
convert it to Kilograms and print on the terminal.
'''
# # My Solution to the above Algorithm

# Input() function gets input from the user
name = input(" Good Day, what is your name?: ")
conversion = input( " {} Let's convert your current weight into kilograms. Press enter ".format(name))
# Or
# float() function converts the numerical string returned by the input() function into a numerical value
pounds = float(input(" Enter your weigth in pounds: "))
# the formula to convert lbs to kgs is 1 lb = 0.453592 kgs
kilo_grams = pounds * 0.453592
# Round the float value to 2 decimal places using round( 2 arguments req.)
print(round(kilo_grams, 2))
# printing conclusion
#print("So, You are {} lbs and {} total kgs 🥰".format(pounds, kilo_grams))
# OR to refactor: place the f in front of the sting and the values inside of the braces {}
print(f"So, You are {pounds} lbs and {kilo_grams} total kgs 🥰" )
# Mosh's Solution
weight_lbs = input ('Weight (lbs): ')
weight_kg = int(weight_lbs) * 0.45
print(weight_kg)
