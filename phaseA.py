import subprocess
from datetime import datetime
from dateutil.parser import parse
import json
import os
import requests
import re
import base64
import numpy as np
import sqlite3
from resp import url,headers
def create_data(path,email):
    print(path)
    subprocess.run(['uv','run',path,email,'--root','./data'],capture_output=True, text=True, check=True)  
    
def format_data(path,version):
    file_path ='.'+path  
    print(file_path)
    subprocess.run('npx prettier@{version} --write {path}'.format(version=version,path=file_path),shell=True,check=True)
    original=open(file_path).read()
    expected = subprocess.run(
        ["npx", "prettier@3.4.2", "--stdin-filepath", path],
        input=original,
        capture_output=True,
        text=True,
        check=True,
        shell=True,
    ).stdout
    print(expected)


def count_weekday_occurrences(input_file, output_file, target_day):
    # Map weekday names to their corresponding integer values (Monday=0, ..., Sunday=6)
    input_file = os.path.abspath('.'+input_file)
    output_file = os.path.abspath('.'+output_file)
    weekday_map = {
        "monday": 0, "tuesday": 1, "wednesday": 2,
        "thursday": 3, "friday": 4, "saturday": 5, "sunday": 6
    }
    day_code=weekday_map[target_day.lower()]
    # Count the occurrences of the target weekday in the input file
    count = 0
    dates=open(input_file).read().splitlines()
    ct=sum(1 for date in dates if parse(date).weekday() == day_code)
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(str(ct))

def sort_array(input_file,first_target,second_target,output_file):
    input_file = os.path.abspath('.'+input_file)
    output_file = os.path.abspath('.'+output_file)
    contacts=json.load(open(input_file))
    contacts.sort(key=lambda x: (x[first_target], x[second_target]))
    with open(output_file, "w") as f:
        json.dump(contacts, f, indent=4)

def write_recent_first_lines(input_dir, output_file, num_files):
    input_dir = os.path.abspath('.'+input_dir)
    output_file = os.path.abspath('.'+output_file)
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

def extract_sender_email(inputfile, outputfile):
    inputfile = os.path.abspath('.'+inputfile)
    outputfile = os.path.abspath('.'+outputfile)
    s=open(inputfile).read()
    req=requests.post(url=url,headers=headers,json={
     "model":"gpt-4o-mini",
    "messages":[
        {"role": "system", "content": "Extract the sender's email address from the given email text. Reply with only the email address and nothing else."},
        {"role": "user", "content": s}
    ],})
    email=req.json()['choices'][0]['message']['content']
    with open(outputfile, 'w', encoding='utf-8') as out_file:
        out_file.write(email)

def generate_markdown_index(directory, output_file):
    index = {}
    output_file='.'+output_file
    directory='.'+directory
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):  # Only process markdown files
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, directory)
                with open(file_path, "r", encoding="utf-8") as f:
                    for line in f:
                        match = re.match(r"^#\s+(.+)", line)  # Find first H1 heading
                        if match:
                            index[relative_path] = match.group()
                            break  # Stop after first H1
    
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=4)


def card_ocr(inputimage,outputfile):
    inputimage = os.path.abspath('.'+inputimage)
    outputfile = os.path.abspath('.'+outputfile)
    b64img=base64.b64encode(open(inputimage,'rb').read()).decode('utf-8')
    req=requests.post(url=url,headers=headers,json={
     "model":"gpt-4o-mini",
    "messages":[
        {"role": "system", "content": "You are an OCR assistant. Extract and return the text from the image."},
        {"role": "user", "content": [{"type": "image_url", "image_url":{"url":f"data:image/jpeg;base64,{b64img}"}}]}
    ],})
    print(req.json())

def similar_comments(inputfile,outputfile):
    inputfile = '.'+inputfile
    outputfile = '.'+outputfile
    print(outputfile)
    comments=open(inputfile).read().splitlines()
    n=len(comments)
    max_val=0
    max_i,max_j=None,None
    vecs=[]
    url="https://aiproxy.sanand.workers.dev/openai/v1/embeddings"
    for i in range(n):
        payload = {"input": comments[i],"model": "text-embedding-3-small"}
        response = requests.post(url, headers=headers, json=payload)
        vecs.append(response.json()["data"][0]["embedding"])
    for i in range(n):
        for j in range(n):
            if i!=j:
                sim=np.dot(vecs[i],vecs[j])
                if sim>max_val:
                    max_val=sim
                    max_i=i
                    max_j=j
    with open(outputfile, "w", encoding="utf-8") as file:
        file.write(comments[max_i]+'\n' +comments[max_j])

def sql_query(database,table,Type,outputfile):
    conn=sqlite3.connect(database)
    outputfile=os.path.abspath('.'+outputfile)
    cursor=conn.cursor()
    Type=Type.lower()
    q='select sum(price*units) from {table} where lower(trim(type))="{Type}"'.format(table=table,Type=Type)
    cursor.execute(q)
    result=cursor.fetchone()[0]
    with open(outputfile,"w",encoding="utf-8") as file:
        file.write(str(result))
    conn.close()
