import socket
import uvicorn

if __name__=="__main__":
    host = socket.gethostbyname(socket.gethostname())
    uvicorn.run("app:app", host=host, port=8000, reload=True)