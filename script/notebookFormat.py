import os
import json

directory = 'C:\\Users\\rohan\\OneDrive\\Desktop\\StockWhiz\\exampleFiles\\files'

for filename in os.listdir(directory):
    if filename.endswith('.ipynb'):
        print(filename)
        with open(os.path.join(directory, filename), 'r+', encoding='utf-8') as file:
            data = json.load(file)
            # print(file.name)