from fastapi import FastAPI,UploadFile,File,HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import shutil
import os

app = FastAPI(title = "Resume Management System")

os.makedirs("app/uploads/resumes",exist_ok=True)
os.makedirs("app/uploads/images",exist_ok=True)

#serve images
app.mount("/images",StaticFiles(directory="app/uploads/images"),name="images")

#upload resume
@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only Pdf files are allowed"
        )

    path = f"app/uploads/resumes/{file.filename}"

    with open(path,"wb") as buffer:
        shutil.copyfileobj(file.file,buffer)

    return{
        "message": "Resume uploaded successfully",
        "filename": file.filename
    }

#upload profile pictures
@app.post("/upload-image")
async def upload_image(file: UploadFile = File(...)):

    if not file.content_type.startswith("image/"):
        raise HTTPException(
            status_code=400,
            detail="Only image files are allowed."
        )

    path = f"app/uploads/images/{file.filename}"

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "message": "Image uploaded successfully",
        "filename": file.filename
    }

#download resume
@app.post("/download-resume/{filename}")
async def download_resume(filename: str):
    path = f"app/uploads/resumes/{filename}"

    if not os.path.exists(path):
        raise HTTPException(
            status_code=404,
            detail="Image not found"
        )
    return {
        "Image URL": f"http://127.0.0.1:8000/images/{filename}"
    }

