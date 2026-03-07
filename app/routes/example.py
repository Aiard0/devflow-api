from fastapi import APIRouter

router = APIRouter()

@router.get("/ping")
def ping():
    return {"ping": "pong"}

@router.get("/test")
def test():
    return {"test": "success!"}

@router.get("/devops")
def test():
    return {"devops": "ola mundo!"}
