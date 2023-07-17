import os
import shutil

search_path = r'C:\testxml'
home_directory = r'C:\Users\kur'

for root, directories, files in os.walk(search_path):
    for file in files:
        if file.endswith('.xml'):
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as f:
                if 'Testcase' in f.read():
                    destination_path = os.path.join(home_directory, file)
                    shutil.copyfile(file_path, destination_path)
                    print(f"File '{file}' copied to '{destination_path}'.")
