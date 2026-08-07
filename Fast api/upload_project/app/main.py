import os
import shutil
from fastapi import FastAPI,UploadFile,File,HTTPException
from fastapi.staticfiles import StaticFiles

app = FastAPI()

os.makedirs("app/uploads", exist_ok=True)
os.makedirs("app/images", exist_ok=True)

#folder ko website pr accessible bnana
app.mount("/images",StaticFiles(directory="app/images"),name="images")

#upload a pdf
@app.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files allowed"
        )

    path = f"app/uploads/{file.filename}"

    with open(path,"wb") as buffer:
        shutil.copyfileobj(file.file,buffer)
    return {
        "message": "PDF Uploaded",
        "filename": file.filename
    }

#upload an image
@app.post("/upload-image")
async def upload_image(file: UploadFile = File(...)):
    if file.content_type not in ["image/jpeg","image/png","image/jpg"]:
        raise HTTPException(
            status_code=400,
            detail="Only image files allowed"
        )
    path = f"app/images/{file.filename}"

    with open(path,"wb") as buffer:
        shutil.copyfileobj(file.file,buffer)
    return{
        "message":"Image Uploaded",
        "filename":file.filename
    }

#reject non image files
@app.post("/only-image")
async def only_image(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(
            status_code=400,
            detail="Please upload an image only"
        )

    path = f"app/images/{file.filename}"

    with open(path,"wb") as buffer:
        shutil.copyfileobj(file.file,buffer)
    return{
        "message": "Image Uploaded Successfully"
    }

#limit file size to 1 mb
@app.post("/upload-limit")
async def upload_limit(file: UploadFile = File(...)):
    content = await file.read()

    max_size = 1 * 1024 * 1024

    if len(content) > max_size:
        raise HTTPException(
            status_code=400,
            detail="File size must be less than 1 MB"
        )
    path = f"app/uploads/{file.filename}"

    with open(path,"wb") as buffer:
        buffer.write(content)

    return {
        "message": "Uploaded Successfully"
    }

