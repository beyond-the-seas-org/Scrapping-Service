from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json

professors_publications = {}
professors_data = []


def extract_info(text, link):
    publication_data = {}

    # Split the text into lines
    lines = text.split("\n")

    # Initialize variables to store the extracted information
    title = None
    date_of_conference = None
    doi = None
    citations = None
    ieee_keywords = []
    author_keywords = []

    # Iterate through the lines to find the relevant information
    for i, line in enumerate(lines):
        if i == 1:
            title = line.strip()
        elif "Date Added to IEEE Xplore:" in line:
            date_of_conference = line.split(":")[1].strip()
        elif "DOI:" in line:
            doi = line.split(":")[1].strip()
        elif "All Authors" in line:
            if i + 1 < len(lines):
                citations = lines[i + 1].strip()
        elif "Abstract" in line:
                # Collect the lines that follow the "Abstract:" section
            abstract_lines = []
            for j in range(i + 1, len(lines)):
                if "Published in:" in lines[j]:
                    break
                abstract_lines.append(lines[j])
            abstract = " ".join(abstract_lines).strip()

        elif "IEEE Keywords" in line:
            # take the rest of the lines
            rest_of_the_lines = lines[i + 1:]
            # split the lines by Author Keywords
            
            ieee = True
            author = False
            for keyword in rest_of_the_lines:
                if "Author Keywords" in keyword:
                    author = True
                    ieee = False
                    continue
                
                if "INSPEC: Controlled Indexing" in keyword or "INSPEC: Non-Controlled Indexing" in keyword:
                    ieee = False
                    author = False

                if "Metrics" in keyword:
                    break
                
                if ieee and keyword != ",":
                    ieee_keywords.append(keyword)
                elif author and keyword != ",":
                    author_keywords.append(keyword)

            
    # Store the extracted information in a dictionary
    publication_data["title"] = title
    publication_data["link"] = link
    publication_data["date_of_publication"] = date_of_conference
    publication_data["doi"] = doi
    publication_data["citations"] = citations
    publication_data["abstract"] = abstract
    publication_data["ieee_keywords"] = ieee_keywords
    publication_data["author_keywords"] = author_keywords

    return publication_data



# Read data from the JSON file
with open("professors_details.json", "r", encoding="utf-8") as data_file:
    data = json.load(data_file)

driver = webdriver.Chrome()

publication_data = {}

prof_count = 0
try:
    for d in data:
        professor = d["name"]
        publications = d["publications"]
        pub_count = 0
        prof_publications = []
        try:
            for pub in publications:
                # Go to the pub link and get the abstract, title, keywords, doi, citations , date and venue
                try:
                    print(pub)
                    driver.get(pub)
                    time.sleep(5)

                # scroll down to the bottom of the page to get the keywords
                
                    for i in range(1, 5):
                        driver.execute_script(f"window.scrollTo(0,{(i+1)*500})")
                        time.sleep(3)
                except:
                    pass


                
                try:
                    keyword_id = driver.find_element(By.ID, 'keywords')
                    keyword_id.click()
                    time.sleep(5)
                except:
                    time.sleep(5)


                
                try:
                    title = driver.find_element(By.ID, 'xplMainContentLandmark')
                    publication_data = extract_info(title.text, pub)
                    prof_publications.append(publication_data)
                    pub_count += 1
                    print("pub_count", pub_count, ", prof_count", prof_count)
                    if pub_count == 10:
                        break
                except:
                    pass
        except Exception as e:
            print(e)
            pass
        
        professors_publications = {
        "name": professor,
        "publications": prof_publications
        }
        print("professor:", professor)
        professors_data.append(professors_publications)
        prof_count += 1
        if prof_count == 150:
            break
except  Exception as e:
    print(e)
    pass

# write the data to a json file
with open("professors_ieee_publications.json", "w", encoding="utf-8") as json_file:
    json.dump(professors_data, json_file, ensure_ascii=False, indent=4)

driver.quit()

