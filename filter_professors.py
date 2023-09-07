import json
# Sample data
data_file = open("professors.json", "r", encoding="utf-8")
data = data_file.read()

# Split the data by lines
lines = data.split("\n")

# Initialize variables to store the university and faculties
professors = []
faculties = []

# Iterate through the lines
for line in lines:
    # Check if the line contains the ▼ symbol and extract the university name
    if "▼" in line:
        # Add the previous university to the list of universities
        if len(faculties) > 0:
            university_faculties = {
                "university": university,
                "faculties": faculties
            }
            professors.append(university_faculties)
            faculties = []

        university = line.split("▼")[1].strip()
        # Ignore the last 2 parts
        university = university.split()[:-2]
        # Combine all parts of the university name
        university = " ".join(university)

    # Check if the line contains faculty information
    elif "Faculty" not in line and line.strip() != "":
        # Extract faculty names (excluding lines with "Faculty")
        faculty_info = line.split()
        # Combine all parts of the faculty name
        faculty_name = " ".join(faculty_info[:-2])
        # Split the name with space and ignore the parts that start with small letters
        faculty_name = faculty_name.split()
        faculty_name = [name for name in faculty_name if name[0].isupper()]
        faculty_name = " ".join(faculty_name)

        # Make a dictionary of faculty name and research areas
        faculty = {
            "name": faculty_name
        }
        # Add the faculty to the list of faculties
        faculties.append(faculty)

# Add the last university to the list of universities
if university and faculties:
    university_faculties = {
        "university": university,
        "faculties": faculties
    }
    professors.append(university_faculties)

# Write the data into a file in JSON format
with open("university_professors.json", "w", encoding="utf-8") as file:
    json.dump(professors, file, indent=4)
