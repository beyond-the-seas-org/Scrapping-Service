# Given input text
input_text = "United States 37\u00b025\u203239\u2033N 122\u00b010\u203212\u2033W"

# Split the input text by space
parts = input_text.split()

# Extract the country name (first part)
country_name = " ".join(parts[:2])

print(country_name)
