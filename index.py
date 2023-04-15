from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import ToolsRoutes


app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get('/')
def hello():
    return {"Hello" : "World"}

@app.get('/something')
def something():
    return {"Data": "Something"}

app.include_router(ToolsRoutes.router)