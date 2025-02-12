import requests
import json
from agent import funtion_tools
url='https://aiproxy.sanand.workers.dev/openai/v1/chat/completions'
token='eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIzZjIwMDAyMzdAZHMuc3R1ZHkuaWl0bS5hYy5pbiJ9.tjKXBiC47bZVi3r-PCbHZd0cMXLRPz-1OjnA_HSB33k'
headers={
    "Authorization":f"Bearer {token}",
    "Content-Type":"application/json"
}
def send_request(q):
    response=requests.post(url=url,headers=headers,json={
    "model":"gpt-4o-mini",
    "messages":[
        {
            "role":"system","content":"You are a function-calling assistant. Work only within /data and its subdirectories. Never delete data."
        },
        {
        "role":"user","content":q,
    }],
    "tools":funtion_tools,
    "tool_choice":"auto"})
    message=response.json()['choices'][0]['message']['content']
    name_of_function=response.json()['choices'][0]['message']['tool_calls'][0]['function']['name']
    args=json.loads(response.json()['choices'][0]['message']['tool_calls'][0]['function']['arguments'])
    return (name_of_function,args,message)