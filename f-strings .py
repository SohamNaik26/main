letter = "Hey my name is {1} and I am from {0}"
country = "India"
Name = "Soham"

print(letter.format(country, Name))
print(f"Hey my name is {Name} and I am from {country}")

txt = "For only {price: .2f} dollars!"
print(txt.format(price = 49.0999))

print(type(f"{2 * 30}"))