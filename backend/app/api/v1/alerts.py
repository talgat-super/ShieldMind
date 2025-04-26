from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def list_alerts():
    return {"alerts": ["Example alert 1", "Example alert 2"]}
