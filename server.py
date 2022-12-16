from fastapi import FastAPI, APIRouter


app = FastAPI()
router = APIRouter()


@router.get("/")
def inicial():
    return True


app.include_router(router)
