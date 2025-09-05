from fastapi import APIRouter

router = APIRouter(
    prefix="/mfa",
    tags=["mfa"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def get_mfa_status():
    # TODO: Call Graph API for MFA status report
    return [
        {"user": "user1@contoso.com", "status": "enabled"},
        {"user": "user2@contoso.com", "status": "disabled"},
    ]
