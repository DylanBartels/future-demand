from fastapi import FastAPI

from api.router import api_router
from fastapi.middleware.cors import CORSMiddleware

from starlette.responses import Response

origins = [
    "https://localhost",
    "http://localhost:3000",
    "https://localhost:3000",
]


app = FastAPI(
    title="Future-Demand API",
    description="🎭Events API serving events scraped from https://www.lucernefestival.ch/en/program/summer-festival-22",
    version="0.1.0",
    redoc_url=None,
)


@app.get("/", include_in_schema=False)
def root():
    index = """
    <html>
    🎭Events API serving events scraped from https://www.lucernefestival.ch/en/program/summer-festival-22".
    </html>
    """
    return Response(index)


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)
