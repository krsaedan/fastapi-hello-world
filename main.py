import Request
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root(request: Request):
    print('request.headers')
    print(request.headers)
    print('request.headers[Authorization]')
    print(request.headers['Authorization'])
    return {"message": "Hello World"}

# if __name__ == '__main__':
#     uvicorn.run(app, port=8080, host='0.0.0.0')