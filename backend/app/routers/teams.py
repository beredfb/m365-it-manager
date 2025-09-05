from fastapi import APIRouter

router = APIRouter(
    prefix="/teams",
    tags=["teams"],
    responses={404: {"description": "Not found"}},
)

@router.get("/active")
async def get_active_users():
    # TODO: Call Graph API for Teams activity report (last 7 days)
    return [
        {"user": "user1@contoso.com", "last_activity": "2023-10-27"},
    ]
