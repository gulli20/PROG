### CODE STARTS ###

# Modifier to convert miles to km (km/mile) and to AU (mile/AU)
km_mi_mod = 1.609344
au_mi_mod = 92955887.8

# Voyager 1 speed (miles/hour) and the starting distance from the sun in miles
mi_speed = 38241
distance_mi = 16637000000

# Ask for the days after 9/25/09 and convert them to hours
days = int(input("Number of days after 9/25/09: "))
hours = days * 24

# The distance that Voyager 1 has traveled
distance_traveled_mi = mi_speed * hours

# All distances calculated, km and AU rounded
final_distance_mi = distance_mi + distance_traveled_mi
final_distance_km = round(final_distance_mi * km_mi_mod)
final_distance_au = round(final_distance_mi/au_mi_mod)

# Print the output for the distances
print("Miles from the sun:", final_distance_mi)
print("Kilometers from the sun:", final_distance_km)
print("AU from the sun:", final_distance_au)

### CODE ENDS ###