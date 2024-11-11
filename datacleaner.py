# Author: Kelly Shields
# GitHub username: kellys1210
# Date: 10/03/2023
# Description:

import json

filePath = 'creatures_data.json'
testfilePath = 'creatures_data_test.json'

# Opens file in read mode
with open(filePath, 'r') as creatures:
    data = json.load(creatures)

    # Iterates over each dictionary in list 'data'
    for dict in data:

        # Iterates over each key-value pair in the dictionary
        for key, value in list(dict.items()):

            # If key = 'common_name', renamed to 'Common Name' by popping current key
            if key == 'common_name':
                dict['Common Name'] = dict.pop('common_name')

                # If 'Common Name' = 'false', sets to 'No Data'
                if value == 'false':
                    dict['Common Name'] = "No Data"

            # If key = 'countries', renamed to 'Countries' by popping current key
            elif key == 'countries':
                dict['Countries'] = dict.pop('countries')

                # If 'Countries' = empty list, sets to 'No Data'
                if value == []:
                    dict['Countries'] = 'No Data'

                # If Countries = list, converted to string with each element separated by a comma
                elif isinstance(value, list):
                    dict['Countries'] = ', '.join(value)

            # If key = 'scientific_name', renamed to 'Scientific Name' by popping current key
            elif key == 'scientific_name':
                dict['Scientific Name'] = dict.pop('scientific_name')

            # This can be removed if not necessary; preserves order of keys in each dict
            else:
                dict['image'] = dict.pop('image')


# Opens file in write mode, all prev. data is cleared and overwritten with random num
with open(testfilePath, 'w') as creatures_test:
    json.dump(data, creatures_test, indent=4)

