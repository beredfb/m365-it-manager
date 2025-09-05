from fastapi import APIRouter

router = APIRouter(
    prefix="/licenses",
    tags=["licenses"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def get_assigned_licenses():
    # TODO: Call Graph API
    return [{"user": "user1@contoso.com", "licenses": ["E3", "EMS"]}]

@router.patch("/{user_id}")
async def assign_remove_licenses(user_id: str):
    # TODO: Call Graph API to add/remove licenses
    return {"status": f"Licenses updated for {user_id}"}
