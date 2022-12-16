import uvicorn
from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
async def root(request: Request):
    print('request.headers')
    print(request.headers)

    if ('Authorization' in request.headers):
        print('request.headers[Authorization]')
        print(request.headers['Authorization'])
    
    data = await request.json()
    print('data')
    print(data)

    return {"message": "Hello World"}

# if __name__ == '__main__':
#     uvicorn.run(app, port=8080, host='0.0.0.0')
