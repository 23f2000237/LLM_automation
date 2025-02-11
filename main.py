# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "fastapi",
#     "uvicorn",
#   "fastapi.responses",
#   "python-dateutil",
#   "requests",
#   "numpy"
# ]
# ///
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
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

@app.get("/read")
async def get_data(path:str):
    path='.'+path
    try:
        with open(path, "r", encoding="utf-8") as file:
            content = file.read()
            content = "".join(content.splitlines()).strip()
        try:
            op=eval(content)
            return op
        except:
            return content
        #try:
        #    op=eval(content)
        #    return JSONResponse(content=op, status_code=200)
        #except:
        #    return JSONResponse(content=content, status_code=200)
    #except Exception as e: 
    #    return JSONResponse(content={"error": str(e)}, status_code=500)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
   
@app.post("/run")
async def post_data(task:str):
    func,args=send_request(task)
    execute(func,args)
    return JSONResponse(content={"func": func,"args":args}, status_code=200)



if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="debug")