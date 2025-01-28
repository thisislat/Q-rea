from fastapi import FastAPI
from pydantic import BaseModel
import os
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI
app = FastAPI()

# CORS Setup (Allows external API calls)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust to limit access to specific domains
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

# Main Execution Block (Ensures Railway Port Handling)
if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  # Railway assigns a port dynamically
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port)
