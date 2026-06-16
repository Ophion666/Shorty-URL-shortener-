from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import links, redirect

app = FastAPI(title="Shorty API")
app.include_router(links.router)
app.include_router(redirect.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)