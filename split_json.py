import json

def split_json(file_path):
    # I want to split the json file into chunks of 200
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
        
        chunks = 200
        for i in range(0,len(data), chunks):
            with open(f"chunk_{i}.json", 'w') as outfile:
                outfile.write(json.dumps(data[i:i+chunks]))

file_path = input("Enter the file path of the JSON file: ")
split_json(file_path)
