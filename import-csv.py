import csv 
import json 
  
csvFilePath = '/Users/colbymay/Colby's Google Drive/School/Data-Vis/D3-Data-Vis/Node Visualization/ad-interests.csv'  
jsonFilePath = '/Users/colbymay/Colby's Google Drive/School/Data-Vis/D3-Data-Vis/Node Visualization/ad-interests.json'
data={}


# Function to convert a CSV to JSON 
# Takes the file paths as arguments 
def make_json(csvFilePath, jsonFilePath): 
      
    # create a dictionary 
    data = {} 
      
    # Open a csv reader called DictReader 
    with open(csvFilePath, encoding='utf-8') as csvFile: 
        csvReader = csv.DictReader(csvFile) 
          
        # Convert each row into a dictionary  
        # and add it to data 
        for rows in csvReader: 
              
            # Assuming a column named 'No' to 
            # be the primary key 
            key = rows['No'] 
            data[key] = rows 
  
    # Open a json writer, and use the json.dumps()  
    # function to dump data 
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonFile: 
        jsonFile.write(json.dumps(data, indent=4)) 
          
# Driver Code 
  
# Decide the two file paths according to your  
# computer system 
csvFilePath = 'ad-interests.csv'
jsonFilePath = 'ad-interests.json'

data = []
with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for rows in csvReader:
        id = rows['id']
        data[id] = rows
  
# Call the make_json function 
    with open(jsonFilePath, w) as jsonFile:
        jsonFile.write(json.dumps(data,indent=4))

