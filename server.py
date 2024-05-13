import uvicorn

if __name__=="__main__":
    uvicorn.run("app:app", host="10.7.151.204", port=8000, reload=True)