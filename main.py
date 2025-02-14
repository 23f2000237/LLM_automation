# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "fastapi",
#     "uvicorn",
#   "fastapi.responses",
#   "python-dateutil",
#   "requests",
#   "numpy",
#   "duckdb",
#    "bs4",
#    "Pillow",
#    "pydub",
#    "SpeechRecognition",
#    "markdown",
# ]
# ///
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse,PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware
from resp import send_request
from exec import execute
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to specific domains for better security
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

@app.get("/read",response_class=PlainTextResponse)
async def get_data(path:str):
    try:
        with open(path, "r", encoding="utf-8") as file:
            content = file.read()
            content = "".join(content.splitlines()).strip()
        return content
        #try:
        #    op=eval(content)
        #    return JSONResponse(content=op, status_code=200)
        #except:
        #    return JSONResponse(content=content, status_code=200)
    #except Exception as e: 
    #    return JSONResponse(content={"error": str(e)}, status_code=500)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=404)
   
@app.post("/run")
async def post_data(task:str):
    func,args,message=send_request(task)
    if not message:
        execute(func,args)
    else:
        return JSONResponse(content={"message":"bad request"}, status_code=400)
    return JSONResponse(content={"message":"ok"}, status_code=200)



if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")