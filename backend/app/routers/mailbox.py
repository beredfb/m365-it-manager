from fastapi import APIRouter

router = APIRouter(
    prefix="/mailbox",
    tags=["mailbox"],
    responses={404: {"description": "Not found"}},
)

@router.get("/usage")
async def get_mailbox_usage():
    # TODO: Call Graph API for mailbox usage report
    return [
        {"user": "user1@contoso.com", "usage_gb": 48.5, "quota_gb": 50},
        {"user": "user2@contoso.com", "usage_gb": 10.2, "quota_gb": 50},
    ]
