import requests
import json
import os
from agent import funtion_tools
url='https://aiproxy.sanand.workers.dev/openai/v1/chat/completions'
token=os.getenv("AI_PROXY_TOKEN") 
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
