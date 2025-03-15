from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

# Enable CORS to allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from any frontend (change to ["http://localhost"] for security)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# List of clean jokes
jokes = [
    "Why don’t skeletons fight each other? They don’t have the guts.",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "What did one ocean say to the other ocean? Nothing, they just waved.",
    "Why don’t some couples go to the gym? Because some relationships don’t work out.",
    "Why did the golfer bring two pairs of pants? In case he got a hole in one."
]

# Root Endpoint for API Status Check
@app.get("/", include_in_schema=False)
@app.head("/")
def root():
    return {"message": "Welcome to the Joke API!"}

@app.get("/joke")
def get_joke():
    return {"joke": random.choice(jokes)}

