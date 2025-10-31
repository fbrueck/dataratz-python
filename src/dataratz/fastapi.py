from fastapi import FastAPI
from dataratz.api.children import children_router

app = FastAPI()
app.include_router(children_router)
