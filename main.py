from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import auth
from routes import auth, products
app = FastAPI()

# Allow frontend requests (Vercel)
origins = [
    "http://localhost:3000",
    "https://your-frontend-domain.vercel.app"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth.router, prefix="/api/auth", tags=["Auth"])
app.include_router(auth.router, prefix="/api/auth", tags=["Auth"])
app.include_router(products.router, prefix="/api/products", tags=["Products"])

@app.get("/")
def read_root():
    return {"message": "SMF Jewels Backend Running!"}
