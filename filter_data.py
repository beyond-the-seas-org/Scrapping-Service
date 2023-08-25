import json

# Read data from the file
with open("data.json", "r") as file:
    lines = file.readlines()

# Create a list to store filtered data
filtered_data = []

# Process and filter data
for line in lines:
    # Filter the arrow
    line = line.replace("►", "")
    # Split the line
    line_parts = line.split()
    # Get the rank
    rank = line_parts[0]
    # Get the name of the university (assuming "   " is the delimiter)
    rest = " ".join(line_parts[2:]).split("   ")[0]
    #split based on " "
    name = rest.split(" ")
    #remove the last 2 elements
    name = name[:-2]

    #make the name a string
    name = " ".join(name)

    print(name)

    data = {
        "rank": rank,
        "name": name
    }

    filtered_data.append(data)

# Convert filtered data to JSON
json_data = json.dumps(filtered_data, indent=4)

# Write JSON data to a file
with open("filtered_data.json", "w") as file:
    file.write(json_data)
