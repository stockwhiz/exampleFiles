import os
import json

directory = 'C:\\Users\\rohan\\OneDrive\\Desktop\\StockWhiz\\exampleFiles\\files'

for filename in os.listdir(directory):
    if filename.endswith('.ipynb'):
        # Show which file presently working on 
        print(filename)
        with open(os.path.join(directory, filename), 'w+', encoding='utf-8') as file:
            data = json.load(file)
            # Looping through the cells below
            for cell in data.cells:
                # Each cell has a source object
                # We will only edit the cells which are of type code
                if cell.cell_type == "code":
                    # Inside the source
                    # print('inside source')
                    source = cell.source
                    if isinstance(source,str):
                        # The source element is a string
                        result = [s + "\n" for s in source.split("\n")] 
                        print(result)