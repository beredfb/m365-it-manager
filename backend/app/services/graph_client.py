import httpx
import asyncio
from os import getenv

GRAPH_BASE_URL = getenv("GRAPH_BASE_URL", "https://graph.microsoft.com/v1.0")
# In a real app, token management would be more sophisticated
# This is a placeholder for where you'd get your auth token
ACCESS_TOKEN = getenv("AZURE_CLIENT_SECRET") # Example: NOT FOR PRODUCTION

class GraphClient:
    def __init__(self):
        self.client = httpx.AsyncClient(
            base_url=GRAPH_BASE_URL,
            headers={
                "Authorization": f"Bearer {ACCESS_TOKEN}",
                "Content-Type": "application/json"
            }
        )

    async def get(self, url: str, params: dict = None):
        max_retries = 3
        retry_delay = 1
        for attempt in range(max_retries):
            try:
                response = await self.client.get(url, params=params)
                response.raise_for_status()
                return response.json()
            except (httpx.HTTPStatusError, httpx.RequestError) as e:
                if isinstance(e, httpx.HTTPStatusError) and e.response.status_code in [429, 503, 504]:
                    if attempt < max_retries - 1:
                        await asyncio.sleep(retry_delay)
                        retry_delay *= 2  # Exponential backoff
                        continue
                # For other errors or if retries are exhausted, raise the exception
                raise e

graph_client = GraphClient()

async def get_graph_client() -> GraphClient:
    return graph_client
