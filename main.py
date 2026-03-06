from fastapi import FastAPI, UploadFile, File

app = FastAPI()

@app.post("/upload-image")
async def upload_image(file: UploadFile = File(...)):
    
    contents = await file.read()

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "message": "Image received successfully"
    }

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)