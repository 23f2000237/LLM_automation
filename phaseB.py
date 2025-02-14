import requests
import subprocess
import sqlite3
import duckdb
from bs4 import BeautifulSoup
from PIL import Image
import speech_recognition as sr
from pydub import AudioSegment
import markdown
def fetch_api(url,parameters,save_path):
    save_path='.'+save_path
    if not parameters: 
        val=requests.get(url)
    if parameters:
        val=requests.get(url,params=parameters)
    with open(save_path,'w',encoding='utf-8') as out_file:
        out_file.write(val.text)

def clone_repo(url):
    subprocess.run(["git", "clone", url])
    subprocess.run(["git","commit","-m","initial commit"])
    subprocess.run(["git","push","-u","origin","main"])
    status = subprocess.run(["git", "status", "--porcelain"],check=False)

def run_query(query,database,db_type):
    database='.'+database
    if db_type=='duckdb':
        conn=duckdb.connect(database)
    else:
        conn=sqlite3.connect(database)
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        print(result)
        conn.commit()
    finally:
        conn.close()

def scrape(url,file=None):
    response = requests.get(url, timeout=5)
    response.raise_for_status() 
    soup = BeautifulSoup(response.text, "html.parser")
    tex=soup.get_text()
    if file:
        if file[0]=='/':
            file='.'+file
        with open(file, "w", encoding="utf-8") as f:
            f.write(tex)

def comp_resize_image(inputfile,outputfile):
    image = Image.open(inputfile)
    image.thumbnail((128, 128))
    image.save(outputfile)

def transcribe_audio(mp3_path,outputfile):
    audio = AudioSegment.from_mp3(mp3_path)
    wav_path = mp3_path.replace(".mp3", ".wav")
    audio.export(wav_path, format="wav")

    # Load audio for transcription
    recognizer = sr.Recognizer()
    with sr.AudioFile(wav_path) as source:
        audio_data = recognizer.record(source)

    # Transcribe using Google's free API
    try:
        text=recognizer.recognize_google(audio_data)
        if outputfile:
            with open(outputfile, "w", encoding="utf-8") as file:
                file.write(text)
    except sr.UnknownValueError:
        return "Could not understand the audio."
    except sr.RequestError:
        return "API request failed."


def convert_md_html(md_file, html_file):
    md_file='.'+md_file
    html_file='.'+html_file
    with open(md_file, "r", encoding="utf-8") as file:
        md = file.read()
    html = markdown.markdown(md)
    with open(html_file, "w", encoding="utf-8") as file:
        file.write(html)
    print(html)