from itertools import product

from fastapi import FastAPI

from app.routers import category
from app.routers import products

app = FastAPI()

app.include_router(category.router)
app.include_router(products.router)


@app.get("/")
async def welcome() -> dict:
    return {"message": "My e-commerce app"}