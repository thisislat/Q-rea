import os
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS Setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# InquiryRequest Model
class InquiryRequest(BaseModel):
    topic: str

# Inquiry Endpoints
@app.post("/generate_question")
def generate_question(request: InquiryRequest):
    return {"question": f"What are the deeper implications of {request.topic}?"}

@app.post("/find_contradictions")
def find_contradictions(request: InquiryRequest):
    return {"contradictions": [f"Potential contradiction in {request.topic}"]}

@app.post("/generate_analogy")
def generate_analogy(request: InquiryRequest):
    return {"analogy": f"{request.topic} is like a river—constantly flowing and reshaping itself."}

@app.post("/summarize_context")
def summarize_context(request: InquiryRequest):
    return {"summary": f"Summary of {request.topic}: Key insights and takeaways."}

# Root Check
@app.get("/")
def read_root():
    return {"message": "Hello, Q'rea!"}

# Ensure correct PORT and HOST
if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  
    host = os.getenv("HOST", "0.0.0.0")  # Add this line
    uvicorn.run(app, host=host, port=port)
