from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def read_users():
    # TODO: Call Graph API
    return [{"username": "user1@contoso.com"}, {"username": "user2@contoso.com"}]

@router.post("/")
async def create_user():
    # TODO: Call Graph API
    return {"status": "user created"}

@router.delete("/{user_id}")
async def delete_user(user_id: str):
    # TODO: Call Graph API
    return {"status": f"user {user_id} deleted"}
