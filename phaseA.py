import subprocess
from datetime import datetime
from dateutil.parser import parse
import json
import os
def create_data(path,email):
    print('came here')
    try:
        subprocess.run(['uv','run',path,email],capture_output=True, text=True, check=True)
        return '200'
    except:
        return '404'  
    
def format_data(path,version):
    with open(path, "r", encoding="utf-8") as f:
        file_contents = f.read()
        result = subprocess.run(["npx", f"prettier@{version}", "--stdin-filepath", path],input=file_contents,capture_output=True,text=True,check=True,shell=True)
        print(result.stdout)


def count_weekday_occurrences(input_file, output_file, target_day):
    # Map weekday names to their corresponding integer values (Monday=0, ..., Sunday=6)
    weekday_map = {
        "monday": 0, "tuesday": 1, "wednesday": 2,
        "thursday": 3, "friday": 4, "saturday": 5, "sunday": 6
    }
    day_code=weekday_map[target_day.lower()]
    # Count the occurrences of the target weekday in the input file
    count = 0
    with open(input_file, "r", encoding="utf-8") as file:
        for line in file:
            if parse(line).weekday() == day_code:
                count += 1
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(str(count) + "\n")

def sort_array(input_file,first_target,second_target,output_file):
    contacts=json.load(open(input_file))
    contacts.sort(key=lambda x: (x[first_target], x[second_target]))
    with open(output_file, "w") as f:
        json.dump(contacts, f, indent=4)

import os

def write_recent_first_lines(input_dir, output_file, num_files):
    all_files = [
        os.path.join(input_dir, f)
        for f in os.listdir(input_dir)
        if os.path.isfile(os.path.join(input_dir, f))
    ]
    all_files.sort(key=os.path.getmtime, reverse=True)
    first_lines = []
    for file_path in all_files[:num_files]:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                first_line = file.readline().rstrip('\n')
                first_lines.append(first_line)
        except Exception as e:
            print(f"Error reading file {file_path}: {e}")
    try:
        with open(output_file, 'w', encoding='utf-8') as out_file:
            for line in first_lines:
                out_file.write(line + '\n')
    except Exception as e:
        print(f"Error writing to file {output_file}: {e}")
