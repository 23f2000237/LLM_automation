# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "fastapi",
#     "uvicorn",
#   "fastapi.responses",
#   "python-dateutil",
#   "requests",
# ]
# ///
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from resp import send_request
from exec import execute
app = FastAPI()


@app.get("/read")
async def get_data(path:str):
    try:
        with open(path, "r") as file:
            content = file.read()
        return JSONResponse(content={"path": path}, status_code=200)
    except FileNotFoundError:
        return JSONResponse(content={"error": ""}, status_code=404)
   
@app.post("/run")
async def post_data(task:str):
    func,args=send_request(task)
    execute(func,args)
    return JSONResponse(content={"func": func,"args":args}, status_code=200)



if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="debug")