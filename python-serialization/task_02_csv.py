
#!/usr/bin/python3
import csv
import json


def convert_csv_to_json(csv_filename):
    try:
        with open(csv_filename, 'r') as csv_file:
            # Use DictReader to convert each row into a dictionary
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)

        # Serialize the list of dictionaries to JSON
        json_data = json.dumps(data, indent=4)

        # Write the serialized JSON data to data.json
        with open('data.json', 'w') as json_file:
            json_file.write(json_data)
        
        return True
    except FileNotFoundError:
        print(f"File '{csv_filename}' not found.")
        return False
