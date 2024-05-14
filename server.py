import uvicorn

if __name__=="__main__":
    uvicorn.run("app:app", host="192.168.1.8", port=1000, reload=True)